from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView


class MainWidget(FloatLayout):

    def create_layouts(self):
        self.create_recycle_view()

    def create_recycle_view(self):
        recycle_box_layout = RecycleBoxLayout(default_size=(None, dp(56)), default_size_hint=(1, None),
                                              size_hint=(1, None), orientation='vertical')
        recycle_box_layout.bind(
            minimum_height=recycle_box_layout.setter("height"))
        recycle_view = RecycleView()
        recycle_view.add_widget(recycle_box_layout)
        recycle_view.viewclass = 'Label'
        self.add_widget(recycle_view)
        recycle_view.data = [{'text': str(x)} for x in range(20)]


class MainApp(App):
    def build(self):
        Clock.schedule_once(self.add_rv)
        return MainWidget()

    def add_rv(self, dt):
        self.root.create_layouts()


MainApp().run()
