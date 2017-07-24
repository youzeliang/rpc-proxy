#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 16:20

list = [1, 2, 3, 4]  # 这是迭代中的两个基本方式之一iter
it = iter(list)  # 创建迭代对象
for x in it:
    print(x)

# next函数

import sys

list1 = [1, 2, 3, 4, 5]
it = iter(list1)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
