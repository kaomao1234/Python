import importlib
import View.HomeScreen.home_screen
import Model.home_screen
importlib.reload(View.HomeScreen.home_screen)
importlib.reload(Model.home_screen)


class HomeScreenController:
    def __init__(self, model):
        self.model = model
        self.view = View.HomeScreen.home_screen.HomeScreen(controller=self, model=self.model)

    def get_view(self) -> View.HomeScreen.home_screen:
        return self.view

