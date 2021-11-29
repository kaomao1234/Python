import ttkbootstrap as ttk
from tkinter import *
from tkinter import font
from pprint import pprint
from functools import partial


class FormatModel:
    def __init__(self, controller):
        self.controller = controller
        self.defaultFont = self.controller.mainFrame.textBar.defaultFont
        self.textArea: Text = self.controller.mainFrame.textBar.textArea
        self.pop_up = Toplevel(controller)
        self.pop_up.wm_withdraw()
        self.pop_up.protocol("WM_DELETE_WINDOW", self.close)
        self.pop_up.title('Font')
        self.pop_up.resizable(0, 0)
        self.fontblock = FontBlock(controller, self, self.pop_up)
        self.styleblock = StyleBox(controller, self, self.pop_up)
        self.sizeblock = SizeBox(controller, self, self.pop_up)
        self.sampleText = ttk.Labelframe(
            self.pop_up, text='Sample', height=80, width=250)
        self.text = ttk.Label(self.sampleText, text='AaBbYyZz',
                              anchor='n', font=tuple(self.defaultFont.values()))
        self.ok_btn = ttk.Button(
            self.pop_up, text='OK', bootstyle='primary', width=15, command=self.ok_click)
        self.cancel_btn = ttk.Button(
            self.pop_up, text='Cancel', bootstyle='primary', width=15, command=self.close)

    def ok_click(self):
        self.textArea.configure(font=tuple(self.defaultFont.values()))
        self.close()

    def close(self):
        for i in [self.fontblock, self.styleblock, self.sizeblock]:
            i.selectVar.set('')
            i.tree.selection_remove(tuple(i.id.values()))
            i.tree.yview_moveto(0)
        self.pop_up.wm_withdraw()

    def wrap_text(self, var):
        if var.get():
            self.textArea.configure(wrap='word')
        else:
            self.textArea.configure(wrap='none')

    def fontText(self):
        self.text.place(x=0, y=0, height=75, width=245)
        self.fontblock.grid()
        self.styleblock.grid()
        self.sizeblock.grid()
        self.sampleText.grid(columnspan=3, sticky='e', padx=10, pady=10)
        self.ok_btn.grid(row=2, column=1, sticky='e', padx=10, pady=10)
        self.cancel_btn.grid(row=2, column=2, sticky='w', padx=10, pady=10)
        self.pop_up.wm_deiconify()

    def autoScroll_move(self, instance, e):
        rangeScroll = 0.003389830508474576
        text = instance.selectVar.get()
        if text.isdigit() and instance.tree.winfo_name() == 'size':
            self.defaultFont.update({'size': int(text)})
            self.text.configure(font=tuple(self.defaultFont.values()))
        try:
            certain_element = list(
                filter(lambda s: str(s)[0] == text[0], instance.elementLst))
            getId = [instance.id[str(i)] for i in certain_element]
            first_index = instance.elementLst.index(certain_element[0])
            instance.tree.yview_moveto(first_index*rangeScroll)
            instance.tree.selection_set(getId)
        except Exception as e:
            instance.tree.yview_moveto(0)
            instance.tree.selection_remove(tuple(instance.id.values()))

    def on_click(self, instance, e: Event):
        value = e.widget.item(e.widget.focus())['text']
        key = e.widget.winfo_name()
        self.defaultFont.update({key: value})
        self.text.configure(font=tuple(self.defaultFont.values()))
        instance.selectVar.set(value)
        if key == 'font':
            for i in self.styleblock.elementLst:
                self.styleblock.tree.tag_configure(
                    i, font=(value, 10, i.lower()))


class FontBlock(ttk.Frame):
    def __init__(self, controller, model, master):
        super().__init__(master=master)
        self.model = model
        self.selectVar = StringVar()
        self.elementLst = sorted(
            (list(map(lambda s: s.lower(), font.families()))))
        self.id = {}
        self.treeScroll = ttk.Scrollbar(self)
        self.search = ttk.Entry(
            self, textvariable=self.selectVar, font=('consolas', 10))
        self.tree = ttk.Treeview(
            self, yscrollcommand=self.treeScroll.set, show='tree', name='font', height=7)
        self.treeScroll.configure(command=self.tree.yview)
        self.pinTreeFont()

    def pinTreeFont(self):
        for i in self.elementLst:
            fontID = self.tree.insert(
                '', 'end', text=i, tag=i)
            self.id.update({i: fontID})
            self.tree.tag_configure(i, font=(i, 10))
        ttk.Label(self, text='Font:', font=('consolas', 10)).grid(
            row=0, column=0, columnspan=2, sticky='ew')
        self.search.grid(row=1, column=0, columnspan=2, sticky='ew')
        self.search.focus()
        self.tree.grid(row=2, column=0)
        self.treeScroll.grid(row=2, column=1, sticky='ns')

    def grid(self):
        self.search.bind("<KeyRelease>", partial(
            self.model.autoScroll_move, self))
        self.tree.bind('<ButtonRelease-1>',
                       partial(self.model.on_click, self))
        super().grid(row=0, column=0, pady=10, padx=10)


class StyleBox(ttk.Frame):
    def __init__(self, controller, model, master):
        super().__init__(master=master)
        self.model = model
        self.id = {}
        self.elementLst = ['normal', 'italic', 'bold',
                           'bold italic', 'roman', 'underline', 'overstrike']
        self.selectVar = StringVar()
        self.search = ttk.Entry(
            self, textvariable=self.selectVar, font=('consolas', 10))
        self.treeScroll = ttk.Scrollbar(self)
        self.tree = ttk.Treeview(
            self, yscrollcommand=self.treeScroll.set, show='tree', name='style', height=7)
        self.treeScroll.configure(command=self.tree.yview)
        self.pinTreeStyle()

    def pinTreeStyle(self):
        for i in self.elementLst:
            styleID = self.tree.insert(
                '', 'end', text=i, tag=i)
            self.id.update({i: styleID})
            self.tree.tag_configure(i, font=('arial', 10, i.lower()))
        ttk.Label(self, text='Style:', font=('consolas', 10)).grid(
            row=0, column=0, columnspan=2, sticky='ew')

        self.search.grid(row=1, column=0, columnspan=2, sticky='ew')
        self.search.focus()
        self.tree.grid(row=2, column=0)
        self.treeScroll.grid(row=2, column=1, sticky='ns')

    def grid(self):
        self.search.bind("<KeyRelease>", partial(
            self.model.autoScroll_move, self))
        self.tree.bind('<ButtonRelease-1>',
                       partial(self.model.on_click, self))
        super().grid(row=0, column=1, pady=10, padx=10)


class SizeBox(ttk.Frame):
    def __init__(self, controller, model, master):
        super().__init__(master=master)
        self.model = model
        self.id = {}
        self.elementLst = [8, 9, 10, 11, 12, 14, 16,
                           18, 20, 22, 24, 26, 28, 36, 48, 72]
        self.selectVar = StringVar()
        self.treeScroll = ttk.Scrollbar(self)
        self.tree = ttk.Treeview(
            self, yscrollcommand=self.treeScroll.set, show='tree', name='size', height=7)
        self.treeScroll.configure(command=self.tree.yview)
        self.search = ttk.Entry(
            self, textvariable=self.selectVar, font=('consolas', 10))
        self.pinTreeSize()

    def pinTreeSize(self):
        for i in self.elementLst:
            sizeID = self.tree.insert('', 'end', text=i, tag=i)
            self.id.update({str(i): sizeID})
        ttk.Label(self, text='Size:', font=('consolas', 10)).grid(
            row=0, column=0, columnspan=2, sticky='ew')
        self.search.grid(row=1, column=0, columnspan=2, sticky='ew')
        self.search.focus()
        self.tree.grid(row=2, column=0)
        self.treeScroll.grid(row=2, column=1, sticky='ns')

    def grid(self):
        self.search.bind("<KeyRelease>", partial(
            self.model.autoScroll_move, self))
        self.tree.bind('<ButtonRelease-1>',
                       partial(self.model.on_click, self))
        super().grid(row=0, column=2, pady=10, padx=10)
