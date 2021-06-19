import json 
import ast
dic_sam = 'name'
# dic_sam = dict(json.loads(dic_sam))
print(type(ast.literal_eval(str(dic_sam))))