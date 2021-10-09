from os import system
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from pprint import pprint
from kivy.uix.label import Label
Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
<M@BoxLayout>:
    orientation:'vertical'
    spacing: '10dp'
    AnchorLayout:
        anchor_y: 'center'
        GridLayout:
            size_hint: None,None 
            cols:2
            size:300,10
            MDTextField:
                size_hint_y: None
                id:t_widget
                text:"Hello world"
                password:True
            MDIconButton:
                size_hint_y: None
                id:hide
                icon:"eye"
                ripple_scale:0
""")
class M(BoxLayout):
    def __init__(self, **kwargs):
        super(M, self).__init__(**kwargs)
        pprint(dir(self.ids.hide))
        # print(self.ids.Field_btn.focus)
        self.ids.hide.bind(state=self.on_press)
    
    
    def on_press(self, *e):
        focus = e[1]
        instance = e[0]
        if focus == "normal":
            instance.icon = "eye"
            self.ids.t_widget.password = True
        else:
            instance.icon = "eye-off"
            self.ids.t_widget.password = False

class Sene(Screen):
    def __init__(self, **kw):
        super(Sene, self).__init__(**kw)
        self.add_widget(M())
class MYApp(MDApp):
    def build(self):
        return M()


def main():
    MYApp().run()


if __name__ == '__main__':
    system('cls')
    main()
