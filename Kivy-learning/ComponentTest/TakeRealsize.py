# import kivy
# from kivy.core.text import markup
# from kivy.uix.scatter import Scatter
# from kivy.uix.label import Label
# from kivy.app import App
# from kivy.uix.layout import Layout


# class TouchWidget(Scatter):
#     def __init__(self, **kwargs):
#         super(TouchWidget, self).__init__(**kwargs)
#         self.P = Label(text='[size=30]This is Widget', markup=True) 
#         self.P.bind(size=self.on_size)
#         self.on_size()
#         self.add_widget(self.P)

#     def on_size(self, *args):
#         print(self.P.size)


# class MyApp(App):
#     def build(self):
#         return TouchWidget()


# RunApp = MyApp()
# RunApp.run()
import kivy
from kivy.core.text import markup
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.layout import Layout
from kivy.graphics import Rectangle,Color


class TouchWidget(Scatter):
    def __init__(self, **kwargs):
        super(TouchWidget, self).__init__(**kwargs)
        self.P = Label(text='[size=30]This is Widget', markup=True)
        self.P.bind(on_touch_move=self.on_size)
        self.add_widget(self.P)
        self.size_hint=[None,None]
        self.size=[500,500]
        with self.canvas.before:
        	Color(rgba=[1,0,0,1])
        	Rectangle(pos=self.pos,size=self.size)

    def on_size(self, *args):
        print(args[0].pos)
        # print(self.P.size)


class MyApp(App):
    def build(self):
        return TouchWidget()


RunApp = MyApp()
RunApp.run()