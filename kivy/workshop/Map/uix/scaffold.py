from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.widget import MDWidget
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.metrics import dp
from kivy.utils import get_color_from_hex as hex_to_bin
from uix.appbar import AppBar


class Scaffold(MDScreen):
    def __init__(self, appbar: AppBar = None, body: MDWidget = None, bottom: MDWidget = None):
        super().__init__(MDBoxLayout(appbar, body, bottom, orientation="vertical", spacing="10dp"),
                         md_bg_color=hex_to_bin("#fafafa"))
