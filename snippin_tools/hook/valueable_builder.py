from typing import Callable
import flet as ft


class ValueNotifier:
    def __init__(self, callback_value: Callable) -> None:
        self.callback_value = callback_value
        self.buffer_value = callback_value()
        self.listeners: list[Callable] = []

    @property
    def get(self):
        return self.callback_value()

    def add_listener(self, listener: Callable):
        self.listeners.append(listener)

    def remove_listener(self, listener: Callable):
        self.listeners.remove(listener)

    def notifiy_listener(self):
        for i in self.listeners:
            i()


class ValueListenableBuilder:
    def __init__(self, value_listenable: ValueNotifier, builder: Callable) -> None:
        self.value_listenable = value_listenable
        self.view = ft.Container(
            content=builder(value_listenable.get)
        )
        self.builder = builder
        value_listenable.add_listener(self.listening)

    def listening(self):
        if (self.value_listenable.buffer_value != self.value_listenable.get):
            self.view.clean()
            self.view.content = self.builder(self.value_listenable.get)
            self.value_listenable.buffer_value = self.value_listenable.get
