import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
Builder.load_string("""
<CustomDropDown>:
    Button:
        text: 'College Name'
        size_hint_y: None
        height: 44
        on_release: root.select('College is')
    Label:
        text: 'Not in college'
        size_hint_y: None
        height: 44
    Button:
        text: 'KccItm'
        size_hint_y: None
        height: 44
        on_release: root.select('Kcc')
""")


class CustomDropDown(DropDown):
    pass


class DropdownDemo(FloatLayout):
    def __init__(self, **kwargs):
        super(DropdownDemo, self).__init__(**kwargs)
        self.dropdown = CustomDropDown()
        self.mainbutton = Button(text='Do you in college?', size_hint_y=0.15,
                                 size_hint_x=0.6, on_release=self.dropdown.open)
        self.add_widget(self.mainbutton)
        self.dropdown.bind(on_select=lambda instance,
                           x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select=self.callback)

    def callback(self, instance, x):
        print("The chosen mode is: {0}" . format(x))


class MyApp(App):
    def build(self):
        return DropdownDemo()


if __name__ == '__main__':
    MyApp().run()
