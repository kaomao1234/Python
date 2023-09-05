from Model.base_model import BaseScreenModel
from Utility import full_screen_capture,crop_image


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self):
        super().__init__()
        self.full_screen_capture = full_screen_capture
        self.crop_image = crop_image
