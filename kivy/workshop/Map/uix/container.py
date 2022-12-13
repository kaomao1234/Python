from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex as hex_to_bin
from uix.colors import Colors


class Container(MDBoxLayout):
    def __init__(self, child: Widget = None, width=0, height=0, padding=[8, 8, 8, 8], radius=[0, 0, 0, 0],
                 background_color=hex_to_bin("#fafafa")):
        super().__init__(size_hint_x=None if width != 0 else 1,
                         size_hint_y=None if height != 0 else 1, height=height, width=width, padding=padding,
                         radius=radius, md_bg_color=background_color)
        if child is not None:
            self.add_widget(child)
