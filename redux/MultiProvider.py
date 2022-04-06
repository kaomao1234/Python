import ChangeNotifierProvider as cnp


class MultiProvider:
    def __init__(self, providers: list[cnp.ChangeNotifierProvider]):
        self.providers = providers
