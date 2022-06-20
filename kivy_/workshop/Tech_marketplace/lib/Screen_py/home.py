from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation
from kivymd.uix.tab import MDTabsBase
from pprint import pprint
class HomeScreen(MDScreen):
    def __init__(self, **kw):
        super(HomeScreen, self).__init__(**kw)
    
    def switch_screen(self,*args):
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.2
        self.manager.current = 'categories_screen'
    def slide_dot(self):
        pass
    def slide_widget(self,*args):
        # pprint(sorted(dir(args[0])))
        # print(args[0].to_widget)
        # print(args[0])
        pass
        # print(self.ids.grid.children[int(args[0].scroll_x)])
        # print(args[0].scroll_x)
        # get_child_scroll = {i:v.x for i,v in enumerate(self.ids.grid.children)}
        # print(get_child_scroll)
        # print(args[1].x)
        # for i in args[0].children[0].children:
        #     print(i,'=',i.pos)