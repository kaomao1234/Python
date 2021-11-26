import time
import ttkbootstrap as ttk
from functools import partial
from tkinter import *
from tkinter import messagebox


class EditModel:
    def __init__(self, controller):
        self.controller = controller
        self.textArea: Text = self.controller.mainFrame.textBar.textArea
        self.tagIdx_list = []

    def stamp_time(self):
        stamp_time = time.strftime('%H:%M %p %d/%m/%Y')
        last_index = self.textArea.index(INSERT)
        self.textArea.insert(last_index, stamp_time)

    def find_word(self):
        pop_up = Toplevel(self.controller)
        pop_up.protocol("WM_DELETE_WINDOW", partial(self.remove_tag, pop_up))
        pop_up.resizable(width=False, height=False)
        pop_up.title('Find...')
        pop_up.geometry('365x155')
        pop_up.transient(self.controller)
        FindFrame(self.controller, pop_up, self).pack(padx=20, pady=20)

    def replace_word(self):
        pop_up = Toplevel(self.controller)
        pop_up.protocol("WM_DELETE_WINDOW", partial(self.remove_tag, pop_up))
        pop_up.resizable(width=False, height=False)
        pop_up.title('Replace...')
        pop_up.geometry('400x200')
        pop_up.transient(self.controller)
        ReplaceFrame(self.controller, pop_up, self).pack(padx=20, pady=20)

    def goto_line(self):
        pop_up = Toplevel(self.controller)
        pop_up.title('Go To Line')
        pop_up.geometry('300x130')
        pop_up.resizable(0, 0)
        GotoFrame(self.controller, pop_up, self).pack()

    def add_tag(self, text_var: StringVar):
        self.tagIdx_list.clear()
        self.search_all(self.textArea, text_var.get())
        for i in self.tagIdx_list:
            self.textArea.tag_add('red_tag', i[0], i[1])

    def remove_tag(self, container):
        container.destroy()
        self.textArea.tag_remove("red_tag", "1.0", "end")

    def replace_click(self, word, container):
        word = word.get()
        try:
            index_text = self.tagIdx_list.pop(0)
            self.textArea.tag_remove("red_tag", index_text[0], index_text[1])
            self.textArea.delete(index_text[0], index_text[1])
            self.textArea.insert(index_text[0], word)
            self.textArea.tag_add('red_tag', index_text[0], index_text[1])
        except:
            messagebox.showinfo(container.wm_title(),
                                'Cannot find {}'.format(f"'{word}'"))

    def replaceAll_click(self, word):
        word = word.get()
        for i in self.tagIdx_list:
            self.textArea.delete(i[0], i[1])
            self.textArea.insert(i[0], word)
            self.textArea.tag_add('red_tag', i[0], i[1])

    def search_all(self, Text: Text, word: str, start=None):
        if start == '':
            return
        elif start == None:
            self.search_all(Text, word, Text.search(word, '1.0', END))
        else:
            leng_word = f'+{len(word)}c'
            end = start+leng_word
            self.tagIdx_list.append((start, end))
            continue_search = Text.search(word, end, END)
            self.search_all(Text, word, continue_search)

    def typeNumber_check(self, event):
        entry = event.widget
        text = entry.get()
        if text.isdigit() is False:
            messagebox.showerror(
                'Unacceptable Charactor', 'You can only type a number here.')
            entry.delete(0, 'end')
            text = text[0:len(text)-1]
            entry.insert('end', text)

    def markPos_inText(self, frame):
        mark_num = int(frame.entry_var.get())
        if mark_num < int(self.textArea.index('end-1c')[0]) and mark_num > 0:
            self.textArea.mark_set('insert', f'{mark_num}.0')
            frame.getline.delete(0, END)
            frame.master.destroy()
        else:
            messagebox.showinfo(
                'Notepad - Goto Line', 'The line number is beyond the total number of lines')


class FindFrame(ttk.Frame):
    def __init__(self, controller, master, model: EditModel):
        super().__init__(master=master)
        entry_var = StringVar()
        ttk.Label(self, text='Find what:', bootstyle='primary').grid(
            row=0, column=0, sticky='ns', pady=10, padx=10)
        ttk.Entry(self, textvariable=entry_var).grid(
            row=0, column=1, sticky='nsew', pady=10, padx=10)
        ttk.Button(self, text='Search', command=partial(model.add_tag, entry_var)).grid(
            row=0, column=2, sticky='nsew', pady=10, padx=10)
        ttk.Button(self, text='Cancel', command=partial(model.remove_tag, master)).grid(
            row=1, column=2, pady=10, padx=10)


class ReplaceFrame(ttk.Frame):
    def __init__(self, controller, master, model: EditModel):
        super().__init__(master=master)
        replace_var = StringVar()
        find_var = StringVar()
        ttk.Label(self, text='Find what:', bootstyle='primary').grid(
            row=0, column=0, sticky='ns', pady=10, padx=10)
        ttk.Entry(self, textvariable=find_var, width=20).grid(
            row=0, column=1, sticky='ew', pady=10)
        ttk.Label(self, text='Replace with: ', style='primary.TLabel').grid(
            column=0, row=1, padx=10, sticky='ns')
        ttk.Entry(self, textvariable=replace_var, width=20).grid(
            row=1, column=1)
        ttk.Button(self, text='Find next', command=partial(model.add_tag, find_var)).grid(
            row=0, column=2, pady=25, padx=20)
        ttk.Button(self, text='Replace', command=partial(model.replace_click, replace_var, master)).grid(
            row=1, column=2)
        ttk.Button(self, text='Replace all', command=partial(model.replaceAll_click, replace_var)).grid(
            row=2, column=1, pady=10)
        ttk.Button(self, text='Cancel', command=partial(
            model.remove_tag, master)).grid(row=2, column=0, pady=10)


class GotoFrame(ttk.Frame):
    def __init__(self, controller, master, model: EditModel):
        super().__init__(master=master)
        self.entry_var = StringVar()
        ttk.Label(self, text='Line number:', justify=LEFT).pack(
            side=TOP, anchor=NW, padx=10, pady=10)
        self.getline = ttk.Entry(self, width=38,
                                 font='consolas 10', textvariable=self.entry_var)
        self.getline.bind('<KeyRelease>', model.typeNumber_check)
        self.getline.pack(padx=10, anchor=W)
        ttk.Button(self, text='Cancel',
                   command=master.destroy).pack(side=RIGHT, padx=10, pady=10)
        ttk.Button(self, text='Go to', command=partial(
            model.markPos_inText, self)).pack(side=RIGHT, padx=10, pady=10)
        self.getline.focus()