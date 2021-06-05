# cls主要用在类方法定义，而self则是实例方法
# python创建实例时，会先调用__new__构造方法，然后使用__init__进行实例初始化。
# a = A(xxxx)，实际上是a = A.__new__(A)，和a.__init__(xxx)
# https://www.cnblogs.com/ydf0509/p/9463832.html

class Singleton():
    __instance_e = None
    __instance_c = None

    def __init__(self, lang):
        print("我是init方法.", lang)

    def __new__(cls, lang):
        if lang == 'c':
            # print(Singleton.__instance_c)
            if not cls.__instance_c:
                cls.__instance_c = object.__new__(cls)
            return cls.__instance_c
        else:
            if not cls.__instance_e:
                cls.__instance_e = object.__new__(cls)
            return cls.__instance_e

from functools import wraps
def singleton(cls):
    print(cls, "-----")
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance


@singleton
class MyClass(object):
    def __init__(self):
        super().__init__()
        print("init")
    a = 1


obj1 = Singleton(lang="c")
obj2 = Singleton(lang="c")
obj3 = Singleton(lang='e')
print(id(obj1), id(obj2), id(obj3))

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
print(id(obj1), id(obj2), id(obj3))