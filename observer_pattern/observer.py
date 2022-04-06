class Observer:
    def __init__(self, observable):
        self.observable = observable
        self.listening = False
        self.observable.subscribe(self)

    def notify(self):
        print("I am notified")
        self.listening = False

    def bussiness_logic(self):
        self.listening = True
