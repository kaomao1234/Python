import kivymd
import kivy
from functools import partial
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation
path = "C:/Users/borip/Documents/GitHub/PythonWorkShop/WorkKivy/Project/WinterCakeApp/Page/"
lst_file = ["Sign_in.kv","Sign_up.kv"]
for i in lst_file:
    Builder.load_file("{}{}".format(path, i))


class MainScreen(MDFloatLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.start, 4)
        # print(self.ids)
        self.ids.eye_pass.bind(state=partial(self.on_press,self.ids.password_field))
        self.ids.change_screen.add_widget(Sign_up())

    def on_press(self,text_event,*e):
        focus = e[1]
        instance = e[0]
        if focus == "down":
            instance.icon = "eye"
            text_event.password = False
        else:
            instance.icon = "eye-off"
            text_event.password = True

    def start(self, *e):
        p = Animation(y=0, duration=0.2)
        m = Animation(size_hint_y=0.5,duration=0.2)
        p.start(self.ids.backdrop)
        m.start(self.ids.bg_img)

class Sign_up(MDScreen):
    def __init__(self, **kwargs):
        super(Sign_up, self).__init__(**kwargs)
class WinterCake(MDApp):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    WinterCake().run()