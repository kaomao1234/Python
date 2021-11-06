from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from time import sleep
from kivy.clock import Clock
# from functools import partial
class RegisterScreen(MDScreen):
    def __init__(self,**kw):
        super(RegisterScreen, self).__init__(**kw)

    def on_password(self,instance):
        instance.password = False
        Clock.schedule_once(lambda s : setattr(instance,'password',True),0.2)
    
    def on_lengt(self,instance_text,instance_helper):
        pass
    def on_in(self):
        pass
    def on_out(self):
        pass