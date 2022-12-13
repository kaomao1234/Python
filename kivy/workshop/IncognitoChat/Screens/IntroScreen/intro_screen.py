from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.clock import Clock


class IntroScreen(MDScreen):
    def __init__(self, **kw):
        super(IntroScreen, self).__init__(**kw)
        Clock.schedule_once(self.animate_widget, 1)

    def animate_widget(self, *e):
        anim_bg = Animation(pos_hint={'center_y': abs(
            self.ids.bg.pos_hint['center_y'])}, duration=0.2)
        anim_title = Animation(pos_hint={'center_y': abs(
            self.ids.title.pos_hint['center_y'])}, duration=0.5)
        anim_start_btn = Animation(pos_hint={'center_y': abs(
            self.ids.start_btn.pos_hint['center_y'])}, duration=0.7)
        anim_bg.start(self.ids.bg)
        anim_title.start(self.ids.title)
        anim_start_btn.start(self.ids.start_btn)

    def on_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.5
        self.manager.current = 'login_screen'
