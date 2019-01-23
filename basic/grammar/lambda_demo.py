#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
lambda 定义了一个匿名函数
'''

from functools import reduce


def make_incrementor(n):  # 等价于 make_incrementor(n)=lambda x:x+n
    return lambda x: x + n


m = 54

make_incrementor1 = lambda x: x + m

f = make_incrementor(46)
n = 10
print(f(n))  # 56

if __name__ == '__main__':
    print(make_incrementor1(3))

    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

    print("sum: %s" % sum(foo))
    print(list(filter(lambda x: x == 0, foo)) == [])

    print(list(filter(lambda x: x % 3 == 0, foo)))
    # [18, 9, 24, 12, 27]

    print(list(map(lambda x: x * 2 + 10, foo)))
    # [14, 46, 28, 54, 44, 58, 26, 34, 64]

    print(reduce(lambda x, y: x + y, foo))
    # 139

    fl = [{"ans_score": 0.9, "ans": "test1"}, {"ans_score": 0.1, "ans": "test2"}]
    print([f for f in fl if f["ans_score"] > 0.5])

    fl = {"ans_score": 0.9, "ans": 0.8}
    print([k for k, v in fl.items() if v > 0.5])

    test = {"t":"q","w":"f"}
    print(("t" in test))  # True
    print(("q" in test))  # False
    print(test.values()) # list

    wdict = {}
    for k, v in wdict if type(wdict) is type([]) else wdict.items():
        print(k,v)

    for i in "test":
        print(i)

    """
    三目运算符
    """
    x = 2
    x = x+1 if x%2==1 else x

    ss = set()
    ss.add("test")
    ss.add("test")
    print(ss)

    # 两个list合并&去重
    a = [1,3,5,7]
    b = [1,3,4,6,8]
    c=list(set(a) | (set(b)))

    # c = list(set(a + b))

    print(c)

    print(str(["1","2"]))
    items = [{"sale":1.0},{"sale":2.0}]
    print(reduce(lambda x, y: x["sale"] + y["sale"], items))

