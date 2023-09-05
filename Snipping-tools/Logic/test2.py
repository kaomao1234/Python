from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
import time


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.minimize_button = Button(text='Minimize', size_hint=(None, None))
        self.minimize_button.bind(on_press=self.minimize_and_wait)

        layout.add_widget(self.minimize_button)

        return layout

    def minimize_and_wait(self, instance):
        Window.minimize()  # Minimize the window
        Clock.schedule_once(self.restore_after_delay, 1)  # Schedule the restore function after 1 second

    def restore_after_delay(self, dt):
        Window.restore()  # Restore (show) the window


if __name__ == '__main__':
    MyApp().run()
