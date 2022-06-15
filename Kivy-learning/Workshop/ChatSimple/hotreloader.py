from kaki.app import App
from kivymd.app import MDApp
import os
from kivy.core.window import Window
from kivymd_extensions.akivymd import *
import importlib
Window.softinput_mode = 'pan'




class Hotreloader(MDApp, App):
    DEBUG = 1
    KV_FILES = {
        os.path.join(os.getcwd(), 'Views', 'Root.kv'),
        os.path.join(os.getcwd(), 'Views', 'Intro','IntroScreen.kv'),
        os.path.join(os.getcwd(), 'Views', 'Login','LoginScreen.kv'),
        os.path.join(os.getcwd(), 'Views', 'Social','SocialScreen.kv'),
        os.path.join(os.getcwd(), 'Views', 'OpenPost','OpenPostScreen.kv'),
        os.path.join(os.getcwd(), 'Components', 'backgroundLogin','backgroundLogin.kv'),
        os.path.join(os.getcwd(), 'Components', 'postbox','postbox.kv'),
    }
    CLASSES = {
        'RootScreen': 'Views.Root',
        'IntroScreen': 'Views.Intro.IntroScreen',
        'LoginScreen': 'Views.Login.LoginScreen',
        'SocialScreen': 'Views.Social.SocialScreen',
        'OpenPostScreen': 'Views.OpenPost.OpenPostScreen',
        'BackgroundLogin': 'Components.backgroundLogin.backgroundLogin',
        'PostBox': 'Components.postbox.postbox',
    }
    AUTORELOADER_PATHS = [
        (os.getcwd(), {'recursive': True})
    ]
    def build_app(self, first=False):
        from Views.Root import Root
        Window.bind(on_keyboard=self._rebuild)
        return Root()

    def _rebuild(self, *ar):
        if ar[1] == 32:
            return self.rebuild()


if __name__ == "__main__":
    Hotreloader().run()
