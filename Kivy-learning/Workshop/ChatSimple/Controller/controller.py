from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd_extensions.akivymd import *
import os
KV_FILES = {
    os.path.join(os.getcwd(), 'Views', 'Root.kv'),
    os.path.join(os.getcwd(), 'Views', 'Intro', 'IntroScreen.kv'),
    os.path.join(os.getcwd(), 'Views', 'Login', 'LoginScreen.kv'),
    os.path.join(os.getcwd(), 'Components',
                 'backgroundLogin', 'backgroundLogin.kv'),
}
for i in KV_FILES:
    Builder.load_file(i)
from Components.backgroundLogin.backgroundLogin import BackgroundLogin
from Views.Root import Root
from Views.Intro.IntroScreen import IntroScreen
from Views.Login.LoginScreen import LoginScreen

class TalkTalker(MDApp):
    def build(self):
        return Root()