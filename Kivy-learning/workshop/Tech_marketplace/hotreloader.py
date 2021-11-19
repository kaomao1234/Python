import os
import importlib
from kivy.core.window import Window
from kaki.app import App
from kivymd.app import MDApp
from pprint import pprint
Window.size =(360, 640)
class MyApp(App,MDApp):
    DEBUG=1
    KV_FILES = {
        os.path.join(os.getcwd(),'component','ProductCard','productcard.kv'),
        os.path.join(os.getcwd(),'component','PromoteCard','promotecard.kv'),
        os.path.join(os.getcwd(),'component','SalesFlatButton','salesflatbutton.kv'),
        os.path.join(os.getcwd(),'component','UnderIconButton','undericonbutton.kv'),
        os.path.join(os.getcwd(),'lib','Root','root.kv'),
        os.path.join(os.getcwd(),'lib','OnboardScreen','onboard.kv'),
        os.path.join(os.getcwd(),'lib','OnboardScreen','Screens','ConnexionScreen','connexion.kv'),
        os.path.join(os.getcwd(),'lib','OnboardScreen','Screens','ConnexionScreen',"Screens",'ConnectScreen','connect.kv'),
        os.path.join(os.getcwd(),'lib','OnboardScreen','Screens','ConnexionScreen','Screens','RegisterScreen','register.kv'),
        os.path.join(os.getcwd(),'lib','OnboardScreen','Screens','ConnexionScreen','Screens','LoginScreen','login.kv'),
        os.path.join(os.getcwd(),'lib','MainScreen','main.kv'),
        os.path.join(os.getcwd(),'lib','CategoryScreen','category.kv'),
        os.path.join(os.getcwd(),'lib','CategoryScreen','Screens','HomeScreen','home.kv'),
        os.path.join(os.getcwd(),'lib','CategoryScreen','Screens','CategoriesScreen','categories.kv'),
        os.path.join(os.getcwd(),'lib','CategoryScreen','Screens','ProductScreen','product.kv')
    }
    CLASSES = {
        'ProductCard':'component.ProductCard.productcard',
        'PromoteCard':'component.PromoteCard.promotecard',
        'UnderIconButton':'component.UnderIconButton.undericonbutton',
        'SalesFlatButton':'component.SalesFlatButton.salesflatbutton',
        'Tab':'component.Tab.tab',
        'RightContainer':'component.RightContainer.rightcontainer',
        'Root':'lib.Root.root',
        'OnboardScreen':'lib.OnboardScreen.onboard',
        'ConnexionScreen':'lib.OnboardScreen.Screens.ConnexionScreen.connexion',
        'ConnectScreen':'lib.OnboardScreen.Screens.ConnexionScreen.Screens.ConnectScreen.connect',
        'RegisterScreen':'lib.OnboardScreen.Screens.ConnexionScreen.Screens.RegisterScreen.register',
        'LoginScreen':'lib.OnboardScreen.Screens.ConnexionScreen.Screens.LoginScreen.login',
        'MainScreen':'lib.MainScreen.main',
        "CategoryScreen":'lib.CategoryScreen.category',
        'HomeScreen':'lib.CategoryScreen.Screens.HomeScreen.home',
        'CategoriesScreen':'lib.CategoryScreen.Screens.CategoriesScreen.categories',
        'ProductScreen':'lib.CategoryScreen.Screens.ProductScreen.product'
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