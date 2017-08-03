#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 18:02

# import random
# for i in range(5):
#     print(random.randint(1, 5))

# import sys
# while True:
#     print("fde")
#     a = input()
#     if a =="exit":
#         sys.exit()
#     print("fdf")

def spam(f):
    try:
        return  1/f
    except ZeroDivisionError:
        print('除数不能为0')

print(spam(3))