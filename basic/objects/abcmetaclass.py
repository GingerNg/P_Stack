import abc


class Animal(metaclass=abc.ABCMeta):  # 同一类事物:动物
    def __init__(self):
        pass

    @abc.abstractmethod                   # 上述代码子类是约定俗称的实现这个方法，加上@abc.abstractmethod装饰器后严格控制子类必须实现这个方法
    def talk(self):
        pass
        # raise AttributeError('子类必须实现这个方法')


class People(Animal):  # 动物的形态之一:人
    def __init__(self):
        super().__init__()

    def talk(self):
        print('say hello')


class Dog(Animal):  # 动物的形态之二:狗
    def talk(self):
        print('say wangwang')


class Pig(Animal):  # 动物的形态之三:猪
    def talk(self):
        print('say aoao')

# a = Animal()  # 抽象类无法实例化
peo2 = People()
pig2 = Pig()
d2 = Dog()

peo2.talk()
pig2.talk()
d2.talk()