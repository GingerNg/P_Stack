from functools import reduce


def str2list(string, type=str):
    return list(map(type, string))


print(str2list('12345', int))


def square_it_func(a):
    return a * a


x = map(square_it_func, [1, 4, 7])
list(x)


def cube(x): return x*x*x


list((map(cube, range(1, 11))))

seq = range(8)
reportDataToal = dict(map(lambda x: (x, x), seq))
print(reportDataToal)

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(filter(lambda x: x % 3 == 0, foo)))
print(reduce(lambda x, y: x + y, foo))

ii = [(0, '\x00+N\x01'), (1, '\x00+E\x01'), (2, '\x00+W\x01')]


def saleplus(x, y):
    #     print(x)
    return (0, x[1]+y[1])


print(reduce(saleplus, ii)[1][1])

N = 100000
a = [1 for _ in range(N)]
b = [i for i in range(N)]


def mulipy(x, v, t):
    return x+v*t


# def mul2(x[0]):
#     return x[0]+x[1]
# %time
x = map(mulipy, a, b)
print(x)

# %time
x = map(lambda x, y: x+x*y, a, b)


def f(x):
    return x[2] < 0


xx = filter(f, x)
list(xx)


def plus(x, y):
    return x[0]+y[0]


print(reduce(plus, xx))


def stop(x):
    if x[1] <= 0 or x[1] >= 3:
        x[2] = 0
    return x


xxx = list(map(stop, xx))
xxx


def f(x):
    return x % 2 != 0 and x % 3 != 0


sum(filter(f, range(2, 25)))


def for_mulity(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i]*b[i]+a[i])
    return res


# %time
res = for_mulity(a, b)
alist = [1, 2, 3]
print(reduce(lambda x, y: x + y, alist))
