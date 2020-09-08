# coding:utf8
# author:ginger

class A(object):
    def __init__(self):
        self.b = 1
        self.c = 2

    def do_nothing(self):
        pass


a = A()
a.__dict__
print(type(a.__dict__))

"""
dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。
如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
"""


def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value):
            pr[name] = value
    return pr


print(type(props(a)))
print(props(a))
