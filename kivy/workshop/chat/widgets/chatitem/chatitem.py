from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import StringProperty
from kivy.lang import Builder
Builder.load_file('./widgets/chatitem/chatitem.kv')


class ChatItem(AnchorLayout, RecycleDataViewBehavior):

    message_text = StringProperty()
    mode = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tmp_height = None
        self.data: dict = None

    def refresh_view_attrs(self, rv, index, data):
        self.data = data
        if(self.data != None):
            self.mode = self.data['mode']
            if(self.data['mode'] == 'sender'):
                self.anchor_x = 'right'
                self.anchor_y = 'center'
            elif(self.data['mode'] == 'receiver'):
                self.anchor_x = 'left'
                self.anchor_y = 'center'
            else:
                self.anchor_y = 'center'
                self.anchor_x = 'center'
        return super().refresh_view_attrs(rv, index, data)

    def on_height(self, instance, value):
        if(self.data != None and (self.tmp_height != None and self.tmp_height != self.height)):
            self.data['height'] = self.tmp_height
            self.height = self.tmp_height

    def on_texture_size(self, instance):
        self.tmp_height = max(50, instance.texture_size[1]+20)
        instance.height = self.tmp_height
        self.on_height(self, self.tmp_height)
