from kivy.uix.label import Label
from kivymd.app import MDApp

from uix.appbar import AppBar
from uix.colors import Colors
from uix.scaffold import Scaffold
from uix.text import Text


class App(MDApp):
    def build(self):
        return Scaffold(
            appbar=AppBar(
                # centerTitle=False,
                title=Text("Appbar", font_size=20)),
            body=Label(text="Center")
        )


App().run()
