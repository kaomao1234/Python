from kivy import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation 
from kivy.lang import Builder
from kivy.clock import Clock
Builder.load_string("""
#:import Window kivy.core.window.Window
#:import get_color_from_hex kivy.utils.get_color_from_hex
<SC1@MDScreen>:
    black:0,0,0,1
    copper_rust:get_color_from_hex("#9b4f4f")
    white:get_color_from_hex("#ffffff")
    weathered_stone:get_color_from_hex("#c4c4c4")
    AnchorLayout:
        anchor_y: 'top'
        FitImage:
            id:bg_img
            source:"C:/Users/borip/Documents/GitHub/PythonWorkShop/WorkKivy/Project/WinterCakeApp/Icon/Rose_Vale_Flowers_Soft_Organic_Fashion_Logo.png"
    MDBoxLayout:
        id:sign_in_frame
        y:-1000
        size_hint_y:0.5
        orientation:'vertical'
        radius:[dp(30),dp(30),dp(0),dp(0)]
        md_bg_color:root.white
        Label:
            text:"Hello world"
            font_size: 30
            color: root.black
""")
class SC1(MDScreen):
    def __init__(self, **kwargs):
        super(SC1, self).__init__(**kwargs)
        Clock.schedule_once(self.start,4)
    def start(self,*e):
        p = Animation(y=0, duration=0.2)
        m = Animation(size_hint_y=0.6,duration=0.2)
        p.start(self.ids.sign_in_frame)
        m.start(self.ids.bg_img)

    
        

class TestApp(MDApp):
    def build(self):
        return SC1()

def main():
    TestApp().run()
if __name__ == '__main__':
    main()