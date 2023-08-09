from PIL.Image import Image
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle, Canvas
from PIL import ImageGrab
from io import BytesIO

Builder.load_string("""
<RootWidget>:
    orientation: 'vertical'

    MDRaisedButton:
        text: "Capture Snip"
        on_release: app.capture_screenshot()

    ImageWidget:
        id: screenshot_display
""")

class ImageWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.texture = None
        self.canvas = self._create_canvas()
        self.canvas_size = (Window.width, Window.height)  # Store canvas size for reference
        self.add_widget(self.canvas)

    def _create_canvas(self):
        canvas = Canvas()  # Create a new canvas
        with canvas:
            self.rect = Rectangle(size=self.canvas_size, pos=self.pos)
        return canvas

    def update_texture(self, image_data):
        if self.texture is None:
            self.texture = Texture.create(size=self.canvas_size)
            self.rect.texture = self.texture
        self.texture.blit_buffer(image_data, colorfmt='rgba', bufferfmt='ubyte')


class RootWidget(BoxLayout):
    pass

class SnippingToolApp(MDApp):
    def build(self):
        self.root = RootWidget()
        return self.root

    def capture_screenshot(self):
        screenshot = ImageGrab.grab(bbox=(Window.left, Window.top, Window.right, Window.bottom))
        screenshot = screenshot.transpose(Image.FLIP_TOP_BOTTOM)
        screenshot_io = BytesIO()
        screenshot.save(screenshot_io, format='png')
        screenshot_data = screenshot_io.getvalue()
        self.root.ids.screenshot_display.update_texture(screenshot_data)

if __name__ == "__main__":
    SnippingToolApp().run()
