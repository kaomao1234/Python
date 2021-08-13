import requests as rq 
from tkinter import *
class CoApp(Tk):
    def __init__(self):
        super().__init__()
        self.rqCovid = rq.get('https://covid19.th-stat.com/json/covid19v2/getTodayCases.json').json()
        self.thtop= ['ยอดผู้ป่วยสะสม','ยอดผู้รักษาหายแล้ว','ยอดผู้ได้รับการรักษา','ยอดผู้เสียชีวิต','ผู้ป่วยรายใหม่','ผู้รักษาหายแล้วรายใหม่','ผู้ได้รับการรักษารายใหม่','ผู้เสียชีวิตรายใหม่','วันที่','พัฒนาโดย']
        self.rqCovid = {v:self.rqCovid[i] for (i,v) in zip(self.rqCovid,self.thtop)}
        self.geometry('400x500')
        for row,key in zip(range(0,len(self.rqCovid.keys())),self.rqCovid):
            Label(self,text=key,font='consolas 15',bg='#ffc107').grid(row=row,column=0,sticky='ew')
            Label(self,text=self.rqCovid[key],font='consolas 15',background='#ddc079').grid(row=row,column=1,sticky='ew')
if __name__ == '__main__':
    # CoApp().mainloop()
    rqCovid = rq.get('https://covid19.th-stat.com/json/covid19v2/getTodayCases.json')
    print(rqCovid)