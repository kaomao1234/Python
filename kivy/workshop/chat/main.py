
from kivy.app import App

from controller import Controller


class Chat(App):
    def build(self):
        return Controller()


if __name__ == "__main__":
    Chat().run()