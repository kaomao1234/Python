from kivy.app import App
from kivy.core import text
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

# long_text = "".join(
#     ["this is a long line "+str(n)+"\n" for n in range(1, 101)])




class ScrollableLabel(ScrollView):
    # text = StringProperty('')

    def __init__(self, **kwargs):
        super(ScrollableLabel, self).__init__(**kwargs)
        self.label = Label(size_hint_y=None, text="".join(
            ["this is a long line "+str(n)+"\n" for n in range(1, 101)]))
        self.add_widget(self.label)
        Clock.schedule_once(self.update, -1)

    def update(self, *args):
        self.label.text_size = (self.label.width, None)
        self.label.height = self.label.texture_size[1]



class ScrollApp(App):
    def build(self):
        return ScrollableLabel()


if __name__ == "__main__":
    ScrollApp().run()
# import kivy
# from kivy.app import App
# kivy.require('1.9.0')
# from kivy.uix.label import Label
# from kivy.uix.scrollview import ScrollView
# from kivy.properties import StringProperty
# from kivy.base import runTouchApp
# from kivy.lang import Builder

# Builder.load_string('''

# # Define the scroll view
# <ScrollableLabel>:
#     text: 'You are learning Kivy' * 500
#     Label:
#         text: root.text
#         font_size: 50
#         text_size: self.width, None
#         size_hint_y: None
#         height: self.texture_size[1]
# ''')
# class ScrollableLabel(ScrollView):
#     text = StringProperty('')
# runTouchApp(ScrollableLabel())
