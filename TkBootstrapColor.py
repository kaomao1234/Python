from tkinter import *
from ast import *
import re


class ColorSample(Tk):
    def __init__(self):
        super().__init__()
        self.color = {'blue':       '#467FD0',
                      'indigo':     '#6610f2',
                      'purple':     '#7c69ef',
                      'pink':       '#e83e8c',
                      'red':        '#df4759',
                      'orange':     '#fd9644',
                      'yellow':     '#ffc107',
                      'green':      '#42ba96',
                      'teal':       '#20c997',
                      'cyan':       '#17a2b8',
                      'light-blue': '#69d2f1',
                      'white': '#FFFFFF',
                      'gray-base': '#181b1e',
                      'gray-100': '#F9FBFD',
                      'gray-200': '#F1F4F8',
                      'gray-300': '#D9E2EF',
                      'gray-400': '#C6D3E6',
                      'gray-500': '#ABBCD5',
                      'gray-600': '#869AB8',
                      'gray-700': '#506690',
                      'gray-800': '#384C74',
                      'gray-900': '#1B2A4E',
                      'black': '#161C2D'}
        self.resizable(0, 0)
        for i in self.color:
            Label(self, text=i, background=self.color[i], font='consolas 15', width=15).grid(
                sticky='ew', column=0, row=list(self.color.keys()).index(i))
            Label(self, text=self.color[i], font='consolas 15', width=15).grid(
                sticky='ew', column=1, row=list(self.color.keys()).index(i))

    def regColor(self, m):
        m = m.split(';')
        m = [i.replace(' !default', '').replace(
            '$', '').replace('\n', '') for i in m]
        m = {i.split(': ')[0]: i.split(' : ')[1] for i in m}


if __name__ == '__main__':
    ColorSample().mainloop()
    # print([int(input('input h'))*int(input('input b'))for i in range(0,5)])
