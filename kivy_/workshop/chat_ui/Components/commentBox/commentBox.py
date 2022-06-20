from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import *
from kivy.lang import Builder
Builder.load_file(r'Components\commentBox\commentBox.kv')
class CommentBox(MDBoxLayout):
    avartar = StringProperty("human")
    text = StringProperty()
    