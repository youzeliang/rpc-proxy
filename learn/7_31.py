#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 16:14
# while True:
#     print("ds")
#     name = input()
#     if name == "a":
#         break
#     print("b")

# while True:
#     print("a")
#     name = input()
#     if name !="b":
#         continue
#     print("c")
#     password = input()
#     if password != "d":
#         break
# print("e")

total = 0
for num in range(101):
    total = num+total
print(total)