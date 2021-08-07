import sys
from clientKv import Frontend
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import ScrollView
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.textinput import TextInput
import kivy
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')
Builder.load_string("""
<ScrollableLabel>:
    chat:chat
    Label:
        id:chat
        text: root.text
        font_size:30
        text_size:self.width,None
        size_hint_y: None
        height: self.texture_size[1]
        markup:True
        background_color:'green'
<ScreenUI>:
    rows: 2
    getChat:scrollChat.chat
    ScrollableLabel:
        id:scrollChat
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        size:(0,150)
        TextInput:
            id:text
            multiline:True
            size_hint_y: None
            size:(100,100)
            font_size: 50
        Button:
            text: 'submit'
            size_hint_y: None
            size_hint_x: None
            on_press:root.submitText(text,scrollChat.chat)
    
""")


class ScrollableLabel(ScrollView):
    text = StringProperty()


class ScreenUI(GridLayout):
    def __init__(self):
        super(ScreenUI, self).__init__()
        self.client = Frontend(self.getChat)
        self.client.start()
        Window.bind(on_request_close=lambda s: sys.exit())

    def submitText(self, event, chat):
        if event.text != '':
            self.client.send(event.text)
            chat.text = chat.text+event.text+'\n'
            event.text = ''


class MyApp(App):
    def build(self):
        return ScreenUI()


if __name__ == '__main__':
    MyApp().run()
