import os
from xlsxwriter import *
from pandas import *
from styleframe import StyleFrame

# def add(data):
#     dataframe = DataFrame(data)
#     writer = ExcelWriter('simple_data.xlsx', engine='xlsxwriter')
#     dataframe.to_excel(writer, sheet_name='หน้าที่1', index=False)
#     writer.save()


# data = {'Data': [1,'line3\r\nline4',], 'locate': [1,'line3\r\nline4',]}
# while True:
#     try:
#         add_data = int(input('type in Data:\n---'))
#         add_locate = int(input('type in locate:\n---'))
#         data['Data'].append(add_data)
#         data['locate'].append(add_locate)
#         add(data)
#     except:1
#         break 
save_path = os.getcwd()+f'/TestBase'
select_save = os.path.join(save_path,'simple_data.xlsx')
rd = read_excel(r'{}'.format(select_save))
df = DataFrame({'Data': [7,'line5\nline6',], 'locate': [8,'line1\nline4']})
result = concat([rd,df])
writer = ExcelWriter('simple_data.xlsx', engine='xlsxwriter')
result.to_excel(writer,sheet_name='หน้าที่1',index=False)
writer.save()

