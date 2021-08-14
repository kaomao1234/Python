from kivy import Config
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '730')
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

Builder.load_string("""
#: import get_color_from_hex kivy.utils.get_color_from_hex
<Intro@Screen>:
    name:'Logo'
    FitImage:
        source:'F:/DocCode/PythonWorkShop/WorkKivy/Project/WinterCakeApp/Icon/Nature_Flower_Red_beauty_salon_stamp_Logo_.png'
        
<SignUp@Screen>:
    name:'Sigup'
    title:title
    canvas:
        Color:
            rgb:(0.9333333333333333, 0.9215686274509803, 0.9098039215686274, 1.0)
        Rectangle:
            size:root.width,root.height
    MDGridLayout:
        rows:8
        Image:
            source:'F:/DocCode/PythonWorkShop/WorkKivy/Project/WinterCakeApp/Icon/Nature_Flower_Red_beauty_salon_stamp_Logo_crop.png'
            size_hint_y: None
            height:200
        MDLabel:
            id:title
            text:'[size=20][b]Login To Your Account[/b][/size]'
            size_hint_y: None
            height:50
            halign: "center"
            valign:'center'
            markup: True
        AnchorLayout:  
            size_hint_y: None
            anchor_x:'center'
            height:57
            MDTextField:
                hint_text:'Email'
                size_hint_y: None
                size_hint_x:None
                width:325
                mode: "rectangle"
                line_color_normal:(0.4588235294117647, 0.2823529411764706, 0.2784313725490196, 1.0)
        AnchorLayout:  
            size_hint_y: None
            anchor_x:'center'
            height:57
            MDTextField:
                hint_text:'Password'
                size_hint_y: None
                size_hint_x:None
                width:325
                mode: "rectangle"
                line_color_normal:(0.4588235294117647, 0.2823529411764706, 0.2784313725490196, 1.0)
        MDLabel:
            text:'[size=12][b]Or Continue With[/b][/size]'
            size_hint_y: None
            valign: "center"
            halign: "center"
            markup: True
            height:20
        AnchorLayout:
            size_hint_y:None
            height:57
            anchor_x:'center'
            MDBoxLayout:
                orientation:'horizontal'
                size_hint_x:None
                width:152*2
                spacing:65
                MDRectangleFlatIconButton:
                    icon:'facebook'
                    text:'Facebook'
                    font_size:14
                    size_hint_x: None
                    theme_text_color: "Custom"
                    icon_color:get_color_from_hex('#0275d8')
                    
                MDRectangleFlatIconButton:
                    icon:'google'
                    text:'Google'
                    font_size:14
                    size_hint_x: None
                    theme_text_color: "Custom"
                    icon_color:get_color_from_hex('#d9534f')
                    line_color:get_color_from_hex('#d9534f')
                    text_color:get_color_from_hex('#d9534f')
        AnchorLayout:
            anchor_x:'center' 
            size_hint_y: None
            height:40      
            MDRectangleFlatButton:
                size_hint_y: None
                text: "Forgot Your Password?"
                theme_text_color: "Custom"
                text_color: (0.4588235294117647, 0.2823529411764706, 0.2784313725490196, 1.0)
                line_color: 0, 0, 0, 0
        AnchorLayout:
            anchor_x: 'center'
            size_hint_y: None
            height:57
            Button:
                text:'Login' 
                font_size:16
                size_hint_x:None
                background_color:(0.4588235294117647, 0.2823529411764706, 0.2784313725490196, 1.0)
                width:141
""")


class Intro(Screen):
    def __init__(self, **kwargs):
        super(Intro, self).__init__(**kwargs)


class SignUp(Screen):
    def __init__(self, **kwargs):
        super(SignUp, self).__init__(**kwargs)


class sm(ScreenManager):
    def __init__(self, **kwargs):
        super(sm, self).__init__(**kwargs)
        self.transition = SlideTransition()
        self.add_widget(Intro())
        self.add_widget(SignUp())
        Clock.schedule_once(self.waiting, 5)

    def waiting(self, *e):
        self.current = 'Sigup'


class WinterCakeApp(MDApp):
    def build(self):
        return sm()


if __name__ == '__main__':
    WinterCakeApp().run()
