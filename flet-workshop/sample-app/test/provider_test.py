class Provider:
    def __init__(self):
        self._listeners = set()

    def add_listener(self, listener):
        self._listeners.add(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

    def notify_listeners(self):
        for listener in self._listeners:
            listener()


class MyDataProvider(Provider):
    def __init__(self, data):
        self._data = data
        super().__init__()

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify_listeners()


class MyWidget:
    def __init__(self, provider):
        self._provider = provider
        self._provider.add_listener(self.update)

    def update(self):
        data = self._provider.get_data()
        print(data)


provider = MyDataProvider("Initial Data")
widget = MyWidget(provider)
provider.set_data("New Data")
