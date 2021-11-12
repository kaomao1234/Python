from pprint import pprint
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivy.animation import Animation
from kivy import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Builder.load_string("""
#:import Window kivy.core.window.Window
#:import get_color_from_hex kivy.utils.get_color_from_hex
<TLongin@MDFloatLayout>:
    black:0,0,0,1
    copper_rust:get_color_from_hex("#9b4f4f")
    white:get_color_from_hex("#ffffff")
    weathered_stone:get_color_from_hex("#c4c4c4")
    FitImage:
        id:background
        source:"C:/Users/borip/Documents/GitHub/PythonWorkShop/WorkKivy/Project/WinterCakeApp/Icon/Rose_Vale_Flowers_Soft_Organic_Fashion_Logo.png"
    MDBoxLayout:
        y:-1000
        size_hint_y:0.5
        orientation:'vertical'
        spacing:10
        id:frontLayout
        radius:[dp(32),dp(32),dp(0),dp(0)]
        md_bg_color:root.white
        orientation:'vertical'
        Label:
            size_hint_y:None
            height:21
            text: "[size=18]SIGN IN[/size]"
            markup:True
            color:root.copper_rust
        MDBoxLayout:
            size_hint_y: None
            orientation:'vertical'
            AnchorLayout:
                size_hint_y:None
                anchor_x:'left'
                height:16
                Label:
                    size_hint_x: None
                    text: "[size=14]Username[/size]"
                    markup:True
                    color:root.black
            TextInput:
                size_hint_y: None
                height:37
                background_color:root.white if self.focus else root.weathered_stone
            AnchorLayout:
                size_hint_y:None
                anchor_x:'left'
                height:16
                Label:
                    size_hint_x: None
                    text: "[size=14]Password[/size]"
                    markup:True
                    color:root.black
            TextInput:
                size_hint_y: None
                height:37
                background_color:root.white if self.focus else root.weathered_stone
            AnchorLayout:
                anchor_x:"center"
                size_hint_y:None
                height:52
                id:box
                MDBoxLayout:
                    orientation:'horizontal'
                    AnchorLayout:
                        anchor_x:'center'
                        MDFillRoundFlatButton:
                            size_hint: None,None
                            -height:box.height
                            -width:144
                            text: "Sign In"
                            font_size:14
                            md_bg_color: root.copper_rust
                    AnchorLayout:
                        anchor_x:'center'
                        MDFillRoundFlatButton:
                            size_hint: None,None 
                            -height:box.height
                            -width:144
                            text: "Sign Up"
                            font_size:14
                            md_bg_color: root.copper_rust
            AnchorLayout:
                anchor_x:'center'
                size_hint_y: None
                height:38
                MDTextButton:
                    size_hint_x: None
                    text: "Forgot Password?"
                    color:root.copper_rust
                    font_size:14
    
""")


class TLongin(MDFloatLayout):
    def __init__(self, **kwargs):
        super(TLongin, self).__init__(**kwargs)
        self.on_start()
        # pprint(dir(self.ids.m))

    def on_start(self):
        trans = Animation(y=0, duration=0.7)
        back_trans = Animation(duration=0.7)
        back_trans.start(self.ids.background)
        trans.start(self.ids.frontLayout)


class App(MDApp):
    def build(self):
        return TLongin()


if __name__ == '__main__':
    App().run()