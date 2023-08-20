from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.properties import *


class RectCanvas(Widget):
    rectangles = ListProperty([])
    rectangles_callback = ObjectProperty(None)
    enable_draw = BooleanProperty(True)
    def __init__(self, **kwargs):
        super(RectCanvas, self).__init__(**kwargs)
        self.start_pos = None
        self.end_pos = None
        self.rect = None

    def on_touch_down(self, touch):
        if touch.button == 'left' and self.enable_draw:
            self.start_pos = touch.pos
            self.end_pos = touch.pos
            with self.canvas:
                Color(1, 0, 0, 1)
                self.rect = Line(rectangle=(self.start_pos[0], self.start_pos[1], 0, 0))

    def on_touch_move(self, touch):
        if self.rect and touch.button == 'left' and self.enable_draw:
            self.end_pos = touch.pos
            self.rect.rectangle = (self.start_pos[0], self.start_pos[1],
                                   self.end_pos[0] - self.start_pos[0], self.end_pos[1] - self.start_pos[1])

    def on_touch_up(self, touch):
        if self.rect and touch.button == 'left' and self.enable_draw:
            self.rect.rectangle = (self.start_pos[0], self.start_pos[1],
                                   self.end_pos[0] - self.start_pos[0], self.end_pos[1] - self.start_pos[1])
            self.rectangles.append((self.start_pos[0], self.start_pos[1],
                                    self.end_pos[0] - self.start_pos[0], self.end_pos[1] - self.start_pos[1]))
            if self.rectangles_callback:
                self.rectangles_callback(self.rectangles[-1], self.rectangles)  # Pass all drawn rectangles

            self.rect = None
            self.start_pos = None
            self.end_pos = None
