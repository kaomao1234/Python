import os
"""
kv_files กับ python_files = เก็บ path และ importmodule object สำหรับทำ reload
"""
kv_files = set()
python_files = set()

for root, dirs, files in os.walk(os.getcwd()):
    if 'env' not in root:
        for file in files:
            if file.endswith('.kv'):
                kv_files.add(os.path.join(root, file))
            elif file.endswith('.py') and file != "main.py":
                path = os.path.join(root, file)
                path_splited = path.replace(".py","").split("\\")
                index_lib = path_splited.index("lib")
                module = ".".join(path_splited[index_lib+1:])
                python_files.add(__import__(module, fromlist=['']))
            # lib. is a way to add an import object another way that doesn't have to be in the lib package
                # to prevent import errors
