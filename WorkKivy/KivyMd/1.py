import kivymd
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
Builder.load_string(""" 
<ItemBackdropFrontLayer@TwoLineAvatarListItem>
    icon: "android"

    IconLeftWidget:
        icon: root.icon


<MyBackdropFrontLayer@ItemBackdropFrontLayer>
    backdrop: None
    text: "Lower the front layer"
    secondary_text: " by 50 %"
    icon: "transfer-down"
    pos_hint: {"top": 1}
    _no_ripple_effect: True
    
<Example>:
    Image:
        size_hint: .8, .8
        source: "data/logo/kivy-icon-512.png"
        pos_hint: {"center_x": .5, "center_y": .6}
    MyBackdropFrontLayer:
""")


class Example(MDScreen):
    pass


class App(MDApp):
    def build(self):
        return Example()


if __name__ == '__main__':
    App().run()
