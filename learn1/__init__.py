#!/usr/bin/env python
# -*- coding: utf-8 -*-
print('hello')
if 1==1:
    print("true")
else:
    print("false")
print("a", end="")
print("b")
import sys
print("================Python import mode==========================");
print("命令行参数为:")
for i in sys.argv:
    print(i)
    print('\n python路径',sys.path)
    print(help(max))