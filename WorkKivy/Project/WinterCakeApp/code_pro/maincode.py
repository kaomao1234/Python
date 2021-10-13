import kivy
import kivymd
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import SwapTransition
from kivymd.uix.button import MDRoundFlatIconButton
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from functools import partial
from pprint import pprint
from kivy.uix.button import Button
from kivy.properties import ColorProperty
from kivy.core.window import Window
from kivymd.uix.transition import MDFadeSlideTransition
lst_file = ["onboarding.kv", 'sign_in.kv', 'sign_up.kv', 'shopping.kv']
for i in lst_file:
    Builder.load_file("{}".format(i))


class MainScreen(ScreenManager):
    black = 0, 0, 0, 1
    copper_rust = get_color_from_hex("#9b4f4f")
    white = get_color_from_hex("#ffffff")
    weathered_stone = get_color_from_hex("#c4c4c4")

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.add_layout_with_id()
        Clock.schedule_once(self.start, 4)
        self.transition = MDFadeSlideTransition()

    def add_layout_with_id(self):
        sign_in = Sign_in
        sign_up = Sign_up
        shopping = ShopScreen
        self.ids[sign_in.id] = sign_in(self)
        self.ids[sign_up.id] = sign_up(self)
        self.ids[shopping.id] = shopping(self)
        self.ids.s_drop_manager.add_widget(self.ids[sign_in.id])
        self.ids.s_drop_manager.add_widget(self.ids[sign_up.id])
        self.add_widget(self.ids[shopping.id])

    def start(self, *e):
        p = Animation(y=0, duration=0.2)
        m = Animation(size_hint_y=0.5, duration=0.2)
        p.start(self.ids.backdrop_widget)
        m.start(self.ids.bg_img)


class Sign_in(MDScreen):
    id = 'sign_in'

    def __init__(self, root, **kwargs):
        super(Sign_in, self).__init__(**kwargs)
        self.ids.eye_pass.bind(state=partial(
            self.switch_event, self.ids.password_field))
        self.root = root
        self.back_arrow = MDRoundFlatIconButton(
            icon='arrow-expand-left',
            size_hint=(.1, .1),
            pos_hint={'x': 0, 'y': .9},
            text='back',
            theme_text_color="Custom",
            line_color=self.copper_rust,
            icon_color=self.white,
            text_color=self.white,
        )

    def switch_event(self, text_event, *e):
        focus = e[1]
        instance = e[0]
        if focus == "down":
            instance.icon = "eye"
            text_event.password = False
        else:
            instance.icon = "eye-off"
            text_event.password = True

    def next_sign_up(self):
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.5
        self.manager.current = 'sign_up'
        anim = Animation(size_hint_y=0.7, duration=0.2)
        anim.start(self.root.ids.backdrop_widget)
        self.back_arrow.on_press = self.root.ids.sign_up.back_to_sign_in
        self.root.ids.on_board.add_widget(self.back_arrow)
        self.root.ids.sign_up.back_arrow = self.back_arrow

    def next_shop_page(self):
        self.root.transition.duration = 0.2
        self.root.current = 'shop_screen'


class Sign_up(MDScreen):
    id = 'sign_up'

    def __init__(self, root, **kwargs):
        super(Sign_up, self).__init__(**kwargs)
        self.back_arrow = ''
        self.root = root
        self.ids.eye_pass.bind(state=partial(
            self.switch_event, self.ids.password_field))
        self.ids.eye_confirm_pass.bind(state=partial(
            self.switch_event, self.ids.confirm_password_field))

    def back_to_sign_in(self, *e):
        self.manager.transition.direction = 'right'
        self.manager.transition.duration = 0.2
        self.manager.current = 'sign_in'
        anim = Animation(size_hint_y=0.5, duration=0.2)
        anim.start(self.root.ids.backdrop_widget)
        self.root.ids.on_board.remove_widget(self.back_arrow)

    def switch_event(self, text_event, *e):
        focus = e[1]
        instance = e[0]
        if focus == "down":
            instance.icon = "eye"
            text_event.password = False
        else:
            instance.icon = "eye-off"
            text_event.password = True


class ShopScreen(MDScreen):
    id = 'shopping'
    
    def __init__(self, root, **kwargs):
        super(ShopScreen, self).__init__(**kwargs)
        self.root = root
        self._keyboard = Window.request_keyboard(None,self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        for i in range(1,21):
            self.ids.shop_view.add_widget(Button(text=f"Product {i}"))

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode[1])
        if keycode[1] == 'c':
            self.root.transition.duration = 0.2
            self.root.current = 'on_board_screen'


class WinterCake(MDApp):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    WinterCake().run()
