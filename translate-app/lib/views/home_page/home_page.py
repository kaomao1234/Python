from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.graphics import Color, Line
from kivy.input.motionevent import MotionEvent
from kivy.core.window import Window
from kivy.clock import Clock
# from lib.utils.capturingScreenshot import capturing_screenshot
# from ... import utils


class HomePage(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.widget_canvas: MDWidget
        self.mode_button: MDDropDownItem
        self.start_pos = None
        self.rect = None
        self.ss_region = []
        self.menu: MDDropdownMenu

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)
        self.widget_canvas = self.ids.widget_canvas
        self.mode_button = self.ids.mode_button
        items = [
            "Free-form Snip", "Rectangle Snip", "Window Snip", "Full-screen Snip"
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.mode_button,
            items=[
                {
                    "text": item,
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=items[index]: self.on_select_item(x),
                    "height": dp(56)
                }
                for index, item in enumerate(items)
            ],
            width_mult=4
        )

    def on_capture(self):
        self.minimize_app()
        Clock.schedule_once(lambda: utils.capturing_screenshot(*self.ss_region), 3)

    def minimize_app(self):
        Window.minimize()

    def on_select_item(self, text_item: str):
        self.mode_button: MDDropDownItem = self.ids.mode_button
        self.mode_button.set_item(text_item)
        self.menu.dismiss()

    def canvas_on_touch_down(self, instance: MDWidget, touch: MotionEvent):
        if instance.collide_point(*touch.pos):
            self.start_pos = touch.pos
            self.rect = Line(rectangle=(self.start_pos[0], self.start_pos[1], 0, 0), width=1)
            instance.canvas.add(self.rect)
            with instance.canvas:
                Color(1, 0, 0, 1)  # Red color

    def canvas_on_touch_move(self, instance: MDWidget, touch: MotionEvent):
        if self.start_pos and self.rect:
            width = touch.pos[0] - self.start_pos[0]
            height = touch.pos[1] - self.start_pos[1]
            self.rect.rectangle = (self.start_pos[0], self.start_pos[1], width, height)
            self.ss_region = [*self.start_pos, width, height]

    def canvas_on_touch_up(self, instance: MDWidget, touch: MotionEvent):
        self.start_pos = None
        self.rect = None

    def on_press(self):
        print("Hello world")

    def draw_outline_box(self):
        with self.widget_canvas.canvas:
            Color(1, 0, 0, 1)
            Line(rectangle=(100, 100, 200, 200), width=2)
