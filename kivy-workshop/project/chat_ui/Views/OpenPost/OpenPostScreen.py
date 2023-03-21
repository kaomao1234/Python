from kivymd.uix.screen import MDScreen
from kivy.properties import *
from kivy.core.window import Window
from Components.commentBox.commentBox import CommentBox


class OpenPostScreen(MDScreen):
    text = StringProperty()
    score = NumericProperty(0)

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_kv_post(self, base_widget):
        for i in self.ids:
            setattr(self, i, self.ids[i])
        for j in range(0, 20):
            self.comment_lst.add_widget(CommentBox(text="Hello {}".format(j)))
        super().on_kv_post(base_widget)

    def onSendComment(self):
        if self.comment_field.text != '':
            self.comment_lst.add_widget(
                CommentBox(text=self.comment_field.text.replace("\n", ''))
            )
            self.comment_field.text = ""
    
    def loadComment(self,instance):
        print(instance.scroll_y,self.comment_lst.size)
        for i in range(0,10):
            print(self.comment_lst.children[i].pos)
    
    def loadCommentMore(self,instance):
        print(instance.scroll_y,self.comment_lst.size)
        for i in range(20,40):
            self.comment_lst.add_widget(CommentBox(text="Hello {}".format(i)))