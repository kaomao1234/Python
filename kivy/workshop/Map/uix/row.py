from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class Row(BoxLayout):
    def __init__(self, children: list[Widget]):
        super().__init__()
        self.orientation = "horizontal"
        for i in children:
            self.add_widget(i)
