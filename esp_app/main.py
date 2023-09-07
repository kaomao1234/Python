import flet as ft
from view import MainView
from viewmodel import MainViewModel
from arduino_api import SerialApi
import threading
# import os
# os.system("C:/Github/Python/esp_app/env/Scripts/activate.bat")


def app(root: ft.Page):
    serial_api = SerialApi("COM1", 9600, 8)
    threading.Thread(target=serial_api.open).start()
    root.title = "EspApp"
    MainView(root=root, route="/",
             view_model=MainViewModel(serial_api=serial_api))
    root.update()
    root.go("/")


ft.app(app)
