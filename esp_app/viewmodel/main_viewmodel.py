from arduino_api import SerialApi
from typing import Callable


class MainViewModel:
    def __init__(self, serial_api: SerialApi) -> None:
        self.serial_api = serial_api

    def serial_read(self) -> str:
        return self.serial_api.readline()

    def serial_write(self, text):
        self.serial_write(text)

    def add_serial_listener(self, callback: Callable):
        self.serial_api.add_listener(callback=callback)

    def remove_serial_listener(self, callback: Callable):
        self.serial_api.remove_listener(callback=callback)
