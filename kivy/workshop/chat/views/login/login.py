from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
Builder.load_file('./views/login/login.kv')


class Login(Screen):

    def __init__(self, controler, **kw):
        super().__init__(**kw)
        self.controller = controler
        self.popup = Popup(title='Error', content=Label(
            text='Username or password is incorrect'), size_hint=(None, None), size=(400, 150))

    def insert_text(self, instance: TextInput, text: str):
        if len(instance.text) > 8 or len(instance.text) > 7:
            instance.text = instance.text[:8]

    def username_validation(self, instance: TextInput, text: str):
        if len(instance.text) > 8:
            instance.text = instance.text[:8]

    def on_press(self):
        if(0 < len(self.ids.username.text) < 7 and len(self.ids.password.text) == 8):
            self.manager.current = 'chat'
            self.controller.client.name = self.ids.username.text
        else:
            self.popup.open()
