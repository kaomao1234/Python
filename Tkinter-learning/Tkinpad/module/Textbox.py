from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
def resizefont(e):
    global defaulfont_size
    if e.delta < 0:
        defaulfont_size -= 1
    else:
        defaulfont_size += 1
    Notetext['font'] = 'consolas {}'.format(defaulfont_size) 
    print(Notetext.get('1.0',END))


def fixNotetext_size(e):
    # print(f'frame size is : {parent_Text.winfo_width()},{parent_Text.winfo_height()}\nWindow size is {root.winfo_width()},{root.winfo_height()}')
    Notetext.place_configure(
        width=parent_Text.winfo_width(), height=parent_Text.winfo_height())


root = Tk()
theme = Style()
defaulfont_size = 11
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
parent_Text = Frame(root, background='yellow')
parent_Text.grid(row=0, column=0, sticky='nesw')
yscroll = Scrollbar(root) 
xscroll = Scrollbar(root,orient=HORIZONTAL)
yscroll.grid(row=0, column=1, sticky='ns')
xscroll.grid(row=1,column=0,sticky='ew')
root.bind('<Configure>', fixNotetext_size)
Notetext = Text(root, wrap='none', background='yellow',
                font='consolas 11', yscrollcommand=yscroll.set,xscrollcommand=xscroll.set)
Notetext.bind('<Control-MouseWheel>', resizefont)
yscroll.configure(command=Notetext.yview)
xscroll.configure(command=Notetext.xview)
root.mainloop()
