class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('self:', self)

    # 定义一个build方法，返回一个person实例对象，这个方法等价于Person()。
    @classmethod
    def build(cls):
        # cls()等于Person()
        p = cls("Tom", 18)
        print('cls:', cls)
        return p


if __name__ == '__main__':
    person = Person.build()
    print(person, person.name, person.age)