import kivy
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.base import runTouchApp
# Build the .kv file
Builder.load_string("""
# Define the scroll view
<Controller>:
    layout_content: layout_content
    BoxLayout:
        id: bl
        orientation: 'vertical'
        padding: 10, 10
        row_default_height: '48dp'
        row_force_default: True
        spacing: 10, 10
        ScrollView:
            size: self.size
            GridLayout:
                id: layout_content
                size_hint_y: None
                cols: 1
                row_default_height: '20dp'
                row_force_default: True
                spacing: 0, 0
                padding: 0, 0

                Label:
                    text: "Lorem ipsum dolor sit amet"
""")


# Define scrollview class
class Controller(FloatLayout):
    layout_content = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.layout_content.bind(
            minimum_height=self.layout_content.setter('height'))


# run the App
runTouchApp(Controller())
