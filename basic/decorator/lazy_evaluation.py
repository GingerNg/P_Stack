# coding:utf8
# lazy evaluation

from functools import reduce


def wrapper():
    alist = range(1, 101)

    def lazy_sum():
        return reduce(lambda x, y: x + y, alist)  # return函数对象

    return lazy_sum  # 返回函数的变量名


"""
alist 为局部变量，随函数被包含在lazy_sum的执行环境中，通过__globals__,
延长了它的生命周期
"""

if __name__ == '__main__':
    lazy_sum = wrapper()
    print(lazy_sum())
