from typing import Dict, Any, List

from kivy.utils import get_hex_from_color, get_color_from_hex as hex_to_bin


class Colors:
    red = {
        50: hex_to_bin("#FFEBEE"),
        100: hex_to_bin("#FFCDD2"),
        200: hex_to_bin("#EF9A9A"),
        300: hex_to_bin("#E57373"),
        400: hex_to_bin("#EF5350"),
        500: hex_to_bin("#F44336"),
        600: hex_to_bin("#E53935"),
        700: hex_to_bin("#D32F2F"),
        800: hex_to_bin("#C62828"),
        900: hex_to_bin("#B71C1C"),
    }
    red_accent = {
        100: hex_to_bin("#FF8A80"),
        200: hex_to_bin("#FF5252"),
        400: hex_to_bin("#FF1744"),
        700: hex_to_bin("#D50000"),
    }
    pink = {
        50: hex_to_bin("#FCE4EC"),
        100: hex_to_bin("#F8BBD0"),
        200: hex_to_bin("#F48FB1"),
        300: hex_to_bin("#F06292"),
        400: hex_to_bin("#EC407A"),
        500: hex_to_bin("#E91E63"),
        600: hex_to_bin("#D81B60"),
        700: hex_to_bin("#C2185B"),
        800: hex_to_bin("#AD1457"),
        900: hex_to_bin("#880E4F"),
    }
    pink_accent = {
        100: hex_to_bin("#FF80AB"),
        200: hex_to_bin("#FF4081"),
        400: hex_to_bin("#F50057"),
        700: hex_to_bin("#C51162"),
    }
    purple = {
        50: hex_to_bin("#F3E5F5"),
        100: hex_to_bin("#E1BEE7"),
        200: hex_to_bin("#CE93D8"),
        300: hex_to_bin("#BA68C8"),
        400: hex_to_bin("#AB47BC"),
        500: hex_to_bin("#9C27B0"),
        600: hex_to_bin("#8E24AA"),
        700: hex_to_bin("#7B1FA2"),
        800: hex_to_bin("#6A1B9A"),
        900: hex_to_bin("#4A148C"),
    }
    purple_accent = {
        100: hex_to_bin("#EA80FC"),
        200: hex_to_bin("#E040FB"),
        400: hex_to_bin("#D500F9"),
        700: hex_to_bin("#AA00FF"),
    }
    deep_purple = {
        50: hex_to_bin("#EDE7F6"),
        100: hex_to_bin("#D1C4E9"),
        200: hex_to_bin("#B39DDB"),
        300: hex_to_bin("#9575CD"),
        400: hex_to_bin("#7E57C2"),
        500: hex_to_bin("#673AB7"),
        600: hex_to_bin("#5E35B1"),
        700: hex_to_bin("#512DA8"),
        800: hex_to_bin("#4527A0"),
        900: hex_to_bin("#311B92"),
    }

    deep_purple_accent = {
        100: hex_to_bin("#B388FF"),
        200: hex_to_bin("#7C4DFF"),
        400: hex_to_bin("#651FFF"),
        700: hex_to_bin("#6200EA"),
    }

    indigo = {
        50: hex_to_bin("#E8EAF6"),
        100: hex_to_bin("#C5CAE9"),
        200: hex_to_bin("#9FA8DA"),
        300: hex_to_bin("#7986CB"),
        400: hex_to_bin("#5C6BC0"),
        500: hex_to_bin("#3F51B5"),
        600: hex_to_bin("#3949AB"),
        700: hex_to_bin("#303F9F"),
        800: hex_to_bin("#283593"),
        900: hex_to_bin("#1A237E"),
    }
    indigo_accent = {
        100: hex_to_bin("#8C9EFF"),
        200: hex_to_bin("#536DFE"),
        400: hex_to_bin("#3D5AFE"),
        700: hex_to_bin("#304FFE"),
    }

    blue = {
        50: hex_to_bin("#E3F2FD"),
        100: hex_to_bin("#BBDEFB"),
        200: hex_to_bin("#90CAF9"),
        300: hex_to_bin("#64B5F6"),
        400: hex_to_bin("#42A5F5"),
        500: hex_to_bin("#2196F3"),
        600: hex_to_bin("#1E88E5"),
        700: hex_to_bin("#1976D2"),
        800: hex_to_bin("#1565C0"),
        900: hex_to_bin("#0D47A1"),
    }

    blue_accent = {
        100: hex_to_bin("#82B1FF"),
        200: hex_to_bin("#448AFF"),
        400: hex_to_bin("#2979FF"),
        700: hex_to_bin("#2962FF"),
    }

    light_blue = {
        50: hex_to_bin("#E1F5FE"),
        100: hex_to_bin("#B3E5FC"),
        200: hex_to_bin("#81D4FA"),
        300: hex_to_bin("#4FC3F7"),
        400: hex_to_bin("#29B6F6"),
        500: hex_to_bin("#03A9F4"),
        600: hex_to_bin("#039BE5"),
        700: hex_to_bin("#0288D1"),
        800: hex_to_bin("#0277BD"),
        900: hex_to_bin("#01579B"),
    }

    light_blue_accent = {
        100: hex_to_bin("#80D8FF"),
        200: hex_to_bin("#40C4FF"),
        400: hex_to_bin("#00B0FF"),
        700: hex_to_bin("#0091EA"),
    }

    cyan = {
        50: hex_to_bin("#E0F7FA"),
        100: hex_to_bin("#B2EBF2"),
        200: hex_to_bin("#80DEEA"),
        300: hex_to_bin("#4DD0E1"),
        400: hex_to_bin("#26C6DA"),
        500: hex_to_bin("#00BCD4"),
        600: hex_to_bin("#00ACC1"),
        700: hex_to_bin("#0097A7"),
        800: hex_to_bin("#00838F"),
        900: hex_to_bin("#006064"),
    }

    cyan_accent = {
        100: hex_to_bin("#84FFFF"),
        200: hex_to_bin("#18FFFF"),
        400: hex_to_bin("#00E5FF"),
        700: hex_to_bin("#00B8D4"),
    }

    teal = {
        50: hex_to_bin("#E0F2F1"),
        100: hex_to_bin("#B2DFDB"),
        200: hex_to_bin("#80CBC4"),
        300: hex_to_bin("#4DB6AC"),
        400: hex_to_bin("#26A69A"),
        500: hex_to_bin("#009688"),
        600: hex_to_bin("#00897B"),
        700: hex_to_bin("#00796B"),
        800: hex_to_bin("#00695C"),
        900: hex_to_bin("#004D40"),
    }

    teal_accent = {
        100: hex_to_bin("#A7FFEB"),
        200: hex_to_bin("#64FFDA"),
        400: hex_to_bin("#1DE9B6"),
        700: hex_to_bin("#00BFA5"),
    }

    green = {
        50: hex_to_bin("#E8F5E9"),
        100: hex_to_bin("#C8E6C9"),
        200: hex_to_bin("#A5D6A7"),
        300: hex_to_bin("#81C784"),
        400: hex_to_bin("#66BB6A"),
        500: hex_to_bin("#4CAF50"),
        600: hex_to_bin("#43A047"),
        700: hex_to_bin("#388E3C"),
        800: hex_to_bin("#2E7D32"),
        900: hex_to_bin("#1B5E20"),
    }

    green_accent = {
        100: hex_to_bin("#B9F6CA"),
        200: hex_to_bin("#69F0AE"),
        400: hex_to_bin("#00E676"),
        700: hex_to_bin("#00C853"),
    }

    light_green = {
        50: hex_to_bin("#F1F8E9"),
        100: hex_to_bin("#DCEDC8"),
        200: hex_to_bin("#C5E1A5"),
        300: hex_to_bin("#AED581"),
        400: hex_to_bin("#9CCC65"),
        500: hex_to_bin("#8BC34A"),
        600: hex_to_bin("#7CB342"),
        700: hex_to_bin("#689F38"),
        800: hex_to_bin("#558B2F"),
        900: hex_to_bin("#33691E"),
    }

    light_green_accent = {
        100: hex_to_bin("#CCFF90"),
        200: hex_to_bin("#B2FF59"),
        400: hex_to_bin("#76FF03"),
        700: hex_to_bin("#64DD17"),
    }

    lime = {
        50: hex_to_bin("#F9FBE7"),
        100: hex_to_bin("#F0F4C3"),
        200: hex_to_bin("#E6EE9C"),
        300: hex_to_bin("#DCE775"),
        400: hex_to_bin("#D4E157"),
        500: hex_to_bin("#CDDC39"),
        600: hex_to_bin("#C0CA33"),
        700: hex_to_bin("#AFB42B"),
        800: hex_to_bin("#9E9D24"),
        900: hex_to_bin("#827717"),
    }

    lime_accent = {
        100: hex_to_bin("#F4FF81"),
        200: hex_to_bin("#EEFF41"),
        400: hex_to_bin("#C6FF00"),
        700: hex_to_bin("#AEEA00"),
    }

    yellow = {
        50: hex_to_bin("#FFFDE7"),
        100: hex_to_bin("#FFF9C4"),
        200: hex_to_bin("#FFF59D"),
        300: hex_to_bin("#FFF176"),
        400: hex_to_bin("#FFEE58"),
        500: hex_to_bin("#FFEB3B"),
        600: hex_to_bin("#FDD835"),
        700: hex_to_bin("#FBC02D"),
        800: hex_to_bin("#F9A825"),
        900: hex_to_bin("#F57F17"),
    }

    yellow_accent = {
        100: hex_to_bin("#FFFF8D"),
        200: hex_to_bin("#FFFF00"),
        400: hex_to_bin("#FFEA00"),
        700: hex_to_bin("#FFD600"),
    }

    amber = {
        50: hex_to_bin("#FFF8E1"),
        100: hex_to_bin("#FFECB3"),
        200: hex_to_bin("#FFE082"),
        300: hex_to_bin("#FFD54F"),
        400: hex_to_bin("#FFCA28"),
        500: hex_to_bin("#FFC107"),
        600: hex_to_bin("#FFB300"),
        700: hex_to_bin("#FFA000"),
        800: hex_to_bin("#FF8F00"),
        900: hex_to_bin("#FF6F00"),
    }

    amber_accent = {
        100: hex_to_bin("#FFE57F"),
        200: hex_to_bin("#FFD740"),
        400: hex_to_bin("#FFC400"),
        700: hex_to_bin("#FFAB00"),
    }

    orange = {
        50: hex_to_bin("#FFF3E0"),
        100: hex_to_bin("#FFE0B2"),
        200: hex_to_bin("#FFCC80"),
        300: hex_to_bin("#FFB74D"),
        400: hex_to_bin("#FFA726"),
        500: hex_to_bin("#FF9800"),
        600: hex_to_bin("#FB8C00"),
        700: hex_to_bin("#F57C00"),
        800: hex_to_bin("#EF6C00"),
        900: hex_to_bin("#E65100"),
    }

    orange_accent = {
        100: hex_to_bin("#FFD180"),
        200: hex_to_bin("#FFAB40"),
        400: hex_to_bin("#FF9100"),
        700: hex_to_bin("#FF6D00"),
    }
    deep_orange = {
        50: hex_to_bin("#FBE9E7"),
        100: hex_to_bin("#FFCCBC"),
        200: hex_to_bin("#FFAB91"),
        300: hex_to_bin("#FF8A65"),
        400: hex_to_bin("#FF7043"),
        500: hex_to_bin("#FF5722"),
        600: hex_to_bin("#F4511E"),
        700: hex_to_bin("#E64A19"),
        800: hex_to_bin("#D84315"),
        900: hex_to_bin("#BF360C"),
    }

    deep_orange_accent = {
        100: hex_to_bin("#FF9E80"),
        200: hex_to_bin("#FF6E40"),
        400: hex_to_bin("#FF3D00"),
        700: hex_to_bin("#DD2C00"),
    }

    brown = {
        50: hex_to_bin("#EFEBE9"),
        100: hex_to_bin("#D7CCC8"),
        200: hex_to_bin("#BCAAA4"),
        300: hex_to_bin("#A1887F"),
        400: hex_to_bin("#8D6E63"),
        500: hex_to_bin("#795548"),
        600: hex_to_bin("#6D4C41"),
        700: hex_to_bin("#5D4037"),
        800: hex_to_bin("#4E342E"),
        900: hex_to_bin("#3E2723"),
    }
    grey = {
        50: hex_to_bin("#FAFAFA"),
        100: hex_to_bin("#F5F5F5"),
        200: hex_to_bin("#EEEEEE"),
        300: hex_to_bin("#E0E0E0"),
        350: hex_to_bin("#D6D6D6"),
        400: hex_to_bin("#BDBDBD"),
        500: hex_to_bin("#9E9E9E"),
        600: hex_to_bin("#757575"),
        700: hex_to_bin("#616161"),
        800: hex_to_bin("#424242"),
        850: hex_to_bin("#303030"),
        900: hex_to_bin("#212121"),
    }
    blue_grey = {
        50: hex_to_bin("#ECEFF1"),
        100: hex_to_bin("#CFD8DC"),
        200: hex_to_bin("#B0BEC5"),
        300: hex_to_bin("#90A4AE"),
        400: hex_to_bin("#78909C"),
        500: hex_to_bin("#607D8B"),
        600: hex_to_bin("#546E7A"),
        700: hex_to_bin("#455A64"),
        800: hex_to_bin("#37474F"),
        900: hex_to_bin("#263238"),
    }
    black = {
        0: hex_to_bin("#000000")
        , 87: (0, 0, 0, 221 / 255)
        , 54: (0, 0, 0, 138 / 255)
        , 45: (0, 0, 0, 115 / 255)
        , 38: (0, 0, 0, 97 / 255)
        , 26: (0, 0, 0, 66 / 255)
        , 12: (0, 0, 0, 31 / 255)
    }
    white = {
        0: hex_to_bin("#FFFFFFFF"),
        70: (179 / 255, 1, 1, 1 / 255),
        60: (153 / 255, 1, 1, 1 / 255),
        54: (138 / 255, 1, 1, 1 / 255),
        38: (98 / 255, 1, 1, 1 / 255),
        30: (77 / 255, 1, 1, 1 / 255),
        24: (61 / 255, 1, 1, 1 / 255),
        12: (31 / 255, 1, 1, 1 / 255),
        10: (26 / 255, 1, 1, 1 / 255),
    }

    def __init__(self):
        self.primaries = [
            self.red,
            self.pink,
            self.purple,
            self.deep_purple,
            self.indigo,
            self.blue,
            self.light_blue,
            self.cyan,
            self.teal,
            self.green,
            self.light_green,
            self.lime,
            self.yellow,
            self.amber,
            self.orange,
            self.deep_orange,
            self.brown,
            self.blue_grey,
        ]

        self.primaries_dict = {
            'red': [self.red, self.red_accent],
            'pink': [self.pink, self.pink_accent],
            'purple': [self.purple, self.purple_accent],
            'deep purple': [self.deep_purple, self.deep_purple_accent],
            'indigo': [self.indigo, self.indigo_accent],
            'blue': [self.blue, self.blue_accent],
            'light blue': [self.light_blue, self.light_blue_accent],
            'cyan': [self.cyan, self.cyan_accent],
            'teal': [self.teal, self.teal_accent],
            'green': [self.green, self.green_accent],
            'light green': [self.light_green, self.light_green_accent],
            'lime': [self.lime, self.lime_accent],
            'yellow': [self.yellow, self.yellow_accent],
            'amber': [self.amber, self.amber_accent],
            'orange': [self.orange, self.orange_accent],
            'deep orange': [self.deep_orange, self.deep_orange_accent],
            'brown': self.brown,
            'grey': self.grey,
            'blue grey': self.blue_grey,
            'black': self.black,
            'white': self.white
        }

    @staticmethod
    def color_from_hex(hex_str: str):
        return hex_to_bin(hex_str)
# print(len(Colors().primaries))
# print(f"{Colors.red=}".split('=')[0])
