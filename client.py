import _thread
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from socket import *

con =""
host= input("Enter you ip address: ")
port = 4444

s = socket()
s.bind((host,port))
chatOb= None

class Chat(BoxLayout):
    
    def __init__(self):
        super(Chat,self).__init__()

    def clickAction(self):
        global s
        textMsg = self.ids['EntryBox'].text
        if textMsg != '':
            self.ids['ChatBox'].text += '\nYou: '+textMsg
            self.ids['EntryBox'].text = ''
            s.sendall(textMsg.encode())

class ChatAppInterface(App):
    def build(self):
        global chatOb
        chatOb = Chat()
        Window.size = (400,500)
        return chatOb

def getClientConnected():
    global chatOb
    import time 
    time.sleep(1)
    try:
        s.connect((host,port))
        chatOb.ids['ChatBox'].text ="[+] Succcessfully connected"
    except:
        chatOb.ids["TextBox"].text ='[+] Unable to connect'
        return
    while 1:
        try:
            data = s.recv(1024)
            chatOb.ids['ChatBox'].text += '\nOther: '+data.decode()
        except:
            chatOb.ids['ChatBox'].text = '[+] peer has disconnected'
            break
    s.close()

if __init__ == '__main__':
    _thread.start_new_thread(getClientConnected,())
    ChatAppInterface().run()