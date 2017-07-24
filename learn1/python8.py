#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 19:16
import sys


def fibonacci(n):  # 生成器函数，斐波拉契
    a, b, conter = 0, 1, 0
    while True:
        if (conter > n):
            return
        yield a
        a, b = b, a + b
        conter += 1
f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()