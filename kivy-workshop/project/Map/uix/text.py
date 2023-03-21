from kivy.uix.label import Label
from kivy.utils import get_color_from_hex as hex_to_bin
from kivy.lang import Builder

from uix.colors import Colors

Builder.load_string("""
<Text@Label>:
    size_hint_x:None
    width:self.texture_size[0]
""")


class Text(Label):
    def __init__(self, text: str, font_size: int = 12, bold=False, italic=False,
                 color=hex_to_bin("#FAFAFA")):
        super().__init__(
            text=text, font_size=font_size, bold=bold, italic=italic, color=color)
