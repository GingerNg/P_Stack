# ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。

print(ord("A"))
print(chr(65))

# bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
print(bin(10))  # 0b1010

# oct() 函数将一个整数转换成 8 进制字符串，8 进制以 0o 作为前缀表示。
print(oct(10))  # 0o12

# hex() 函数用于将一个指定数字转换为 16 进制数。
print(hex(10))

# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
a = frozenset(range(10))
print(a)  # frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})


class Ginger:
    a = 1


# vars() 函数返回对象object的属性和属性值的字典对象。
print(vars(Ginger))
# {'__module__': '__main__', 'a': 1, '__dict__': <attribute '__dict__' of 'Ginger' objects>,
# '__weakref__': <attribute '__weakref__' of 'Ginger' objects>, '__doc__': None}
