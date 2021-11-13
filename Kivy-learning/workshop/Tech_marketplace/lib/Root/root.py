from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from lib.Onboard.onboard import OnboardScreen
class Root(ScreenManager):
    def __init__(self,**kw):
        super(Root, self).__init__(**kw)
    