def print_everything(*args):  # 可以传递任意数量的参数:
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count, thing))
        print('{1}. {0}'.format(count, thing))  # {0}和{1}是元组的索引值

def table_things(**kwargs):   # 允许你使用没有事先定义的参数名
    for name, value in kwargs.items():
        print ('{0} = {1}'.format(name, value))

if __name__ == '__main__':
    print_everything('apple', 'banana', 'cabbage')
    table_things(apple='fruit', cabbage='vegetable')

    print("{server}{1}:{0}".format(8888, '192.168.1.100', server='Web Server Info :'))
    a = {1,2,3,4,5}  # set
    b = (1,2,)  # 元组  # 不可变序列
    c = [1,2,3]
    d = {1:2}

    print(a)
    print(type(a))
    print(type(b))
    print(d)
    print(c)