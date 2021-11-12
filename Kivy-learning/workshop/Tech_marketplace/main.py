import os
import importlib
from kivy.core.window import Window
from kaki.app import App
from kivymd.app import MDApp
Window.size = (360, 640)
class MyApp(App,MDApp):
    DEBUG=1
    KV_FILES = {
        os.path.join(os.getcwd(),'lib','Root','root.kv'),
        os.path.join(os.getcwd(),'lib','Onboard','onboard.kv'),
        os.path.join(os.getcwd(),'lib','component','Tab','tab.kv'),
    }
    CLASSES = {
        'Root':'lib.Root.root',
        'OnboardScreen':'lib.Onboard.onboard',
        'Tab':'lib.component.Tab.tab'
    }
    AUTORELOADER_PATHS=[
        ('.',{'recursive':True})
    ]
    
    def build_app(self):
        self.icon = 'images/Logo.png'
        self.title = 'MyApp'
        import lib.Root.root
        Window.bind(on_keyboard=self._rebuild)
        importlib.reload(lib.Root.root)
        return lib.Root.root.Root()
    
    def _rebuild(self,*args):
        if args[1] == 32:
            return self.rebuild()

if __name__ == '__main__':
    MyApp().run()
    