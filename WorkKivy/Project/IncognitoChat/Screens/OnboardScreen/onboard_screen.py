from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
class OnboardScreen(MDScreen):
    def __init__(self,**kw):
        super(OnboardScreen, self).__init__(**kw)
        Clock.schedule_once(lambda s : setattr(self.ids.fit_image,'source','assets\images\image1blur.png'),1)
    
    
    