#!/usr/bin/python
# -*- coding:utf-8 -*-
class A:
    def __init__(self):
        for k in (getattr(self, x) for x in dir(self)): # dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
            # print 'x':x
            print(k)
        a = 0
        b = 0

    def func2(self, func1):
        func1.no = 2
        print(func1.__dict__)


class B(A):
    aa = 1
    bb = 2

    @staticmethod
    def func1(self):
        print(1)


if __name__ == '__main__':
    b = B()
    a = A()
    a.func2(B.func1)
