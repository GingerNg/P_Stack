#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
lambda 定义了一个匿名函数
'''

from functools import reduce

def make_incrementor(n):   # 等价于 make_incrementor(n)=lambda x:x+n
	return lambda x:x+n

m = 54

make_incrementor1 = lambda x:x+m



f = make_incrementor(46)
n=10
print (f(n))

if __name__ == '__main__':
    print (make_incrementor1(3))

    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

    print (list(filter(lambda x: x % 3 == 0, foo)))
    # [18, 9, 24, 12, 27]

    print (list(map(lambda x: x * 2 + 10, foo)))
    # [14, 46, 28, 54, 44, 58, 26, 34, 64]

    print (reduce(lambda x, y: x + y, foo))
    # 139

    fl = [{"ans_score":0.9,"ans":"test1"}, {"ans_score":0.1,"ans":"test2"}]
    print([f for f in fl if f["ans_score"] > 0.5])