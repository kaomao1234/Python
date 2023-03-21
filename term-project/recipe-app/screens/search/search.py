from kivy.clock import Clock, mainthread
from kivy.uix.recycleview import RecycleView
from kivymd.uix.screen import MDScreen
from kivy.network.urlrequest import UrlRequest
from viewmodels.search_viewmodel import SearchViewModel
import asyncio
from threading import Thread


class SearchScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.viewmodel = SearchViewModel()
        self.search_thread = lambda text, rv: Thread(target=self.on_text(text, rv))

    def on_kv_post(self, base_widget):
        self.ids.search_field.bind(focus=self.on_focus)

    def on_focus(self, value, ins):
        pass

    def on_text(self, text: str, rv: RecycleView):
        Thread(target=lambda *args: setattr(rv, 'data', self.viewmodel.search(text))).start()
        rv.data = [
            {"text": "None"}
        ]

