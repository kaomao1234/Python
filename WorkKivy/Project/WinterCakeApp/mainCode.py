import kivymd
import kivy
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
path_kv = "C:/Users/borip/Documents/GitHub/PythonWorkShop/WorkKivy/Project/WinterCakeApp/Page/"
for i in ['Login','Onboarding']:
    Builder.load_file(f"{path_kv}{i}.kv")
class Onboarding(MDScreen):
    pass
class Login(MDScreen):
    pass
class WinterCake(MDApp):
    def build(self):
        return Onboarding()
if __name__ == '__main__':
    WinterCake().run()