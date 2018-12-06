# coding=utf-8

'''
类的定义过程，其实是type类型实例化的过程。
和 dict 类似，type 也是一个工厂构造函数，调用其将返回 一个type类型的实例（即 类）。


type 有两个重载版本：
type(object)，即我们最常用的版本。
type(name, bases, dict)，一个更强大的版本。通过指定 类名称（name）、父类列表（bases）和 属性字典（dict） 动态合成一个类。
'''

class Integer(int):

   name = 'my integer'

   def increase(self, num):
       return num + 1

   # 与上面的类定义等价
   # Integer = type('Integer', (int, ), {
   # 'name': 'my integer',
   # 'increase': lambda self, num:
   #      num + 1    # 很酷的写法，不是么
   #  })