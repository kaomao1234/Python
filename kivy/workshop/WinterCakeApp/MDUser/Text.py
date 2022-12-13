from os import system
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
from pprint import pprint
from kivy.uix.label import Label
from kivymd.uix.button import MDIconButton
from kivymd.icon_definitions import md_icons
from pprint import pprint
from functools import partial
Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
#: import md_icons kivymd.icon_definitions.md_icons
<MakeIconButton@ButtonBehavior+FocusBehavior+MDIcon>:
<M@MDBoxLayout>:
    orientation:'vertical'
    padding:[50,0]
    MDRoundFlatIconButton:
        icon: "android"
        text: "MDROUNDFLATICONBUTTON"
    MDTextFieldRound:
        hint_text: 'Empty field'
    MDBoxLayout:
        orientation:'horizontal'
        padding:[3,3]
        md_bg_color:(0.7686274509803922, 0.7686274509803922, 0.7686274509803922, 1.0)
        size_hint_y: None
        radius:[20,20]
        height:40
        MDBoxLayout:
            id:text_con
            md_bg_color:(0.7686274509803922, 0.7686274509803922, 0.7686274509803922, 1.0)
            radius:[20,20]
            TextInput:
                id:text_test
                background_color:0,0,0,0
                on_focus:root.anim_fucn(self)
        MakeIconButton:
            id:make
            icon:'eye'
            size_hint_x: None
            width:40
            halign: "center"
            
""")
class M(MDBoxLayout):
    def __init__(self, **kwargs):
        super(M, self).__init__(**kwargs)
        self.ids.make.bind(state=partial(self.switch_event,self.ids.text_test))
    def anim_fucn(self,instance):
        A = None
        if instance.focus:
            A = Animation(md_bg_color=[1,1,1,1],duration=0.1)
        else:
            A = Animation(md_bg_color=[0.7686274509803922, 0.7686274509803922, 0.7686274509803922, 1.0],duration=0.1)
        
        A.start(self.ids.text_con)
    
    def switch_event(self, text_event,*e):
        focus = e[1]
        instance = e[0]
        text_event.focus= True
        print(text_event.text)
        if focus == "down":
            instance.icon = "eye"
            text_event.password = False
        else:
            instance.icon = "eye-off"
            text_event.password = True

class MYApp(MDApp):
    def build(self):
        self.title = 'MyApp'
        return M()


def main():
    MYApp().run()


if __name__ == '__main__':
    system('cls')
    main()
