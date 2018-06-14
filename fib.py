# 连续输出fib前n个数，把函数变成generator，如果一个函数定义中包含
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
