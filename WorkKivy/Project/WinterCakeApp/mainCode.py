import kivy
import kivymd
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from pprint import pprint
from functools import partial
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDRoundFlatIconButton
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.utils import get_color_from_hex



lst_file = ["onboarding.kv", 'sign_in.kv', 'sign_up.kv']
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

    def add_layout_with_id(self):
        sign_in = Sign_in
        sign_up = Sign_up
        self.ids[sign_in.id] = sign_in(self)
        self.ids[sign_up.id] = sign_up(self)
        self.ids.s_drop_manager.add_widget(self.ids[sign_in.id])
        self.ids.s_drop_manager.add_widget(self.ids[sign_up.id])

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
            text='back',
            size_hint=(.1, .1),
            pos_hint={'x': 0, 'y': .9},
            text_color= self.root.white,
            theme_text_color= "Custom",
            line_color=self.root.copper_rust,
            icon_color=self.root.white
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

    def next_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.5
        self.manager.current = 'sign_up'
        anim = Animation(size_hint_y=0.7, duration=0.2)
        anim.start(self.root.ids.backdrop_widget)
        self.back_arrow.on_press = self.root.ids.sign_up.back_screen
        self.root.ids.on_board.add_widget(self.back_arrow)
        self.root.ids.sign_up.back_arrow = self.back_arrow


class Sign_up(MDScreen):
    id = 'sign_up'

    def __init__(self, root, **kwargs):
        super(Sign_up, self).__init__(**kwargs)
        self.back_arrow = ''
        self.root = root
        self.ids.eye_pass.bind(state=partial(self.switch_event,self.ids.password_field))
        self.ids.eye_confirm_pass.bind(state=partial(self.switch_event,self.ids.confirm_password_field))
        
    def back_screen(self, *e):
        self.manager.transition.direction = 'right'
        self.manager.transition.duration = 0.5
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

class WinterCake(MDApp):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    WinterCake().run()