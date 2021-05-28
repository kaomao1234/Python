# class Solution:
#     def twoSum(self, nums, target):
#         sum_num = {i: {j: i+j for j in nums if j != i}for i in nums}
#         ans = []
#         for i in sum_num:
#             for j in sum_num[i]:
#                 if sum_num[i][j] == target:
#                     ans.append(nums.index(i))
#         print(ans)
# Solution().twoSum([2, 7, 11, 15],22)
from tkinter import *

# ------------------------------------

# root = Tk()
# def tag_word():
#     pos_start = t.search(word.get(), '1.0', END)

#     # check if found the word
#     while pos_start:

#         # create end position by adding (as string "+5c") number of chars in searched word
#         pos_end = pos_start + offset

#         print(pos_start, pos_end) # 1.6 1.6+5c :for first `World`

#         # add tag
#         t.tag_add('red_tag', pos_start, pos_end)

#         # search again from pos_end to the end of text (END)
#         pos_start = t.search(word.get(), pos_end, END)
# #---

# t = Text(root)
# t.pack()

# t.insert(0.0, 'Hello World of Tkinter. And World of Python.')

# # create tag style
# t.tag_config("red_tag", foreground="red", underline=1)

# #---

# word = StringVar()
# Entry(root,textvariable=word).pack()
# Button(root,text='tag',command=tag_word).pack()
# # word length use as offset to get end position for tag
# offset = '+%dc' % len(word.get()) # +5c (5 chars)

# # search word from first char (1.0) to the end of text (END)


# #---
# root.mainloop()

# #------------------------------------
def tag_word(start):
    offset = '+%dc' % len(word.get()) 
    end = start+offset 
    if start == '' or word.get()=='':
        return
    sp_txt.tag_add('red_tag', start, end)
    tag_word(sp_txt.search(word.get(), end, END))
    
root = Tk()
word = StringVar()
sp_txt = Text(root)
sp_txt.pack()
Entry(root, textvariable=word, font=('consolas', 20)).pack()
Button(root, text='tag', font=('consolas', 20), command=lambda: tag_word(
    sp_txt.search(word.get(), '1.0', END))).pack() 
Button(root,text='clear',command=lambda : sp_txt.tag_remove("red_tag", "1.0", "end"),font=('consolas',20)).pack()
sp_txt.tag_configure("red_tag", foreground="red", underline=1)
root.mainloop()
