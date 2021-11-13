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
        os.path.join(os.getcwd(),'lib','Onboard','lib','Connexion','connexion.kv'),
        os.path.join(os.getcwd(),'lib','Onboard','lib','Connexion','lib','ConnectScreen','connectscreen.kv'),
        os.path.join(os.getcwd(),'lib','Onboard','lib','Connexion','lib','RegisterScreen','registerscreen.kv'),
        os.path.join(os.getcwd(),'lib','Onboard','lib','Connexion','lib','LoginScreen','loginscreen.kv')
    }
    CLASSES = {
        'Root':'lib.Root.root',
        'OnboardScreen':'lib.Onboard.onboard',
        'Tab':'lib.component.Tab.tab',
        'ConnexionScreen':'lib.Onboard.lib.Connexion.connexion',
        'ConnectScreen':'lib.Onboard.lib.Connexion.lib.ConnectScreen.connectscreen',
        'RegisterScreen':'lib.Onboard.lib.Connexion.lib.RegisterScreen.registerscreen',
        'LoginScreen':'lib.Onboard.lib.Connexion.lib.LoginScreen.loginscreen'
    }
    AUTORELOADER_PATHS=[
        ('.',{'recursive':True})
    ]
    def __init__(self,**kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.icon = 'images/Logo.png'
        self.title = 'MyApp'
        
    def build_app(self):
        import lib.Root.root
        Window.bind(on_keyboard=self._rebuild)
        importlib.reload(lib.Root.root)
        return lib.Root.root.Root()
    
    def _rebuild(self,*args):
        if args[1] == 32:
            return self.rebuild()
MyApp().run()