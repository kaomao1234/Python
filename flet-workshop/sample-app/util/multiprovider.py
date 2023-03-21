class MultiProvider:
    def __init__(self, **providers):
        self._providers = {}
        for key, provider in providers.items():
            self._providers[key] = provider()
            self._providers[key].add_listener(self.update)

    def update(self):
        for provider in self._providers.values():
            provider.notify_listeners()

    def __getattr__(self, name):
        if name in self._providers:
            return self._providers[name]
