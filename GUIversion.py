import tkinter
from pythoncrawler import *

def getScreenSize():
    return root.winfo_screenwidth(),root.winfo_screenheight()

class Frame(object):
    def __init__(self,root):
        self._root=root
    def Label(self,label):
        root.title(label)

    def CenterWindow(self,width,height,posX,posY):
        size = '%dx%d+%d+%d' % (width,height,posX,posY)
        root.geometry(size)

def setLabel(event):
    labelName.set('Downloading ...')
def Excute(event):
    url = Url.get()
    loginUrl = LoginUrl.get()
    username=entryUsername.get()
    password=entryPassword.get()
    folder_name=entryFolder_name.get()
    labelName.set('Download')
    if loginUrl:
        TestMoodle(loginUrl, url, username, password, folder_name)
    else:
        TestEncryptWebsite(url,username,password,folder_name)

root=tkinter.Tk()
frame=Frame(root)
frame.Label('Certain File Download')
width, height = getScreenSize()
frame.CenterWindow(width / 2, height / 2, width / 4, height / 4)

content=tkinter.StringVar()
contentLogin=tkinter.StringVar()
radio1=tkinter.Radiobutton(root,text='Operating System',value='https://cs4.ucc.ie/moodle/course/view.php?id=122',variable=content)
radio2=tkinter.Radiobutton(root,text='Web Servers',value='https://cs4.ucc.ie/moodle/course/view.php?id=190',variable=content)
radio3=tkinter.Radiobutton(root,text='Intermediate Programming',value='https://cs4.ucc.ie/moodle/course/view.php?id=140',variable=content)
radio4=tkinter.Radiobutton(root,text='Algorithm and Datastructure',value='http://www.cs.ucc.ie/~kb11/teaching/CS2515/Home/',variable=content)
radio5=tkinter.Radiobutton(root,text='Logic Design',value='http://wgrothaus.ucc.ie/',variable=content)
radio6=tkinter.Radiobutton(root,text='Login Page',value="https://cs4.ucc.ie/moodle/login/index.php",variable=contentLogin)

labelUrl=tkinter.Label(root,text='* Please Enter Url')
Url=tkinter.Entry(root,textvariable=content,width=100)
labelLoginUrl=tkinter.Label(root,text='Please Enter Login Url(if Needed)')
LoginUrl=tkinter.Entry(root,width=100,textvariable=contentLogin)
labelUsername=tkinter.Label(root,text='Username')
labelPassword=tkinter.Label(root,text='Password')
labelFolder_name=tkinter.Label(root,text='Download into (folder)')
entryUsername=tkinter.Entry(root,width=100)
entryPassword=tkinter.Entry(root,width=100,show='*')
entryFolder_name=tkinter.Entry(root,width=100)

labelName=tkinter.StringVar()
labelName.set('Download')
button=tkinter.Button(root,textvariable=labelName,bg='DodgerBlue',activebackground='SkyBlue',font=('Arial,12'),width= 20, height=2)
button.bind('<Button-1>',setLabel)

button.bind('<ButtonRelease>', Excute)

radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()
radio5.pack()
labelUrl.pack()
Url.pack()
radio6.pack()
labelLoginUrl.pack()
LoginUrl.pack()
labelUsername.pack()
entryUsername.pack()
labelPassword.pack()
entryPassword.pack()
labelFolder_name.pack()
entryFolder_name.pack()
button.pack(side='bottom')


root.mainloop()
