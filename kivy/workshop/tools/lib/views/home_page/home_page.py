from kivymd.uix.screen import MDScreen
try:
    from lib.modules.foo import foo
except:
    from modules.foo import foo

class HomePage(MDScreen):

    def on_press(self):
        foo()