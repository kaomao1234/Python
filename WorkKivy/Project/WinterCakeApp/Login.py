import kivymd
from kivy import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'minimum_width', '400')
Config.set('graphics', 'minimum_height', '600')
# Config.set('graphics', 'resizable', '0')
# Config.set('graphics', 'multisamples', '0')
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
Builder.load_string("""
<LoginPage@MDGridLayout>:
    rows:2
    adaptive_height: True
    canvas:
        Color:
            # rgb:(0.4588235294117647, 0.2823529411764706, 0.2784313725490196, 1.0)
            rgb:(0.9333333333333333, 0.9215686274509803, 0.9098039215686274, 1.0)
        Rectangle:
            size:root.width,root.height
    MDBoxLayout:
        orientation:'vertical'
        size_hint_y: None
        padding:[50, -50]
        # spacing: '10dp'
        MDLabel:
            id:logLabel
            halign: "center"
            valign:'center'
            text: "[size=20]Login[/size]"
            # text_size:self.size
            size_hint_y: None
            markup: True
        MDTextField:
            # text_size:self.size
            hint_text:'Your email address.'
            size_hint_y: None
            line_color_focus:(0.4588235294117647, 0.2823529411764706, 0.2784313725490196, 1.0)
        MDTextField:
            # text_size:self.size
            hint_text:'Your password.'
            size_hint_y: None
            line_color_focus:(0.4588235294117647, 0.2823529411764706, 0.2784313725490196, 1.0)
""")


class LoginPage(MDGridLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)


class WinterCakeApp(MDApp):
    def build(self):
        sm =MDScreen()
        sm.add_widget(LoginPage())
        return sm


if __name__ == '__main__':
    WinterCakeApp().run()
