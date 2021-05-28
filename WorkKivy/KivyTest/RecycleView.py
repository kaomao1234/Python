from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.utils import rgba
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

class Rebox(RecycleBoxLayout):
    def __init__(self, **kwargs):
        super(Rebox, self).__init__(**kwargs)
        self.color = (0, 0.7, 0.4, 0.8)
        self.default_size = (None, None)
        self.default_size_hint = (.4, None)
        self.size_hint_y = None
        self.height = self.minimum_height
        self.orientation = 'vertical'

class ExampleViewer(RecycleView):
    def __init__(self, **kwargs):
        super(ExampleViewer, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(20)]
        self.orientation = 'vertical'
        self.viewclass = 'Button'
        self.spacing = 40
        self.padding = (10, 10)
        self.space_x = self.size[0]/3
        self.add_widget(RecycleBoxLayout())


class MainScreen(Screen):
    def __init__(self, **kw):
        super(MainScreen, self).__init__(**kw)


class BuildApp(App):
    def build(self):
        return ExampleViewer()


myApp = BuildApp()
myApp.run()
# from kivy.uix.recycleview import RecycleView
# from kivy.app import App
# from kivy.lang import Builder
# Builder.load_file('Recycle.kv')
# # The ScrollView widget provides a scrollable view


# # Define the Recycleview class which is created in .kv file
# class ExampleViewer(RecycleView):
#     def __init__(self, **kwargs):
#         super(ExampleViewer, self).__init__(**kwargs)
#         self.data = [{'text': str(x)} for x in range(20)]


# # Create the App class with name of your app.
# class SampleApp(App):
#     def build(self):
#         return ExampleViewer()


# # run the App
# SampleApp().run()
