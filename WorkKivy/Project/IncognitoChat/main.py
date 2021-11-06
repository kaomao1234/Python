import os
from kivy import Config
Config.set('graphics', 'multisamples', '0')
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import importlib
from kivy.core.window import Window
from kaki.app import App
from kivymd.app import MDApp
Window.size = (360,640)
class Live(App,MDApp):
    DEBUG=1
    KV_FILES = {
        os.path.join(os.getcwd(),'Screens','IntroScreen','intro_screen.kv'),
        os.path.join(os.getcwd(),'Screens','OnboardScreen','onboard_screen.kv'),
        os.path.join(os.getcwd(),'Screens','LoginScreen','login_screen.kv'),
        os.path.join(os.getcwd(),'Screens','RegisterScreen','register_screen.kv'),
        os.path.join(os.getcwd(),'assets','modules','LineInput','lineinput.kv'),
        os.path.join(os.getcwd(),'assets','modules','TwoLineInput','twolineinput.kv')
    }
    CLASSES = {
        'OnboardScreen':'Screens.OnboardScreen.onboard_screen',
        'IntroScreen':'Screens.IntroScreen.intro_screen',
        'LoginScreen':'Screens.LoginScreen.login_screen',
        'RegisterScreen':'Screens.RegisterScreen.register_screen',
        'LineInput':'assets.modules.LineInput.lineinput',
        'TwoLineInput':'assets.modules.TwoLineInput.twolineinput'
    }
    AUTORELOADER_PATHS = [
        ('.',{'recursive':True})
    ]
    
    def build_app(self):
        import Screens.OnboardScreen.onboard_screen
        Window.bind(on_keyboard=self._rebuild)
        importlib.reload(Screens.OnboardScreen.onboard_screen)
        
        return Screens.OnboardScreen.onboard_screen.OnboardScreen()

    def _rebuild(self,*args):
        if args[1] == 32:
            return self.rebuild()

Live().run()