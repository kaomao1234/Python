from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp

class MDLive(App,MDApp):
    # DEBUG=1
    CLASSES ={
        'BoxApp':'mdraise_btn'
    }
    AUTORELOADER_PATHS=[
        (".",{'recursive':True})
    ]
    def build_app(self,*args):
        print("Auto reload.")
        return Factory.BoxApp()
MDLive().run()
