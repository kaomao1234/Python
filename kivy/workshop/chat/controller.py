from kivy.uix.screenmanager import ScreenManager
from client.client import Client
from widgets.chatitem.chatitem import ChatItem
from views.chat.chat import Chat
from views.login.login import Login
class Controller(ScreenManager):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.client = Client('localhost', 9999)
        self.add_widget(Login(self,name='login'))
        self.add_widget(Chat(self,name='chat'))