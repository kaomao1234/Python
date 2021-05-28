from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

Builder.load_string('''

<RV>:
    viewclass: 'RVItem'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'

''')

class Attribute:
    def __init__(self, name, values):
        self.name = name
        self.values = values


class RVItem(RecycleDataViewBehavior, BoxLayout):
    index = None
    attribute = ObjectProperty()

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        self.create_widgets(data['attribute'])
        return super(RVItem, self).refresh_view_attrs(
            rv, index, data)

    def create_widgets(self, value: Attribute):
        rv = App.get_running_app().root
        rv.cache_widgets(self.children)
        self.clear_widgets()
        label = rv.get_label()
        label.text = value.name
        self.add_widget(label)
        if isinstance(value.values, dict):
            for _,v in value.values.items():
                label = rv.get_label()
                label.text = v
                self.add_widget(label)
        else:
            label = rv.get_label()
            label.text = value.values
            self.add_widget(label)
        image_button = rv.get_button()
        image_button.text = '+'
        image_button.size_hint = None, None
        image_button.size = "30sp", "30sp"
        image_button.bind(on_press=self.add_button_pressed)
        self.add_widget(image_button)


    def add_button_pressed(self, s):
        print("Would add a new item to the recycleview if implemented.")


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.label_cache = []
        self.button_cache = []
        self.data = [{'attribute': Attribute(str(x), "test")} for x in range(100)]
        for i in range(100):
            if i % 5 == 0:
                self.data[i]['attribute'].values = {'1': 'test1', '2': 'test2', '3': 'test3'}
    def get_button(self):
        if len(self.button_cache) > 0:
            return self.button_cache.pop()
        else:
            return Button()

    def get_label(self):
        if len(self.label_cache) > 0:
            return self.label_cache.pop()
        else:
            return Label()

    def cache_widgets(self, widgets):
        for w in widgets:
            if isinstance(w, Button):
                self.button_cache.append(w)
            else:
                self.label_cache.append(w)


class TestApp(App):
    def build(self):
        return RV()

TestApp().run()