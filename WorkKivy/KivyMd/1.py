import kivymd
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from pprint import pprint
Builder.load_string("""
<Example@MDScreen>:
    MDBoxLayout:
        pos_hint:{'x':0.5,'y':0.5}
        orientation:'vertical'
        MDTextFieldRound:
            id:text_test
            size_hint_x:None
            width:300
            icon_left: 'key-variant'
            icon_right: 'eye-off'
            hint_text: 'Field with left and right icons'
""")


class Example(MDScreen):
    def __init__(self, **kwargs):
        super(Example, self).__init__(**kwargs)
        pprint(dir(self.ids.text_test))
        self.ids.text_test.bind(on_focus=self.p)
    def p(self,*args):
        print(args)


class App(MDApp):
    def build(self):
        return Example()


if __name__ == '__main__':
    App().run()
