# islice(iterable, [start, ] stop [, step]):
# 创建一个迭代器： iterable[start : stop : step]，跳过前start个项，迭代在stop所指定的位置停止，step指定用于跳过项的步幅。迭代默认将从0开始，步幅默认1

from itertools import islice

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
list(islice(fib(),5))