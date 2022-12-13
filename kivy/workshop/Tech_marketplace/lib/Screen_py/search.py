from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from functools import partial
class SearchScreen(MDScreen):
    def __init__(self,**kw):
        super(SearchScreen, self).__init__(**kw)
    def append_data(self):
        self.ids._lst.data = [{'text':'Iphone 11 Pro','second_text':'USD499','img_source':'assets/images/Product.png','when_click':self.clicked}]
        # self.ids._lst.refresh_from_data()
    def clicked(self,*args):
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.2
        self.manager.current = 'detail_page'
        detail_page  = self.manager.children[0]
        detail_page.title = args[0].text
        # print(args)
    def on_change_screen(self,*e):
        sm:ScreenManager = self.ids.sm
        sm.transition.duration = 0.1
        if e[1] != '':
            sm.current = 'screen_2'
        else:
            sm.current = 'screen_1'