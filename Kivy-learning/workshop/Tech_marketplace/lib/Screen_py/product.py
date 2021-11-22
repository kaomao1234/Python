from kivymd.uix.screen import MDScreen
from kivy.properties import *
from firebase import firebase


class ProductScreen(MDScreen):
    title = StringProperty('')

    def __init__(self, **kwargs):
        super(ProductScreen, self).__init__(**kwargs)
        fb = firebase.FirebaseApplication('https://botkaomao-default-rtdb.firebaseio.com')
        self.results = fb.get('recycle_viewData',None)

    def on_start(self):
        self.ids._lst.data = [value for (key,value) in self.results.items()]
        self.ids._lst.refresh_from_data()
