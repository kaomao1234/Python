from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp

class MDLive(App,MDApp):
    DEBUG=1
    CLASSES ={
        'MainScreen':'maincode'
    }
    AUTORELOADER_PATHS=[
        (".",{'recursive':True})
    ]
    def build_app(self,*args):
        print("Auto reload.")
        return Factory.MainScreen()
    
MDLive().run()
