import importlib

import View.MainScreen.main_screen
import Model.main_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.MainScreen.main_screen)
importlib.reload(Model.main_screen)


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model: Model.main_screen.MainScreenModel = model  # Model.main_screen.MainScreenModel
        self.view = View.MainScreen.main_screen.MainScreenView(controller=self, model=self.model)
        self.crop_image = self.model.crop_image
        self.full_screen_capture = self.model.full_screen_capture

    def get_view(self) -> View.MainScreen.main_screen:
        return self.view

    def increment(self):
        self.model.notify_observers("main screen")
