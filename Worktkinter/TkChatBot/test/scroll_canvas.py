import tkinter as tk 
from tkinter import ttk
from tkinter.constants import BOTH, BOTTOM, LEFT, X
from ttkbootstrap import Style
def framewidth(event):
    cw = event.width
    canvas.itemconfig(c_crew,width=event.width)
    # parent.geometry(f'{cw}x{event.height}')
    
st = Style()
parent = st.master
canvas = tk.Canvas(parent)
scroll_y = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)

frame = tk.Frame(canvas)
# group of widgets
t_frame = tk.Frame(frame,background='red')
for i in range(20):
    tk.Button(t_frame, text='label %i' % i,justify='center').pack()
# put the frame in the canvas
t_frame.pack(fill=BOTH,expand=1)
c_crew = canvas.create_window((0,0), anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
canvas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox('all'), 
                 yscrollcommand=scroll_y.set)
canvas.bind('<Configure>',framewidth)
frame.bind('<Configure>',lambda s : canvas.configure(scrollregion=canvas.bbox('all')))
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')
parent.mainloop()