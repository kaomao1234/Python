from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from lib.Screen_py.root import Root
from lib.Screen_py.onboard import OnboardScreen
from component.Tab.tab import Tab
from lib.Connexion.connexion import ConnexionScreen
from lib.ConnectScreen.connectscreen import ConnectScreen
from lib.RegisterScreen.registerscreen import RegisterScreen
from lib.LoginScreen.loginscreen import LoginScreen
Window.size = (360, 640)
path = {
        os.path.join(os.getcwd(),'lib','Root','root.kv'),
        os.path.join(os.getcwd(),'lib','Onboard','onboard.kv'),
        os.path.join(os.getcwd(),'lib','Onboard','Connexion','connexion.kv'),
        os.path.join(os.getcwd(),'lib','ConnectScreen','connectscreen.kv'),
        os.path.join(os.getcwd(),'lib','RegisterScreen','registerscreen.kv'),
        os.path.join(os.getcwd(),'lib','LoginScreen','loginscreen.kv')
    }
for i in path:
    Builder.load_file(i)
class MyApp(MDApp):
    def __init__(self,**kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.icon = 'images/Logo.png'
        self.title = 'MyApp'
    
    def build(self):
        return Root()

MyApp().run()