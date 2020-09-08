def foo():
    print('starting')
    while True:
        r = yield 2
        print(r)


f = foo()
print(f.send(None))
print(f.send(1))


def func(n):
    for i in range(0, n):
        #         print(i)
        val = yield i


g1 = func(10)
print(list(g1))
g = func(10)
for m in g:
    print(m)
    print(g.send(2))
