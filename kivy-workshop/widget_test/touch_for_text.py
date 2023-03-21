import pprint
import kivy
from kivy.core.text import markup
from kivy.core.text import markup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window


class Emu(Screen):
    def __init__(self, **kw):
        super(Emu, self).__init__(**kw)
        self.wid_dict = {}
        self.plus = Button(text='+', font_size=20,
                           size_hint=(None, None))
        self.plus.bind()
        self.Pos_text = Label(markup=True)
        self.add_widget(self.Pos_text)
        self.add_widget(self.plus)

    def callback_pos(self, instance, value):
        self.Pos_text.text = f'{self.wid_dict[instance].text} is {value}\nsize is {instance.size}'
    # def on_touch_move(self,touch):
    #     print(touch)

    def addwidget(self, event):
        move = Scatter(size_hint=(None, None)) 

        no = len(self.wid_dict.keys())
        label = Label(text=f'[color=#ff3030ff]This is Move widget{no}[/color]',markup = True)
        self.wid_dict[move] = label
        move.bind()
        # move.bind(on_touch=self.on_touch_move)
        self.widdict = {}
        self.plus = Button(text='+', font_size=20,
                           size_hint=(None, None))
        self.plus.bind()
        self.add_widget(self.plus)

    def callback_pos(self, instance, value):
        print(self.widdict[instance].text)

    def addwidget(self, event):
        move = Scatter(size_hint=(None, None))
        no = len(self.widdict.keys())
        label = Label(text=f'This is Move widget{no}')
        self.widdict[move] = label
        move.bind()
        move.add_widget(label)
        self.add_widget(move)


class MyApp(App):
    def build(self):
        return Emu()


RunApp = MyApp()
RunApp.run()
