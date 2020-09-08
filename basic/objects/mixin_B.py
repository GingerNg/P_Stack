"""
Mixin 即 Mix-in，常被译为“混入”，是一种编程模式，在 Python 等面向对象语言中，通常它是实现了某种功能单元的类，用于被其他子类继承，将功能组合到子类中。
利用 Python 的多重继承，子类可以继承不同功能的 Mixin 类，按需动态组合使用。
当多个类都实现了同一种功能时，这时应该考虑将该功能抽离成 Mixin 类。
"""

class MappingMixin:
    def __getitem__(self, key):
        return self.__dict__.get(key)

    def __setitem__(self, key, value):
        return self.__dict__.set(key, value)


class ReprMixin:
    def __repr__(self):
        s = self.__class__.__name__ + '('
        for k, v in self.__dict__.items():
            if not k.startswith('_'):
                s += '{}={}, '.format(k, v)
        s = s.rstrip(', ') + ')'  # 将最后一个逗号和空格换成括号
        return s

class Person(MappingMixin, ReprMixin):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


if __name__ == "__main__":
    p = Person("小陈", "男", 18)
    print(p['name'])  # "小陈"
    print(p)