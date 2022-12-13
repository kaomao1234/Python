import importlib
import os
os.getcwd()
from kivy.config import Config
from PIL import ImageGrab

from views.pages import kvs,pys

resolution = ImageGrab.grab().size
Config.set('graphics', 'resizable', False)
# resolution of the application
Config.set("graphics", "height", resolution[1])
Config.set("graphics", "width", "400")

from kivy.core.window import Window

# Place the application window on the right side of the computer screen.
Window.top = 0
Window.left = resolution[0] - Window.width
from kaki.app import App
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager


class TempApp(MDApp, App):
    DEBUG = 1
    KV_FILES = kvs

    def build_app(self, first=False):
        import views.pages as pages
        importlib.reload(pages)
        self.manager_screens = MDScreenManager()
        Window.bind(on_key_down=self.on_keyboard_down)
        self.pages = pages.pages
        for name, page in self.pages.items():
            self.manager_screens.add_widget(page(name=name))
        return self.manager_screens

    def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
        """
        The method handles keyboard events.

        By default, a forced restart of an application is tied to the
        `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
        """

        if "meta" in modifiers or text == "Ĩ":
            import views.pages as pages
            importlib.reload(pages)
            for value in pages.pys:
                importlib.reload(value)
            self.rebuild()


TempApp().run()
