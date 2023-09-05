from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.properties import ListProperty


class DrawRectangleWidget(Widget):
    rectangles = ListProperty([])

    def __init__(self, callback=None, **kwargs):
        super(DrawRectangleWidget, self).__init__(**kwargs)
        self.start_pos = None
        self.end_pos = None
        self.rect = None
        self.callback = callback

    def on_touch_down(self, touch):
        if touch.button == 'left':
            self.start_pos = touch.pos
            self.end_pos = touch.pos
            with self.canvas:
                Color(1, 0, 0, 1)
                self.rect = Line(rectangle=(self.start_pos[0], self.start_pos[1], 0, 0))

    def on_touch_move(self, touch):
        if self.rect and touch.button == 'left':
            self.end_pos = touch.pos
            self.rect.rectangle = (self.start_pos[0], self.start_pos[1],
                                   self.end_pos[0] - self.start_pos[0], self.end_pos[1] - self.start_pos[1])

    def on_touch_up(self, touch):
        if self.rect and touch.button == 'left':
            self.rect.rectangle = (self.start_pos[0], self.start_pos[1],
                                   self.end_pos[0] - self.start_pos[0], self.end_pos[1] - self.start_pos[1])
            self.rectangles.append((self.start_pos[0], self.start_pos[1],
                                    self.end_pos[0] - self.start_pos[0], self.end_pos[1] - self.start_pos[1]))
            if self.callback:
                self.callback(self.rectangles[-1], self.rectangles)  # Pass all drawn rectangles

            self.rect = None
            self.start_pos = None
            self.end_pos = None


class RectangleDrawerApp(App):
    def build(self):
        root = Widget()

        def rectangle_callback(last_rectangle, rectangles):
            print("Last rectangle := ", last_rectangle)
            print("All rectangles :=", rectangles)

        self.draw_widget = DrawRectangleWidget(callback=rectangle_callback)
        root.add_widget(self.draw_widget)
        return root


if __name__ == '__main__':
    RectangleDrawerApp().run()
