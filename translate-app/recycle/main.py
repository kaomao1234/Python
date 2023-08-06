from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDRaisedButton:
        text: "Clear Canvas"
        on_release: app.clear_canvas()

    MyCanvas:
        id: canvas
'''

class MyCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_pos = None
        self.rect_outline = None

    def on_touch_down(self, touch):
        print(touch)
        if self.collide_point(*touch.pos):
            self.start_pos = touch.pos

    def on_touch_move(self, touch):
        if self.start_pos:
            width = touch.pos[0] - self.start_pos[0]
            height = touch.pos[1] - self.start_pos[1]
            self.clear_canvas()
            with self.canvas:
                Color(1, 0, 0, 1)  # Red color
                self.rect_outline = Line(rectangle=(self.start_pos[0], self.start_pos[1], width, height), width=1.5)

    def on_touch_up(self, touch):
        self.start_pos = None

    def clear_canvas(self):
        self.canvas.clear()

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def clear_canvas(self):
        canvas = self.root.ids.canvas
        canvas.clear_canvas()

if __name__ == '__main__':
    MyApp().run()
