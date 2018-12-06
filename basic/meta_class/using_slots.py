# coding:utf8
# author:ginger

# http://www.cnblogs.com/rainfd/archive/2017/04/07/slots.html
"""
当一个类需要创建大量实例时，可以通过__slots__声明实例所需要的属性
例如，class Foo(object): __slots__ = ['foo']。这样做带来以下优点：
更快的属性访问速度
减少内存消耗

默认情况下，访问一个实例的属性是通过访问该实例的__dict__来实现的。如访问a.x就相当于访问a.__dict__['x']

Python内置的字典本质是一个哈希表，它是一种用空间换时间的数据结构。为了解决冲突的问题，当字典使用量超过2/3时，Python会根据情况进行2-4倍的扩容。
由此可预见，取消__dict__的使用可以大幅减少实例的空间消耗。
"""


