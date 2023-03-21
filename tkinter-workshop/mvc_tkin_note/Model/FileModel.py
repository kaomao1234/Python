from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import *
import ttkbootstrap as ttk
from tkinter import *
import os


class FileModel:
    def __init__(self, controller):
        self.controller = controller
        self.textArea: Text = self.controller.baseFrame.textBar.textArea

    def new_file(self):
        if self.controller.wm_title() != 'Untitle - TkNotepad' and self.textArea.get('1.0', 'end') == '\n':
            self.controller.title('Untitle - TkNotepad')
            self.textArea.delete('1.0', 'end')
        elif self.textArea.get('1.0', 'end') != '\n':
            self.ask_to_change()

    def open(self):
        ask_path = askopenfilename(
            initialdir='/', title='Open file', filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        file = open(ask_path, 'r')
        self.controller.title('{}'.format(ask_path.split('/')[-1]))
        self.textArea.delete('1.0', END)
        self.textArea.insert(END, file.read())
        file.close()

    def save(self):
        path = os.path.join(os.getcwd(), f'{self.controller.wm_title()}.txt')
        file = open(path, mode='w+')
        file.write('\n'.join(self.textArea.get('1.0', 'end').splitlines()))
        file.close()

    def save_as(self):
        ask_path = asksaveasfilename(
            initialdir='/', title='Save as', filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        file = open(ask_path+'.txt', 'w+')
        file.write(self.textArea.get('1.0', 'end'))
        file.close()

    def ask_to_change(self):
        pop_up = Toplevel(self.controller)
        pop_up.resizable(0, 0)
        pop_up.transient(self.controller)
        pop_up.geometry('352x134')
        pop_up.title(self.controller.wm_title())
        AskSaveChangeView(self.controller, self, pop_up).pack()

    def destroy_top_level(self):
        self.textArea.delete('1.0', 'end')

class AskSaveChangeView(ttk.Frame):
    def __init__(self, controller, model,master):
        super().__init__(master=master)
        self.controller = controller
        self.master = master
        self.model = model
        ttk.Label(self, text='Do you want to save changes to \n{}?'.format(
            controller.wm_title()), font=('consolas', 13), bootstyle='default', anchor=CENTER).grid(row=0, column=0, columnspan=3)
        ttk.Button(self, text='Save',
                   bootstyle='outline-primary', command=self.save_btn).grid(row=1, column=0)
        ttk.Button(self, text="Don't save",
                   bootstyle='outline-primary', command=self.destroy_master).grid(row=1, column=1)
        ttk.Button(self, text="Cancel",
                   bootstyle='outline-primary', command=master.destroy).grid(row=1, column=2)

    def save_btn(self):
        self.model.save()
        self.master.destroy()

    def destroy_master(self):
        textArea:Text = self.controller.mainFrame.textBar.textArea
        textArea.delete('1.0', 'end')
        self.master.destroy()

    def pack(self):
        super().pack(expand=1, padx=10)
