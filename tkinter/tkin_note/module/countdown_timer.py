from tkinter import *
from tkinter import ttk


def set_time():
    p = Label(f1, text=Set.get())
    p.pack()
    p.after(0, lambda: time_count(int(p['text']), p))


def time_count(time, s):
    if time > 0:
        s['text'] = time
        root.after(1000, lambda: time_count(time-1, s))
    else:
        s.pack_forget()


root = Tk()
Set = IntVar()
Label(root, text='Title', font='consolas 20').pack()
Entry(root, textvariable=Set).pack()
f1 = Frame(root, background='white')
f1.pack()
Button(root, text='+', font='consolas 20', command=set_time).pack()
root.mainloop()
