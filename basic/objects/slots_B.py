# slots
# 作用： 限定一个类创建的实例只能有固定的实例属性(实例变量)

# 当一个类需要创建大量实例时，可以通过__slots__声明实例所需要的属性
# 例如，class Foo(object): __slots__ = ['foo']。这样做带来以下优点：
# 更快的属性访问速度
# 减少内存消耗

# 默认情况下，访问一个实例的属性是通过访问该实例的__dict__来实现的。如访问a.x就相当于访问a.__dict__['x']

# Python内置的字典本质是一个哈希表，它是一种用空间换时间的数据结构。为了解决冲突的问题，当字典使用量超过2/3时，Python会根据情况进行2-4倍的扩容。
# 由此可预见，取消__dict__的使用可以大幅减少实例的空间消耗。


class Person(object):
    __slots__ = ("name", "age")


class O(object):
    def __init__(self):
        self.o = 1


print(O().__dict__)
p = Person()
# print(p.__dict__)
p.name = "jj"
print(p.name)
print(p.__dict__)
