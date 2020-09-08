# global nonlocal
# 在一个 python 程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。

# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。

g_count = 0  # 全局作用域


def outer():
    def inner():
        g_count = 100  # 局部作用域  此g_count 和最外层的g_count 不是同一个
        i_count = 2  # 局部作用域

    o_count = 1  # 闭包函数外的函数中
    print(g_count)
    inner()
    print(g_count)
#     g_count = 100


outer()
print(g_count)

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了


def outer():
    num = 10

    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)


outer()
