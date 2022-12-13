from kivymd.uix.screen import MDScreen
class LoginScreen(MDScreen):
    def __init__(self,**kw):
        super(LoginScreen, self).__init__(**kw)
    def on_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.5
        self.manager.current = 'register_screen'