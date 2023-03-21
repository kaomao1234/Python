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
