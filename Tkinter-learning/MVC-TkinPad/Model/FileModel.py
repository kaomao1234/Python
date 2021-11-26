from tkinter.filedialog import asksaveasfilename
from View.AskSaveChangeView import AskSaveChangeView
from tkinter.filedialog import *
from tkinter import *
import os


class FileModel:
    def __init__(self, controller):
        self.controller = controller
        self.textArea: Text = self.controller.mainFrame.textBar.textArea

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
