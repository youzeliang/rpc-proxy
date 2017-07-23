#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 15:24
# n = 100
# sum = 0
# conter = 0
# while conter<100:
#     sum = sum +conter
#     conter+=1
# print(sum)
#
# a = 1
# b = 1
# print(id(a))


sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Baidu":
        print("百度")
        break
    print(site)
else:
    print("没有循环数据")
print("完成循环")

for i in range(6):  #内置函数
    print(i)