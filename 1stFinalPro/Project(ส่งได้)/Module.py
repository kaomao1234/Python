import csv
import os
from datetime import datetime, date
from tkinter import messagebox
from tkinter import *
now = datetime.now()
now_day = now.strftime("%d/%m/%Y")
now_hours = now.strftime("%H:%M:%S")
directory = 'DataFolder'
current_path = os.getcwd()+f'/{directory}'
record_read = os.path.join(current_path, 'LoginRecord.csv')
registry_read = os.path.join(current_path, 'RegistryData.csv')

try:
    locate_dir = os.getcwd()
    path = os.path.join(locate_dir, directory)
    os.mkdir(path)
    with open(record_read, mode='a', newline='', encoding='utf8') as c_record:
        record_header = csv.DictWriter(
            c_record, fieldname=['ชื่อผู้ใช้', 'รหัสผ่าน', 'วัน/เดือน/ปี', 'เวลา'])
        record_header.writeheader()
    with open(registry_read, mode='a', newline='', encoding='utf8') as c_re:
        re_header = csv.DictWriter(
            c_re, [
                'ชื่อ', 'นามสกุล', 'ชื่อผู้ใช้', 'รหัสผ่าน', 'เวลา', 'วัน/เดือน/ปี'])
        re_header.writeheader()
except:
    pass


def LessUserOrPassword(user, password, confirm):
    if len(user) < 8 or len(password) < 8 or len(confirm) < 8:
        messagebox.showerror(
            'Error', 'ชื่อผู้ใช้หรือรหัสผ่านตวรจะมีตั้งแต่8ตัวอัการขึ้นไป')
    elif (confirm != password) and (len(password) != 0 or len(confirm) != 0):
        messagebox.showerror('Error', 'กรูณาใส่รหัสผ่านให้ตรงกัน')
    else:
        return True


def check_drug(drug_name, disease_name, drug_quantity):
    if drug_name == '' or disease_name == '' or drug_quantity == '':
        messagebox.showerror('Error', 'กรุณากรอกข้อมูลให้ครบ')
    else:
        return True


def CheckLogin(user, password):
    with open(registry_read, mode='r', newline='', encoding='utf8') as f:
        d_login = csv.DictReader(f)
        try:
            for i in d_login:
                user = str(user).replace(' ', '')
                password = str(password).replace(' ', '')
                if user == i['ชื่อผู้ใช้'] and password == i['รหัสผ่าน']:
                    return True
            raise Exception('User or Password not in Data login')
        except:
            messagebox.showerror('Error', 'ไม่พบชื่อผู้ใช้หรือรหัสผ่านนี้')


def sn_upData(name, last_name, user, password):
    if name == '' or last_name == '':
        messagebox.showerror('Error', 'กรุณากรอกข้อมูลให้ครบ')
    else:
        registry = ['ชื่อ', 'นามสกุล', 'ชื่อผู้ใช้',
                    'รหัสผ่าน', 'เวลา', 'วัน/เดือน/ปี']
        get_registry = [name, last_name, user, password, now_hours, now_day]
        map_registry = {e: get_registry[i] for i, e in enumerate(registry)}
        with open(registry_read, mode='r+', newline='', encoding='utf8') as open_sign:
            check_suser = csv.DictReader(open_sign, fieldnames=[
                'ชื่อ', 'นามสกุล', 'ชื่อผู้ใช้', 'รหัสผ่าน', 'เวลา', 'วัน/เดือน/ปี'])
            same_user = list(check_suser)
            sign_file = csv.DictWriter(open_sign, fieldnames=[
                'ชื่อ', 'นามสกุล', 'ชื่อผู้ใช้', 'รหัสผ่าน', 'เวลา', 'วัน/เดือน/ปี'])
            a = list(filter(lambda a: a['ชื่อผู้ใช้'] == user, same_user))
            if len(a) > 1:
                messagebox.showerror('Error', 'ชื่อผู้ใช้นี้ถูกใช้ไปแล้ว')
            else:
                sign_file.writerows([map_registry])


def stamp_login(user, password):
    stm = ['ชื่อผู้ใช้', 'รหัสผ่าน', 'วัน/เดือน/ปี', 'เวลา']
    stm_get = [user, password, now_day, now_hours]
    stm_dict = {e: stm_get[i] for i, e in enumerate(stm)}
    with open(record_read, mode='a', newline='', encoding='utf8') as f:
        record_csv = csv.DictWriter(
            f, ['ชื่อผู้ใช้', 'รหัสผ่าน', 'วัน/เดือน/ปี', 'เวลา'])
        record_csv.writerows([stm_dict])


def eat_med(list_time):
    messagebox.showinfo('เตือน', 'กินยาได้แล้ว')
    list_time.delete(0)


def nofication(drug_noficate, **var):
    time_real = datetime.now()
    var['text_time']['text'] = time_real.strftime("%H:%M:%S")
    if time_real.strftime("%H:%M") == var['list_time'].get(0):
        time = '{}'.format(time_real.strftime("%H:%M"))
        messagebox.showinfo('เตือน', f'กินยา{drug_noficate[time]}แล้ว')
        var['list_time'].delete(0)
        var['sort_clock'].pop(0)
    var['root'].after(1000, lambda: nofication(drug_noficate=drug_noficate, text_time=var['text_time'],
                      root=var['root'], list_time=var['list_time'], sort_clock=var['sort_clock']))


def drug_Person(data):
    with open(record_read, mode='r', encoding='utf8') as f:
        read = csv.DictReader(
            f, fieldnames=['ชื่อผู้ใช้', 'รหัสผ่าน', 'วัน/เดือน/ปี', 'เวลา'])
        all_user = list(read)
        now_login = all_user[len(all_user)-1]
    with open(registry_read, mode='r', encoding='utf8') as redata:
        all_name = csv.DictReader(redata, fieldnames=[
                                  'ชื่อ', 'นามสกุล', 'ชื่อผู้ใช้', 'รหัสผ่าน', 'เวลา', 'วัน/เดือน/ปี'])
        name = list(all_name)
        infor_name = list(
            filter(lambda s: s['ชื่อผู้ใช้'] == now_login['ชื่อผู้ใช้'], name))
        sname, slname = '{} {}'.format(
            infor_name[0]['ชื่อ'], infor_name[0]['นามสกุล']).split(' ')
    file_name = f'{sname} {slname}.csv'
    select_save = os.path.join(current_path, file_name)
    with open(select_save, mode='a+', encoding='utf8', newline='') as f:
        readcsv = csv.DictReader(f)
        if {'โรค': 'โรค', 'ชื่อยา': 'ชื่อยา', 'เวลาทานยา': 'เวลาทานยา', 'ปริมาณยา': 'ปริมาณยา'}  in list(readcsv):
            writecsv = csv.DictWriter(
                f, fieldnames=['โรค', 'ชื่อยา', 'เวลาทานยา', 'ปริมาณยา'])
            writecsv.writerows(data)
        else:
            writecsv = csv.DictWriter(
                f, fieldnames=['โรค', 'ชื่อยา', 'เวลาทานยา', 'ปริมาณยา'])
            writecsv.writeheader()
            writecsv.writerows(data)


def conclud_bmi(bmi, b_group):
    window = Toplevel()
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
    Label(window, text='BMI', font='consolas 25', bg='seagreen1').grid(
        row=0, column=0, sticky='nsew')
    shall_g = ['เครื่องดื่ม', 'ผลไม้', 'อาหาร',
               'อาหารที่ควรงด', 'อาหารที่ควรทานบ่อยๆ']
    for i, e in zip(shall_g, range(1, 6)):
        Label(window, text=i, font='consolas 25', bg='snow3').grid(
            row=e, column=0, sticky='wnes')
    shall_img = {'drink': PhotoImage(file=f'{b_group} เครื่องดื่ม.png'), 'fruit': PhotoImage(
        file=f'{b_group} ผลไม้.png'), 'food': PhotoImage(file=f'{b_group} อาหาร.png'), 'd_food': PhotoImage(file=f'{b_group} อาหารที่ควรงด.png'), 'f_food': PhotoImage(file=f'{b_group} อาหารที่ควรทานบ่อยๆ.png')}
    for i, e in zip(shall_img, range(1, 6)):
        Label(window, image=shall_img[i], bg='lemonchiffon').grid(
            row=e, column=1, sticky='we')
    window.mainloop()