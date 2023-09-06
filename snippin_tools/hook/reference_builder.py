from typing import Callable


class ReferenceNofifier:
    def __init__(self, value) -> None:
        self._value = value
        self.listeners = []

    @property
    def getValue(self):
        return self._value

    @getValue.setter
    def setValue(self, value):
        self._value = value


class ReferenceBuilder:
    def __init__(self, builder: Callable, referenceListenable: ReferenceNofifier) -> None:
        self.buider = builder(referenceListenable)
        referenceListenable.setValue = self.buider

    @property
    def builded(self):
        return self.buider
