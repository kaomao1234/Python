from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
import random

Builder.load_string('''
<Row@Label>:
    canvas.before:
        Color:
            rgba: 0.8, 0.1, 0.1, 0.5 #Red Marker
        Rectangle:
            size: self.size
            pos: self.pos
    text_size: self.width, None
    size_hint_y: None
    height: self.texture_size[1]
    font_size: dp(18)
    markup: True
    on_size: 
        self.texture_update()
        self.height = self.texture_size[1]

<RV>:
    viewclass: 'Row'
    scroll_type: ['bars', 'content']
    scroll_wheel_distance: dp(114)
    bar_width: dp(10)
    RecycleBoxLayout:
        default_size: None, dp(20)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        spacing: dp(3)

''')


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        line = ''
        for i in range(200):

            n = random.randint(0, 1)
            if n:
                j = random.randint(5, 30)
                line = '[color=#ffff00]Line: ' + str(i + 1) + '[/color] This is a test of a bunch of text' * j
            else:
                line = '[color=#ffff00]Line: ' + str(i + 1) + '[/color] This is a test of a bunch of text'
            self.data.append({'text': line})


class TestApp(App):
    def build(self):
        return RV()


if __name__ == '__main__':
    TestApp().run()