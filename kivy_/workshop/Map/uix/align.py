from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget


class Align(AnchorLayout):
    def __init__(self, child: Widget, x='center', y='center'):
        super().__init__(anchor_x=x, anchor_y=y)
        self.child = child
        self.add_widget(self.child)
