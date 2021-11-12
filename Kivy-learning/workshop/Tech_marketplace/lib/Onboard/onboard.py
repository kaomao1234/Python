from kivymd.uix.screen import MDScreen
class OnboardScreen(MDScreen):
    def switch_onboard_screen(self,direction,duration,name):
        self.ids.onboard_manager.transition.direction = direction
        self.ids.onboard_manager.transition.duration = duration
        self.ids.onboard_manager.current = name