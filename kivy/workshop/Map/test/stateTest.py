from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from uix.row import Row


class StateFull(BoxLayout):
    def __init__(self, **kwargs):
        super(StateFull, self).__init__(**kwargs)
        self.orientation = 'horizontal'

    def create_state(self) -> Widget:
        self.add_widget(_StateFull(self).build())


class _StateFull(BoxLayout):
    def __init__(self, state: StateFull, **kwargs):
        super(_StateFull, self).__init__(**kwargs)
        self.state = state
        self.var = 1
        self.state = lambda: Row(
            children=[Button(text=f"{i} set state {self.var}",
                             on_press=lambda *e:  self.set_state()) for i in range(0, 10)]
        )

    def set_state(self):
        self.clear_widgets()
        self.var += 1
        self.build()

    def build(self) -> Widget:
        self.add_widget(
            self.state()
        )
        return self


class MApp(App):
    def build(self):
        state_widget = StateFull()
        state_widget.create_state()
        return state_widget


MApp().run()
