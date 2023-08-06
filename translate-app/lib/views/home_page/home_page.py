from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget
from kivy.graphics import Color, Line
from kivy.input.motionevent import  MotionEvent
class HomePage(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.widget_canvas: MDWidget
        self.start_pos = None
        self.rect = None

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)
        self.widget_canvas = self.ids.widget_canvas

    def canvas_on_touch_down(self, instance: MDWidget, touch:MotionEvent):
        if instance.collide_point(*touch.pos):
            self.start_pos = touch.pos
            self.rect = Line(rectangle=(self.start_pos[0], self.start_pos[1], 0, 0), width=1)
            instance.canvas.add(self.rect)
            with instance.canvas:
                Color(1, 0, 0, 1)  # Red color

    def canvas_on_touch_move(self, instance: MDWidget, touch:MotionEvent):
        if self.start_pos and self.rect:
            width = touch.pos[0] - self.start_pos[0]
            height = touch.pos[1] - self.start_pos[1]
            self.rect.rectangle = (self.start_pos[0], self.start_pos[1], width, height)

    def canvas_on_touch_up(self, instance: MDWidget, touch:MotionEvent):
        self.start_pos = None
        self.rect = None

    def on_press(self):
        print("Hello world")

    def draw_outline_box(self):
        with self.widget_canvas.canvas:
            Color(1, 0, 0, 1)
            Line(rectangle=(100, 100, 200, 200), width=2)
