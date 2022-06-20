from kivymd.app import MDApp
from Screens.OnboardScreen.onboard_screen import OnboardScreen
class IncognitoChat(MDApp):
    def build(self):
        return OnboardScreen()

if __name__ == '__main__':
    IncognitoChat().run()