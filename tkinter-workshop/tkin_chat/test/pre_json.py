import json 
import ast
dic_sam = {'name':'User','text':'hello world'}
# dic_sam = dict(json.loads(dic_sam))
m = str.encode(str(dic_sam))
print('text' in dic_sam)
print(ast.literal_eval(m.decode('utf-8'))['name'])