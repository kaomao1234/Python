from pyflowchart import Flowchart
with open('main.py',encoding='utf8') as f:
     code = f.read()
fc = Flowchart.from_code(code)
print(fc.flowchart())
