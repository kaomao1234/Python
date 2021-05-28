from tkinter import *
from tkinter import font
from tkinter import ttk
from ttkbootstrap import Style
import tkinter as tk


def ball(e):
    sum_show['text'] = f'{eval(summation.get())}'


parent = Tk()
theme = Style().master
summation = StringVar()
space = ttk.Entry(theme, textvariable=summation,
                  style='primary.TEntry', font=('Helvetica', 20))
space.grid(row=0, column=0)
sum_show = Label(theme, text='', font=('Helvetica', 20))
btn = ttk.Label(theme, text='Enter', style='success.Outline.TButton')
btn.bind('<Button-1>',ball)
btn.grid(row=1, column=0)
sum_show.grid(row=2, column=0)
parent.mainloop()