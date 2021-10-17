from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

from kivymd.app import MDApp
from kivymd.uix.behaviors import CircularRippleBehavior,RectangularRippleBehavior, BackgroundColorBehavior
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


Builder.load_string('''
<RectDIYButton@Button>:
    size_hint: None, None
    radius:[20,20]
    text:'Hello world'
    background_color:0,0,0,0
    ripple_scale:1
    # size: "250dp", "50dp"
    # pos_hint: {"center_x": .5, "center_y": .5}
''')

class RectDIYButton(Button,CircularRippleBehavior,ButtonBehavior,BackgroundColorBehavior):
    # md_bg_color = [0, 0, 1, 1]
    def __init__(self,**kwargs):
        super(RectDIYButton, self).__init__(**kwargs)


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        sc = MDScreen()
        p = MDBoxLayout(orientation='vertical',radius=[20,20],size_hint=(None, None),pos_hint={'center_x': .5, 'center_y':.5},md_bg_color = [0, 0, 1, 1])
        p.add_widget(RectDIYButton())
        sc.add_widget(p)
        return sc


Example().run()