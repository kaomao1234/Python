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
        os.path.join(os.getcwd(),'lib','OnboardScreen','onboard.kv'),
        os.path.join(os.getcwd(),'lib','OnboardScreen','Screens','ConnexionScreen','connexion.kv'),
        os.path.join(os.getcwd(),'lib','OnboardScreen','Screens','ConnexionScreen',"Screens",'ConnectScreen','connect.kv'),
        os.path.join(os.getcwd(),'lib','OnboardScreen','Screens','ConnexionScreen','Screens','RegisterScreen','register.kv'),
        os.path.join(os.getcwd(),'lib','OnboardScreen','Screens','ConnexionScreen','Screens','LoginScreen','login.kv'),
        os.path.join(os.getcwd(),'lib','CategoryScreen','category.kv'),
        os.path.join(os.getcwd(),'lib','CategoryScreen','Screens','HomeScreen','home.kv'),
        
    }
    CLASSES = {
        'Tab':'component.Tab.tab',
        'RightContainer':'component.RightContainer.rightcontainer',
        'Root':'lib.Root.root',
        'OnboardScreen':'lib.OnboardScreen.onboard',
        'ConnexionScreen':'lib.OnboardScreen.Screens.ConnexionScreen.connexion',
        'ConnectScreen':'lib.OnboardScreen.Screens.ConnexionScreen.Screens.ConnectScreen.connect',
        'RegisterScreen':'lib.OnboardScreen.Screens.ConnexionScreen.Screens.RegisterScreen.register',
        'LoginScreen':'lib.OnboardScreen.Screens.ConnexionScreen.Screens.LoginScreen.login',
        "CategoryScreen":'lib.CategoryScreen.category',
        'HomeScreen':'lib.CategoryScreen.Screens.HomeScreen.home'
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