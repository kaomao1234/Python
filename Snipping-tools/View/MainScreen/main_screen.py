import cv2
import numpy as np
from kivy.graphics import *
from kivy.input import MotionEvent
from kivy.metrics import dp
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.widget import MDWidget
from kivy.core.image import Image, Texture
import Controller
import Model
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import SlideTransition
from kivy.clock import Clock
from View.base_screen import BaseScreenView
from kivy.properties import *
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
from View.MainScreen.components import RectCanvas
from pprint import pprint


class MainScreenView(BaseScreenView):
    menu: MDDropdownMenu
    mode_button: MDDropDownItem = ObjectProperty()
    image_full_screen: Image = ObjectProperty()
    image_rectangle: Image = ObjectProperty()
    screen_mode_switcher: MDScreenManager = ObjectProperty()
    canvas_rect: MDWidget = ObjectProperty()
    number = StringProperty("0")
    items = {
        "Free-form Snip": "free_form_mode", "Rectangle Snip": "rectangle_mode", "Window Snip": "window_mode",
        "Full-screen Snip": "full_screen_mode"
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller: Controller.MainScreenController = self.controller
        self.start_pos = None
        self.end_pos = None
        self.rect = None
        self.image_rect_array = None
        self.mode_selected = None
        self.mode_with_method = {
            "Free-form Snip": self.free_form_shot, "Rectangle Snip": self.rectangle_shot,
            "Window Snip": self.window_shot,
            "Full-screen Snip": self.full_screen_shot
        }

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)

        self.menu = MDDropdownMenu(
            caller=self.mode_button,
            items=[
                {
                    "text": k,
                    "viewclass": "OneLineListItem",
                    "size_hint_y": None, "height": dp(56),
                    "on_release": lambda text=k, s_name=v: self.on_select_item(text, s_name)
                }
                for k, v in self.items.items()
            ], width_mult=4
        )

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_cancel_click(self):
        self.canvas_rect.canvas.clear()
        self.image_rectangle.texture = None
        self.image_full_screen.texture = None

    def on_new_click(self):
        if self.mode_selected is not None:
            self.mode_with_method[self.mode_selected]()
        else:
            Snackbar(text="Please select mode first.").open()

    def on_select_item(self, text, s_name):
        self.mode_button.set_item(text)
        current_screen_index = self.screen_mode_switcher.screen_names.index(self.screen_mode_switcher.current)

        # Determine the direction based on the screen index
        if self.screen_mode_switcher.screen_names.index(s_name) > current_screen_index:
            direction = 'left'
        else:
            direction = 'right'
        self.mode_selected = text
        # Set the transition direction and switch screens
        self.screen_mode_switcher.transition = SlideTransition(direction=direction)
        self.screen_mode_switcher.current = s_name
        self.menu.dismiss()

    def on_rect_touch_down(self, instance, touch):
        if touch.button == 'left' and self.image_rectangle.texture:
            self.canvas_rect.canvas.clear()
            self.start_pos = touch.pos
            self.end_pos = touch.pos
            with instance.canvas:
                Color(1, 0, 0, 1)
                self.rect = Line(rectangle=(self.start_pos[0], self.start_pos[1], 0, 0))

    def on_rect_touch_move(self, instance, touch):
        if self.rect and touch.button == 'left' and self.image_rectangle.texture:
            self.end_pos = touch.pos
            self.rect.rectangle = (self.start_pos[0], self.start_pos[1],
                                   self.end_pos[0] - self.start_pos[0], self.end_pos[1] - self.start_pos[1])

    def on_rect_touch_up(self, instance, touch):
        if self.rect and touch.button == 'left' and self.image_rectangle.texture:
            x = abs(self.start_pos[0])
            y = abs(self.start_pos[1])
            width = abs(self.end_pos[0] - self.start_pos[0])
            height = (self.end_pos[1] - self.start_pos[1])
            rectangle = (x, y, width, height)
            self.rect.rectangle = rectangle
            regioned = self.image_rectangle.texture.get_region(*rectangle)
            pprint(dir(regioned))
            print(regioned.pixels)
            # cv2.imshow("cropped", cropped_image)
            # self.image_rectangle.texture = texture
            # self.image_rectangle.fit_mode = "contain"
            self.rect = None
            self.start_pos = None
            self.end_pos = None

    def full_screen_shot(self):
        Window.minimize()
        def texturing(dt):
            array_image, buffer = self.controller.full_screen_capture()
            texture = Texture.create(size=(array_image.shape[1], array_image.shape[0]), colorfmt="rgb")
            texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")
            self.image_full_screen.texture = texture
            Window.restore()

        Clock.schedule_once(texturing, 1)

    def rectangle_shot(self):
        Window.minimize()
        self.canvas_rect.canvas.clear()
        self.image_rectangle.fit_mode = "fill"

        def texturing(dt):
            array_image, buffer = self.controller.full_screen_capture()
            self.image_rect_array = array_image
            texture = Texture.create(size=(array_image.shape[1], array_image.shape[0]), colorfmt="bgr")
            texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")
            self.image_rectangle.texture = texture
            Window.restore()

        Clock.schedule_once(texturing, 1)

    def free_form_shot(self):
        pass

    def window_shot(self):
        pass
