#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 10:27
# Fibonacci series
a,b = 0,1
while b<10:
    print(a)
    a,b=b,a+b


number = 10
guess = -1
print("猜字游戏")
while guess!=number:
    guess = int(input("请输入你猜的数字："))
    if guess==number:
        print("caidui")
    elif guess<number:
        print("xiaoel")
    elif guess>number:
        print("ds")