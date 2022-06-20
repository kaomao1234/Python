from kivy.app import App
from functools import partial
# The ScrollView widget provides a scrollable view
import pprint
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder
Builder.load_string("""
<ExampleViewer>:
    viewclass: 'CustomButton'  # defines the viewtype for the data items.
    orientation: "vertical"
    spacing: 40
    padding:10, 10
    space_x: self.size[0]/3
  
    RecycleBoxLayout:
        color:(0, 0.7, 0.4, 0.8)
        default_size: None, dp(56)
  
        # defines the size of the widget in reference to width and height
        default_size_hint: 0.4, None 
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical' # defines the orientation of data items
""")

# Define the Recycleview class which is created in .kv file


class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.on_press = self.clicked
        self.m = None
        # self.m = self.m(self)

    def clicked(self, *e):
        # pprint.pprint(sorted(self.__dir__()))
        self.setter()

    def setter(self):
        print(self.m(self))


class ExampleViewer(RecycleView):
    def __init__(self, **kwargs):
        super(ExampleViewer, self).__init__(**kwargs)
        self.data = [{'text': str(x), 'm': self.getInstance}
                     for x in range(10)]

    def getInstance(self, m=None):
        self.data.append({'text': str(len(self.data)), 'm': self.getInstance})
        return m
# Create the App class with name of your app.


class SampleApp(App):
    def build(self):
        return ExampleViewer()


# run the App
SampleApp().run()
