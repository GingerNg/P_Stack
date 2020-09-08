# lambda 为关键字。filter，map，reduce为内置函数。

def x(a, b): return a * b


x(5, 6)  # prints  30


f0, f1, f2 = [lambda x: x*i for i in range(3)]
print(f0(1))
