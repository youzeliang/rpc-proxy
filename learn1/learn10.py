#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 15:09
num = 1
def fun1():
    global num # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()