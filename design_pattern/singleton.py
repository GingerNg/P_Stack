# 单例
class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class A(Singleton):
    def __init__(self):
        self.attrs = {"1":1}

class B(object):
    def __init__(self):
        self.attrs = {"1",1}

a1 = A()  # 在创建实例之前会调用__new__()方法
a2 = A()

print(a1, a2)
print(id(a1), id(a2))
print(a1 is a2)

b1 = B()  # 在创建实例之前会调用__new__()方法
b2 = B()

print(b1, b2)
print(id(b1), id(b2))
print(b1 is b2)