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
from kivy.uix.anchorlayout import AnchorLayout
import pprint


class TouchWidget(Scatter):
    def __init__(self, **kwargs):
        super(TouchWidget, self).__init__(**kwargs)
        self.size=[300,300]
        self.anchor = AnchorLayout(anchor_x="center",anchor_y="center")
        self.p = Label(text='[size=30]This is Widget', markup=True)
        self.anchor.add_widget(self.p)
        self.add_widget(self.anchor)
        with self.canvas.before:
        	Color(rgba=[1,0,0,1])
        	rec = Rectangle(pos=self.pos,size=self.size)

        self.p.bind(on_touch_move=lambda *e: self.on_move(rec,self.p,*e))

    
    def on_move(self, rec,p,*args):
        rec.pos = self.pos

class MyApp(App):
    def build(self):
        return TouchWidget()


RunApp = MyApp()
RunApp.run()
