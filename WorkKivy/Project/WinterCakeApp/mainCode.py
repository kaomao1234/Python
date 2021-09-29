import kivymd
import kivy
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation
path = "C:/Users/borip/Documents/GitHub/PythonWorkShop/WorkKivy/Project/WinterCakeApp/Page/"
lst_file = ["Sign_in.kv"]
for i in lst_file:
    Builder.load_file("{}{}".format(path, i))


class SignIn(MDScreen):
    def __init__(self, **kwargs):
        super(SignIn, self).__init__(**kwargs)
        Clock.schedule_once(self.start, 4)
        self.ids.hide.bind(state=self.on_press)

    def on_press(self, *e):
        focus = e[1]
        instance = e[0]
        if focus == "down":
            instance.icon = "eye"
            self.ids.t_widget.password = False
        else:
            instance.icon = "eye-off"
            self.ids.t_widget.password = True

    def start(self, *e):
        p = Animation(y=0, duration=0.2)
        m = Animation(size_hint_y=0.6, duration=0.2)
        p.start(self.ids.sign_in_frame)
        m.start(self.ids.bg_img)


class WinterCake(MDApp):
    def build(self):
        return SignIn()


if __name__ == '__main__':
    WinterCake().run()
