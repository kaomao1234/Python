from kivymd.uix.widget import MDWidget

from View.base_screen import BaseScreenView
from kivy.properties import *
from tkinter import filedialog as fd
import kivy
from Utility.command import execute_command_project
import platform
from kivy.clock import Clock


class MainScreenView(BaseScreenView):
    output_message = StringProperty()
    project_name = StringProperty()
    directory = StringProperty()
    build_btn: MDWidget = ObjectProperty()
    optional: dict = DictProperty({
        "--use_hotreload": False
    })

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_browse(self):
        folder_select: str = fd.askdirectory()
        if len(folder_select) > 0:
            self.ids.path_text.text = folder_select.replace("\\", "/")

    def on_build(self, *args):
        enable_optional = [f"{k} yes" for k, v in self.optional.items() if v]
        if len(self.project_name) > 0 and len(self.directory) > 0:
            args[0].disabled = True
            Clock.schedule_once(lambda dt: self.build_project(enable_optional), 1)

    def build_project(self, enable_optional):
        self.output_message = execute_command_project("MVC", self.directory, self.project_name,
                                                      f"python{platform.python_version()[:-2]}", kivy.__version__,
                                                      *enable_optional)
        self.build_btn.disabled = False
        self.project_name = ""
        self.directory = ""
