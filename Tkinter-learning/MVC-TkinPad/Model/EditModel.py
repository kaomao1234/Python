import time
import ttkbootstrap as ttk
from functools import partial
from tkinter import *


class EditModel:
    def __init__(self, controller):
        self.controller = controller
        self.all_tagWord = []

    def stamp_time(self):
        textArea: Text = self.controller.mainFrame.textBar.textArea
        stamp_time = time.strftime('%H:%M %p %d/%m/%Y')
        last_index = textArea.index(INSERT)
        textArea.insert(last_index, stamp_time)

    def find_word(self):
        pop_up = Toplevel(self.controller)
        pop_up.protocol("WM_DELETE_WINDOW", partial(self.remove_tag, pop_up))
        pop_up.resizable(width=False, height=False)
        pop_up.title('Find...')
        pop_up.geometry('365x155')
        pop_up.transient(self.controller)
        FindFrame(self.controller, pop_up, self).pack(padx=20, pady=20)

    def add_tag(self, text_var: StringVar):
        textArea: Text = self.controller.mainFrame.textBar.textArea
        self.all_tagWord.clear()
        search_word = textArea.search(
            text_var.get(), '1.0', END)
        self.tagging(search_word, text_var, textArea)

    def remove_tag(self, container):
        textArea: Text = self.controller.mainFrame.textBar.textArea
        container.destroy()
        textArea.tag_remove("red_tag", "1.0", "end")

    def tagging(self, start, word, Text: Text):
        offset = '+%dc' % len(word.get())
        end = start + offset
        if start == '' or word.get() == '':
            return
        if (start, end) not in self.all_tagWord:
            self.all_tagWord.append((start, end))
        Text.tag_add('red_tag', start, end)
        search_word = Text.search(word.get(), end, END)
        self.tagging(search_word, word, Text)


class FindFrame(ttk.Frame):
    def __init__(self, controller, master, model):
        super().__init__(master=master)
        entry_var = StringVar()
        ttk.Label(self, text='Find what:', bootstyle='primary').grid(
            row=0, column=0, sticky='ns', pady=10, padx=10)
        ttk.Entry(self, textvariable=entry_var).grid(
            row=0, column=1, sticky='nsew', pady=10, padx=10)
        ttk.Button(self, text='Search', command=partial(model.add_tag, entry_var)).grid(
            row=0, column=2, sticky='nsew', pady=10, padx=10)
        ttk.Button(self, text='Cancel', command=model.remove_tag).grid(
            row=1, column=2, pady=10, padx=10)
