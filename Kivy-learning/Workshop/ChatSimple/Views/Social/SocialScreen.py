from kivymd.uix.screen import MDScreen
from kivymd.utils import asynckivy
from Components.postbox.postbox import PostBox
from Components.postboxManager.postboxManager import PostboxManager
from kivymd.utils import asynckivy
from kivy.clock import Clock


class SocialScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.postCell = [PostboxManager(text=i) for i in range(0, 11)]

    def on_kv_post(self, base_widget):
        self.ids.rv.data = [{
            'postText': str(i),
            'heart_plus_icon': self.postCell[i].heart_plus,
            'heart_remove_icon': self.postCell[i].heart_remove,
            'height':100,
            'score': 0,
        } for i in range(0, 10)]
        return super().on_kv_post(base_widget)

    def setListWidget(self):
        async def setting():
            self.disabled = True
            for i in range(0, 10):
                # await asynckivy.sleep(1)
                self.ids.listBox.add_widget(PostBox(text=f"Hello{i}"))
            self.disabled = False
        asynckivy.start(setting())
