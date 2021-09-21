# num_input = int(input())
# for i in range(num_input):
#     a = "/"+("__"*i)+"\ ".strip(' ')
#     a = a.center(num_input*2)
#     print(a)
num_input = int(input())
print("\n".join([("/"+("__"*i if i == num_input-1 else "  "*i)+"\ ".replace(' ','')).center(num_input*2) for i in range(num_input)]))
# print(len('________________'))
# """
#     /\
#    /  \
#   /    \
#  /      \
# /________\
# """