from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.properties import *

class ConnexionScreen(MDScreen):
    def tab_switch(self, *args):
        tabs_text = int(args[1].title)
        weigt_dot = list(filter(lambda s: s.rank == tabs_text,
                         self.ids.dot_scroll.children))[0]
        light_dot = list(filter(lambda s: s.rank != tabs_text,
                         self.ids.dot_scroll.children))
        anim_light_dot = Animation(opacity=0.3, duration=0.2)
        for i in light_dot:
            anim_light_dot.start(i)
        anim_weight_dot = Animation(opacity=1, duration=0.1)
        anim_weight_dot.start(weigt_dot)
        if tabs_text == 3:
            self.ids.next_btn.text = 'Skip for now'
        else:
            self.ids.next_btn.text = 'Next'
            self.ids.account_manager.current = 'connect_screen'

    def on_press(self, instance):
        if instance.text == 'Skip for now':
            self.onboard.manager.transition.direction = 'left'
            self.onboard.manager.transition.duration = 0.2
            self.onboard.manager.current = 'category_screen'
        else:
            tabs = self.ids.tabs
            current_title_tab = tabs.get_current_tab().title
            next_tab = list(filter(lambda s : int(s.tab.title)==int(current_title_tab)+1 ,tabs.get_tab_list()))[0]
            tabs.switch_tab(next_tab)
