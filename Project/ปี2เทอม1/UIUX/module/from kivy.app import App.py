from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

Builder.load_string('''
<table@BoxLayout>:
    col1: ''
    col2: ''
    col3: ''
    col4: ''
    size_hint: None, None
    width: 1600
    height: 32
    orientation: 'vertical'
    Label:
        text: root.col1
    Label:
        text: root.col2
    Label:
        text: root.col3
    Label:
        text: root.col4

<RV>:
    viewclass: 'table'
    scroll_type: ['bars','content']
    bar_width: 16
    do_scroll_x: True
    do_scroll_y: False
    size_hint: 1, 1
    RecycleBoxLayout:
        orientation: 'horizontal'
        # size_hint_y: None
        size_hint_x: None
        default_size_hint: None,1
        spacing: '10dp'
        default_size: 500,None
        height: self.minimum_height
        width: self.minimum_width
''')

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'col1': 'Just some Text to fill the void', 'col2': 'Another, shorter Text', 'col3': f'And now some numbers: {x}', 'col4': 'Lorem Ipsum Dolor'} for x in range(200)]


class TestApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    TestApp().run()