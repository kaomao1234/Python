import kivy
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

class DropWidget(DropDown):
    def __init__(self, **kwargs):
        super(DropWidget, self).__init__(**kwargs)
        for i in range(1, 20):
            self.btn = Button(text=f'value{i}',size_hint=(None,None ),height=30)
            self.btn.bind(on_release=lambda btn: self.select(btn.text))
            self.add_widget(self.btn)


class Display(GridLayout):
    def __init__(self, **kw):
        super(Display, self).__init__(**kw)
        self.dropdown = DropWidget()
        self.main_btn = Button(text ='Hello', size_hint =(None, None), pos =(350, 400)) 
        self.main_btn.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select = self.on_select)
        self.add_widget(self.main_btn)
    def on_select(self,instance,event):
        self.main_btn.text = event
        
class RunApp(App):
    def build(self):
        return Display()


App = RunApp()
App.run()
