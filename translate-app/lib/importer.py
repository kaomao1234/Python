import re
import os

"""
kv_files กับ python_files = เก็บ path และ importmodule object สำหรับทำ reload
"""
kv_files = set()
python_files:set[__import__] = set()
path = os.path.join(os.getcwd(), "lib")
if path.count("lib") > 1:
    path = os.getcwd()

except_file = [
    "main.py",
    'file_path.py'
]

for root, dirs, files in os.walk(path):

    for file in files:

        if file.endswith(".kv"):
            kv_files.add(os.path.join(root, file))
        elif file.endswith(".py") and file not in except_file:
            split_path = root.split("\\")
            index_of_lib = split_path.index("lib")
            try:
                split_path = split_path[index_of_lib+1:]
                split_path.append(file.removesuffix(".py"))
                for_import_path = ".".join(split_path)
                python_files.add(__import__(for_import_path,fromlist=['']))
            except:
                split_path = split_path[index_of_lib:]
                split_path.append(file.removesuffix(".py"))
                for_import_path = ".".join(split_path)
                python_files.add(__import__(for_import_path,fromlist=['']))
