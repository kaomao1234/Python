from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel


class HomeView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # Add a greeting label
        self.add_widget(MDLabel(
            text="Welcome to the Recipe App!",
            font_style="H3",
            halign="center"
        ))

        # Add a button to browse recipes
        self.browse_button = MDRectangleFlatButton(
            text="Browse Recipes",
            on_release=self.browse_recipes
        )
        self.add_widget(self.browse_button)

        # Add a button to search for recipes
        self.search_button = MDRectangleFlatButton(
            text="Search Recipes",
            on_release=self.search_recipes
        )
        self.add_widget(self.search_button)

    def browse_recipes(self, instance):
        # Open the recipe list view
        pass

    def search_recipes(self, instance):
        # Open the search view
        pass


class RecipeApp(MDApp):
    theme_cls = ThemeManager()

    def build(self):
        return HomeView()


if __name__ == "__main__":
    RecipeApp().run()

