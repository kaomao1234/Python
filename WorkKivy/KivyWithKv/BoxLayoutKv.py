import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
Builder.load_string("""
<KVBL>:
    orientation:'vertical'
    Button:
        text:'Btn-1'
        background_color: 0, 1, 1, 1 
        font_size:30
        on_press:root.on_click(self)
    Button:
        text:'Btn-2'
        background_color: 0, 1, 1, 1 
        font_size:30
        on_press:root.on_click(self)
    Button:
        text:'Btn-3'
        background_color: 0, 1, 1, 1 
        font_size:30
        on_press:root.on_click(self)""")


class KVBL(BoxLayout):
    def __init__(self):
        super(KVBL, self).__init__()

    def on_click(self, event):
        event.text = event.text.replace("Btn-", '')
        print(event.text)


class MyApp(App):
    def build(self):
        return KVBL()


if __name__ == '__main__':
    MyApp().run()
