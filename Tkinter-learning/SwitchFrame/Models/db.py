import datetime
class DataBase:
    def __init__(self):
        self.timeStamp = []
    
    def onCurrentTime(self):
        self.timeStamp.append(datetime.datetime.now().strftime("%H:%M:%S"))
    
    