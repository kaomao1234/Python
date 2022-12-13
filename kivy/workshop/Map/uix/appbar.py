from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.uix.widget import Widget
from kivy.metrics import dp
from uix.align import Align
from kivy.utils import get_color_from_hex as hex_to_bin
from uix.colors import Colors


class AppBar(MDBoxLayout, CommonElevationBehavior):
    def __init__(self,
                 leading: Widget = None, trailing: Widget = None, title: Widget = None,  # type: ignore
                 center_title=True, height=dp(56), elevation=2.5,color=hex_to_bin("#2196f3")):
        super().__init__(height=height, elevation=elevation,
                         size_hint_y=None, md_bg_color=color, padding=[16, 16, 16, 16],)
        if leading is not None:
            self.add_widget(Align(
                x='center',
                child=leading
            ))
        if title is not None:
            self.add_widget(Align(
                x='center' if center_title else 'left',
                child=title
            ))

        if trailing is not None:
            self.add_widget(Align(
                x='center',
                child=trailing
            ))
