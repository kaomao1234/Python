from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import *
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
import pprint

Builder.load_string("""
<ListViewItem>:
    on_kv_post:self.refresh_view_attrs()
""")


# > This class is a BoxLayout that can be used in a RecycleView
class ListViewItem(RecycleDataViewBehavior, BoxLayout):
    child: Widget = ObjectProperty()
    index = None
    owner = ObjectProperty()

    def __init__(self):
        super(ListViewItem, self).__init__()
        self.data = None
        # print("this class is deprecated")
        # self.l = Label()

    def refresh_view_attrs(self, rv, index, data):
        return super().refresh_view_attrs(rv, index, data)


class ListViewBuilder(RecycleView):
    def __init__(self, children: list[Widget]):
        super().__init__()

        self.recycle_box_layout = RecycleBoxLayout(
            default_size=(None, dp(56)), default_size_hint=(1, None),
            size_hint=(1, None), orientation='vertical'
        )
        self.recycle_box_layout.bind(
            minimum_height=self.recycle_box_layout.setter("height")
        )
        self.add_widget(self.recycle_box_layout)
        self.viewclass = 'ListViewItem'
        self.data = [
            {
                'child': ele,
                'index': idx,
                'owner': self

            }
            for idx, ele in enumerate(children)
        ]


class MainApp(App):
    def build(self):
        return ListViewBuilder(
            [
                Label(text=f"Hello {i}")
                for i in range(20)
            ]
        )


MainApp().run()
