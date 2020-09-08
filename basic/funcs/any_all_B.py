# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
# Python provides two unique built-in functions that allow us to check if all elements in an iterable are True ,  是否全部是
# and if any element is True . 是否存在一个
all_true = [True, True, 1, 'hello']
any_true = [0, False, True, '', []]
print(any([0, 1, 2]))

print(any([0, 0, 0, 0]))
