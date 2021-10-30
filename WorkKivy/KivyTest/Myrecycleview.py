from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from functools import *
Builder.load_string("""
<Myview>:
    viewclass : 'Button'
    orientation:'vertical'
    spacing: 40
    padding:10, 10
    space_x: self.size[0]/3
    RecycleBoxLayout:
        color:(0, 0.7, 0.4, 0.8)
        default_size: None, dp(56)
  
        # defines the size of the widget in reference to width and height
        default_size_hint: 0.4, None 
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical' # defines the orientation of data items
""")

class Myview(RecycleView):
    def __init__(self, **kwargs):
        super(Myview, self).__init__(**kwargs)
        self.data = self.data = [
            {'text': str(x), 'on_press': partial(self.show_press, x)} for x in range(20)]

    def show_press(self, x):
        print(x)


class MyApp(App):
    def build(self):
        return Myview()


MyApp().run()
