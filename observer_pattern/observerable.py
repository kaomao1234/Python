class Observable:
    def __init__(self):
        self._obsververs: list = []

    def subscribe(self, observer):
        self._obsververs.append(observer)

    def notify(self):
        for observer in self._obsververs:
            if observer.listening:
                observer.notify()

    def unsubscribe(self, observer):
        self._observers.remove(observer)
