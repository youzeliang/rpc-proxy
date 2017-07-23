#!/usr/bin/env python
# -*- coding: utf-8 -*-
# # @Time    : 2017/7/23 16:08
# for letter in "Runoob":
#     if letter=='o':
#         continue
#     print("字母是",letter)
# var = 10
# while var>0:
#     var = var-1
#     if var ==6:
#         continue
#     print("",var)
# print("good")


for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        print(n, "是质数")
