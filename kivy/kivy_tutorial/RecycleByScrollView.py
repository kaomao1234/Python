from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
Builder.load_string("""
<ScrollWidget>:
    MDList:
        spacing:10
        id:container
""")
class ScrollWidget(ScrollView):
    def __init__(self):
        super(ScrollWidget, self).__init__()
        self.container:MDList = self.ids.container
        self.lst_btn = [Button(text=str(i),size_hint_y=None) for i in range(10)]
        self.putInContainer()
        # self.bind(on_scroll_start=lambda *s :print(self.scroll_y))
    
    def putInContainer(self):
        for i in range(10):
            self.container.add_widget(Button(text=str(i),size_hint_y=None))

# class runTouchApp(MDApp):
#     def __init__(self,container):
#         super().__init__()
#         self.container = container
#         self.box = MDBoxLayout()
#         # self.box.add_widget(self.container)
#     def build(self):
#         return self.container
# if __name__ == '__main__':
    # runTouchApp(ScrollWidget()).run()