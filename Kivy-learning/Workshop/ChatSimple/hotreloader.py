from kaki.app import App
from kivymd.app import MDApp
import os
from kivy.core.window import Window
from kivymd_extensions.akivymd import *
import importlib

from Views.Root import Root


class Hotreloader(MDApp, App):
    DEBUG = 1
    KV_FILES = {
        os.path.join(os.getcwd(), 'Views', 'Root.kv'),
        os.path.join(os.getcwd(), 'Views', 'Intro','IntroScreen.kv'),
        os.path.join(os.getcwd(), 'Views', 'Login','LoginScreen.kv'),
        os.path.join(os.getcwd(), 'Views', 'Social','SocialScreen.kv'),
        os.path.join(os.getcwd(), 'Components', 'backgroundLogin','backgroundLogin.kv'),
        os.path.join(os.getcwd(), 'Components', 'textbox','textbox.kv'),
    }
    CLASSES = {
        'RootScreen': 'Views.Root',
        'IntroScreen': 'Views.Intro.IntroScreen',
        'LoginScreen': 'Views.Login.LoginScreen',
        'SocialScreen': 'Views.Social.SocialScreen',
        'BackgroundLogin': 'Components.backgroundLogin.backgroundLogin',
        'TextBox': 'Components.textbox.textbox',
    }
    AUTORELOADER_PATHS = [
        (os.getcwd(), {'recursive': True})
    ]
    def build_app(self, first=False):
        import Views.Root as root
        Window.bind(on_keyboard=self._rebuild)
        return root.Root()

    def _rebuild(self, *ar):
        if ar[1] == 32:
            return self.rebuild()


if __name__ == "__main__":
    Hotreloader().run()
