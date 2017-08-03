#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/3 13:46
spam = {'ds': 'dsd', 'dsdaa': 'ds'}  # 字典，不排序
print(spam)

for v in spam.values():
    print(v) # for迭代字典中的每个值

for k in spam.keys():
    print(k)

for k_v in spam.items():
    print(k_v)
