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
        MDBoxLayout:
            orientation:'vertical'
            size_hint_y: None
            AnchorLayout:
                anchor_x:'center'
                size_hint_y: None
                height:23
                MDIconButton:
                    size_hint_y: None
                    icon:'store-plus'
                    user_font_size:"20dp"
                    theme_text_color: "Custom"
                # text_color:root.copper_rust
            Label:
                size_hint_y: None
                height:15
                text:'halo'
                # font_name:root.sukhumvit_font
                markup:True
                font_size:14
                # halign:'center'
                color:0,0,0,1
                # color:root.copper_rust
                # text_size:self.size
        # MDBoxLayout:
        #     id:parent
        #     size_hint: None,None 
        #     # size_hint_y: None
        #     cols:2
        #     size:300,40
        #     padding:[18,0]
        #     radius:[18,18]
        #     orientation:'horizontal'
        #     line_color:get_color_from_hex("#9b4f4f")
        #     MDTextField:
        #         size_hint_y:None
        #         -height:50
        #         # line_anim:False
        #         id:t_widget
        #         text:"hello world"
        #         # password:True
        #         text_color:0,0,0,1
        #         line_color_focus: 0,0,0,1
        #     MDIconButton:
        #         size_hint_y: None
        #         size_hint_x:None
        #         id:hide
        #         icon:"magnify"
        #         user_font_size:"18dp"
        #         theme_text_color: "Custom"
        #         # text_color:get_color_from_hex("#9b4f4f")
        #         ripple_scale:0
        #         ripple_alpha:0
        #         ripple_rad_default:0
""")
class M(BoxLayout):
    def __init__(self, **kwargs):
        super(M, self).__init__(**kwargs)
        # pprint(dir(self.ids.hide))
        # print(self.ids.Field_btn.focus)
        # self.ids.hide.bind(state=self.on_press)
        # pprint(dir(self.ids.t_widget))
    
    
    # def on_press(self, *e):
    #     focus = e[1]
    #     instance = e[0]
    #     print(instance.ripple_duration_in_fast)
    #     print(instance.ripple_duration_in_slow)
    #     print(instance.ripple_duration_out)
    #     print(instance.ripple_func_in)
    #     print(instance.ripple_func_out)
    #     print(instance.ripple_rad_default)
    #     if focus == "normal":
    #         instance.icon = "eye"
    #         self.ids.t_widget.password = True
    #     else:
    #         instance.icon = "eye-off"
    #         self.ids.t_widget.password = False

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
