from kivymd.uix.screen import MDScreen
from viewmodels.home_viewmodel import HomeViewModel

class HomeScreen(MDScreen):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.viewmodel:HomeViewModel
    
    def on_kv_post(self, base_widget):
        self.viewmodel = HomeViewModel()
        self.ids.rv.data = self.viewmodel.get_random_recipes()
        return super().on_kv_post(base_widget)
    def on_press(self):
        print("Hi")
