import kivy 
from kivy.app import App 
from kivy.lang import Builder
Labelkv = Builder.load_string("""
Label: 
    text: ('Hello World')
    font: '64pt'""")

class MyApp(App):
    def build(self):
        Labelkv.text = 'Hello Guy'
        return Labelkv
if __name__ == '__main__':
    MyApp().run()
    