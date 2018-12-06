# coding:utf8
# author:ginger

class A(object):
    def __init__(self):
        self.b=1
        self.c=2
    def do_nothing(self):
        pass

a = A()
a.__dict__
print (type(a.__dict__))


def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value):
            pr[name] = value
    return pr

print (type(props(a)))
print (props(a))
