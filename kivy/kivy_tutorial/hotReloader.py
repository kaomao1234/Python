from kaki.app import App
from kivymd.app import MDApp
from kivy.factory import Factory
class MDLive(App,MDApp):
    DEBUG=1
    CLASSES = {
        'ScrollWidget':'RecycleByScrollView'
    }
    AUTORELOADER_PATHS=[
        (".",{'recursive':True})
    ]
    def build_app(self,*args):
        print('Auto reload.')
        return Factory.ScrollWidget()

MDLive().run()