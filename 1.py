# -*- coding: utf-8 -*-
# @Time    : 2021-01-26 21:06
# @Author  : qlz
# @File    : 1.py
# @Software : PyCharm
# @function ：


import copy
'''
评测题目: 给你一个字符串，请将字符串处理成一些子串，保证这些子串都保持回文性。
//如 字符串 "abadb"，处理后输出如下
// [
//  ["a","b","a","d","b"],
//  ["aba","d","b"]
// ]
'''

leetcode

data = 'abadb'
mylist = []
new_list = []
for i in data:
   mylist.append(i)
   # mylist.append(',')

print(mylist)
for j in range(len(data)):
    data_1 = data.split('')
print('aaaa',data_1)
for i in range(len(mylist)-2):
    if data[i+1-1]==data[i+2]:
        data_tmp = data[i:i+3]
        # print(data_tmp)
        new_list.append(data_tmp)
    else:
        new_list.append(data[i+2])
print(new_list)







# new_mylist =[]
# num = len(data)
# print(num)
# for i in data:
#     mylist.append(i)
# print(mylist[2])
#
# num1 = int(num /2)
#
# print(num1)
# if num %2 ==1:
#     data_tmp = (mylist[num1])
#     data_left = mylist[0:num1].copy()
#     data_right = mylist[num1+1:num].copy()
#     data_centor = mylist[num1]
#
# print(data_left)
# print(data_right)
# print()
#
# new_mylist = new_mylist.append(data_left,)


