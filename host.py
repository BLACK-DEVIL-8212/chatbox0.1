import _thread
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from socket import *

con =""
host=input("Enter your ip address :  ")
port = 4444

s = socket()
s.bind((host,port))
chatOb= None

class Chat (BoxLayout):

    def __init__(self):
        super(Chat,self).__init__()
    
    def clickAction(self):
        global conn
        textMsg=self.ids['EntryBox'].text
        if textMsg !='':
            self.ids['ChatBox'].text += '\nYou:' +textMsg
            self.ids['EnteryBox'].text += ''
            conn.sendall(textMsg.encode())

class ChatappInterface(App):
    def build(self):
        global chatOb
        chatOb = Chat()
        Window.size = (400,500)
        return chatOb
    
def getHostConnected():
    global conn, chatOb
    import time
    time.sleep(1)
    s.listen(1)
    chatOb.ids['ChatBox'].text='[+] waiting for connection'
    conn, addr = s.accept()
    chatOb.id['ChatBox'].text="[+] connected with"+ str(addr)
    while 1:
        try:
            data = conn.recv(1024)
            chatOb.ids['ChatBox'].text += '\nOther: '+ data.decode()
        except:
            getHostConnected()
    conn.close()

if __name__  == "__main__":
    _thread.start_new_thread(getHostConnected,())
    ChatappInterface().run()