from tkinter import *
def tag_word(start):
    offset = '+%dc' % len(word.get()) 
    end = start+offset 
    if start == '' or word.get()=='':
        return
    sp_txt.tag_add('red_tag', start, end)
    tag_word(sp_txt.search(word.get(), end, END))
    
root = Tk()
word = StringVar()
sp_txt = Text(root)
sp_txt.pack()
Entry(root, textvariable=word, font=('consolas', 20)).pack()
Button(root, text='tag', font=('consolas', 20), command=lambda: tag_word(
    sp_txt.search(word.get(), '1.0', END))).pack() 
Button(root,text='clear',command=lambda : sp_txt.tag_remove("red_tag", "1.0", "end"),font=('consolas',20)).pack()
sp_txt.tag_configure("red_tag", foreground="red", underline=1)
root.mainloop()
