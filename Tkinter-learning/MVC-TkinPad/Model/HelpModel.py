from tkinter import *
import ttkbootstrap as ttk
import os
class HelpModel(Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.container = parent
        self.geometry('475x320')
        self.resizable(0, 0)
        self.title('Tkinpad')
        self.transient(self.container)
        pc_name_f = ttk.LabelFrame(
            self, text='Pc name', bootstyle='primary')
        ttk.Label(pc_name_f, text=os.getenv('COMPUTERNAME'), font=(
            'consolas', 20, 'normal'), foreground='white', bootstyle='inverse-primary').pack(fill=X)
        pc_name_f.pack(fill=X)
        library_f = ttk.LabelFrame(
            self, text='Libary:', bootstyle='primary')
        ttk.Label(library_f, text='tkinter\nttkbootstrap\nos\nre\ntime', font=(
            'consolas', 20, 'normal'), foreground='white', bootstyle='inverse-primary').pack(fill=X)
        library_f.pack(fill=X)
        credit_f = ttk.LabelFrame(
            self, text='Developer', bootstyle='primary')
        ttk.Label(credit_f, text='Kaomao นอนเถอะ', font=('consolas', 20, 'normal'), foreground='white',
                  bootstyle='inverse-primary').pack(fill='both')
        credit_f.pack(fill=BOTH)
        ttk.Button(self, text='OK', bootstyle='warning',
                   command=self.destroy).pack(fill=X)