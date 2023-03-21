import os

from views.home_page.home_page import HomePage
from views.login_page.login_page import LoginPage
from views.setting_page.setting_page import SettingPage

"""
kvs กับ pys = ตัวแปรเก็บ path และ module object สำหรับทำ reload
"""
kvs = set()
pys = set()

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.kv'):
            kvs.add(os.path.join(root, file))
        elif file.endswith('.py') and file != "main.py":
            path = os.path.join(root,file)
            module_path = f'{path}'.replace(os.getcwd(),"").replace("\\",".").replace(".py","")[1:]
            pys.add(__import__(module_path,fromlist=['']))
            # lib. เป็นการเพิ่ม import object อีกแบบนึงไม่จำเป็นต้องเป็น lib ป้องกันการ import error
            pys.add(__import__(f"lib.{module_path}",fromlist=['']))
pages = {
    "home_page": HomePage,
    "login_page":LoginPage,
    'setting_page':SettingPage
}