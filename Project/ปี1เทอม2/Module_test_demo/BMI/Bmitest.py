from tkinter import *
from PIL import Image, ImageTk
bmi = 26
b_group = 'AB'
# window = Toplevel()
# if bmi < 18.5:
#     diag = 'ผอมเกิน'
# elif 18.5 <= bmi <= 25:
#     diag = 'ปกติ'
# elif 25 < bmi <= 30:
#     diag = 'อ้วน'
# elif bmi > 30:
#     diag = 'อ้วนมาก'
# img = PhotoImage(file=f'{diag}.png')
# Label(window, image=img).grid(row=0, column=1)
# Label(window, text='BMI', font='consolas 25',bg='seagreen1').grid(
#     row=0, column=0,sticky='nsew')
# shall_g = ['เครื่องดื่ม', 'ผลไม้', 'อาหาร',
#         'อาหารที่ควรงด', 'อาหารที่ควรทานบ่อยๆ']
# for i, e in zip(shall_g,range(1,6)):
#     Label(window, text=i, font='consolas 25',bg='snow3').grid(
#         row=e, column=0, sticky='wnes')
# shall_img = {'drink': PhotoImage(file=f'{b_group} เครื่องดื่ม.png'), 'fruit': PhotoImage(
#     file=f'{b_group} ผลไม้.png'), 'food': PhotoImage(file=f'{b_group} อาหาร.png'), 'd_food': PhotoImage(file=f'{b_group} อาหารที่ควรงด.png')
#             , 'f_food': PhotoImage(file=f'{b_group} อาหารที่ควรทานบ่อยๆ.png')}
# for i,e in zip(shall_img,range(1,6)):
#     Label(window, image=shall_img[i],bg='lemonchiffon').grid(row=e, column=1, sticky='nwe')
def conclud_bmi(bmi,b_group):
    window = Tk()
    if bmi < 18.5:
        diag = 'ผอมเกิน'
    elif 18.5 <= bmi <= 25:
        diag = 'ปกติ'
    elif 25 < bmi <= 30:
        diag = 'อ้วน'
    elif bmi > 30:
        diag = 'อ้วนมาก'
    img = PhotoImage(file=f'{diag}.png')
    Label(window, image=img).grid(row=0, column=1)
    Label(window, text='BMI', font='consolas 25',bg='seagreen1').grid(
        row=0, column=0,sticky='nsew')
    shall_g = ['เครื่องดื่ม', 'ผลไม้', 'อาหาร',
            'อาหารที่ควรงด', 'อาหารที่ควรทานบ่อยๆ']
    for i, e in zip(shall_g,range(1,6)):
        Label(window, text=i, font='consolas 25',bg='snow3').grid(
            row=e, column=0, sticky='wnes')
    shall_img = {'drink': PhotoImage(file=f'{b_group} เครื่องดื่ม.png'), 'fruit': PhotoImage(
        file=f'{b_group} ผลไม้.png'), 'food': PhotoImage(file=f'{b_group} อาหาร.png'), 'd_food': PhotoImage(file=f'{b_group} อาหารที่ควรงด.png')
                , 'f_food': PhotoImage(file=f'{b_group} อาหารที่ควรทานบ่อยๆ.png')}
    for i,e in zip(shall_img,range(1,6)):
        Label(window, image=shall_img[i],bg='lemonchiffon').grid(row=e, column=1, sticky='we')
    window.mainloop()
conclud_bmi(bmi=bmi,b_group=b_group)
