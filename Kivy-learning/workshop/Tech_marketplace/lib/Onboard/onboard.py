from kivymd.uix.screen import MDScreen
class OnboardScreen(MDScreen):
    def __init__(self,**kw):
        super(OnboardScreen, self).__init__(**kw)
        
    def switch_onboard_screen(self,direction,duration,name):
        self.ids.onboard_manager.transition.direction = direction
        self.ids.onboard_manager.transition.duration = duration
        self.ids.onboard_manager.current = name
    