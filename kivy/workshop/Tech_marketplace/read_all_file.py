import os 
# print(os.listdir('lib/Screen_kv'))
# print(os.getcwd())
Classes = {os.path.join(os.getcwd(),'component',i,os.listdir(f'component/{i}')[0]) for i in os.listdir('component')}
print(Classes)