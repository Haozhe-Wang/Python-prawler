from urllib import request,parse
import http.cookiejar
import re
import os

def OpenRequest(agent,username,password,url):
    headers = {'User-Agent': agent}
    data = {}
    data['username'] = username
    data['password'] = password
    postdata = parse.urlencode(data).encode('UTF-8')

    Req = request.Request(url, postdata, headers)
    return Req

def OpenOpener():
    cookie=http.cookiejar.CookieJar()
    opener=request.build_opener(request.HTTPCookieProcessor(cookie))
    return opener

def Login(agent,username,password,url):
    Req=OpenRequest(agent,username,password,url)
    opener=OpenOpener()
    opener.open(Req)
    return opener

def OpenEncryptWebsite(fileurl,username,password):
    p = request.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, fileurl, username, password)
    handler = request.HTTPBasicAuthHandler(p)
    opener = request.build_opener(handler)
    request.install_opener(opener)
    return request

def Openwebsite(url,opener=None):
    if opener:
        result = opener.open(url)
        content = result.read().decode('UTF-8')
    else:
        content=request.urlopen(url).read().decode('UTF-8')
    return content

def IfHaveFolder(path):
    if path[0]=='/' or path[0]=='\\' or ':'in path[:5]:
        folder=os.path.exists(path)
    else:
        path=os.getcwd()+'\\'+path
        folder=os.path.exists(path)
    return folder,path

def DownloadFile(File,name,folderPath):
    # request.urlretrieve(url,filename=pathname,reporthook=reporthook,data=data)
    Have,path=IfHaveFolder(folderPath)
    if not Have:
        os.makedirs(path)
    f=open(path+'/'+name,'wb')
    block_sz = 8192
    while True:
        buffer = File.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()

def TestMoodle(loginurl,url,username,password,folder_name,agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'):
    opener = Login(agent, username, password, loginurl)
    content = Openwebsite(url, opener)
    files = re.findall(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*/([a-zA-Z0-9\r_-]+\.pdf)[?=a-zA-Z0-9_]*)",content)
    for file in files:
        file_content=opener.open(file[0])
        DownloadFile(file_content,file[-1],folder_name)

def TestEncryptWebsite(url,username,password,folder_name,agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'):
    content = Openwebsite(url)
    files = re.findall(r"href=\"([a-zA-Z0-9\r_/-]+\.pdf)[?=a-zA-Z0-9_\"]*", content)
    fileurl = []
    for i in range(len(files)):
        if url[-1] == '/':
            fileurl.append(url + files[i])
        else:
            fileurl.append(url + '/' + files[i])
        index = files[i].rfind('/')
        if index >= 0:
            files[i] = files[i][index + 1:]

    for i in range(len(fileurl)):
        Req = OpenEncryptWebsite(fileurl[i], username, password)
        page = Req.urlopen(fileurl[i])
        DownloadFile(page, files[i], folder_name)

def Test():
    #This is a moodle test
    loginurl="https://cs4.ucc.ie/moodle/login/index.php"
    url='https://cs4.ucc.ie/moodle/course/view.php?id=122'
    agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    password=''  #hardcode your password
    username=''  #hardcode your username
    folder_name='operating system files'

    TestMoodle(loginurl,url,username,password,agent,folder_name)


    #This is a test that need to enter username and password for the server
    url='http://www.cs.ucc.ie/~kb11/teaching/CS2515/Lectures/'
    password='cs1'
    username='cs1'
    TestEncryptWebsite(url,username,password,'Datastructure and Algorithms')

if __name__=='__main__':
    Test()

