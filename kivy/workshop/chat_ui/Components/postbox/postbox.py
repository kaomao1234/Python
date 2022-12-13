from kivy.metrics import dp
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivy.types import *
from kivy.properties import *
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior


class PostBox(BoxLayout, RecycleDataViewBehavior, RoundedRectangularElevationBehavior):
    score = NumericProperty(0)
    heart_plus_icon = StringProperty()
    heart_remove_icon = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._rv = None
        self.index = None
        self._lastest_data = None
        self.tmpScore = self.score
        self.tempHeight = None

    def refresh_view_attrs(self, rv, index, data):
        self._rv = rv
        self.index= index
        self._lastest_data = data
        # self.update()
        super().refresh_view_attrs(rv, index, data)
    
    def callTexture(self, instance):
        self.tempHeight = max(100, instance.texture_size[1]+20)
        instance.height = self.tempHeight
        self.on_height(self, self.height)
    
    def on_kv_post(self, base_widget):
        for i in self.ids:
            setattr(self, i, self.ids[i])
        return super().on_kv_post(base_widget)

    def on_height(self, instance, value):
        data = self._lastest_data
        if(data != None and (self.tempHeight != None and self.tempHeight != self.height)):
            data['height'] = self.tempHeight
            self.height = self.tempHeight
    
    def update(self):
        if self._rv != None:
            i = self._lastest_data
            i['score'] = self.score
            i['heart_plus_icon'] = self.heart_plus_icon
            i['heart_remove_icon'] = self.heart_remove_icon
            i['text'] = self.text

    def onHeartRemovePress(self, *e):
        if self.heart_remove_icon == self.heart_remove.iconList[0]:
            self.heart_remove_icon = self.heart_remove.iconList[1]
            self.heart_plus_icon = self.heart_plus.iconList[0]
            self.score = self.tmpScore - 1
        else:
            self.score = self.tmpScore
            self.heart_remove_icon = self.heart_remove.iconList[0]

    def onHeartPlusPress(self, *e):
        if self.heart_plus_icon == self.heart_plus.iconList[0]:
            self.heart_plus_icon = self.heart_plus.iconList[1]
            self.heart_remove_icon = self.heart_remove.iconList[0]
            self.score = self.tmpScore + 1
        else:
            self.score = self.tmpScore
            self.heart_plus_icon = self.heart_plus.iconList[0]

