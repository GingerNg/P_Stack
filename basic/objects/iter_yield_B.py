def foo():
    print('starting')
    while True:  # 可重复迭代
        r = yield 2
        # print(type(r))
        print(r)


f = foo()
print("--------------------------")
print(f.send(None))  # 运行到 r = yield 2
print("--")
f.send(5)  # 修改了第一个r, 运行print(r)，运行r = yield 2
# print(f.send(None))
print("--------------------------")


def func(n):
    for i in range(0, n):
        #         print(i)
        val = yield i
        # yield i


g1 = func(10)
print(list(g1))
g = func(10)
try:
    for m in g:
        print(m)
        print(g.__next__())
        print(g.send(2))
        print("---")
except Exception as e:
    print(e.__repr__())
# 第一次执行要么next(r)要么r.send(None)，不能使用r.send('xxxxx'), 发送给前一个位置的变量
# send主要是用于外部与生成器对象的交互
# send的作用其实就是一个动作指令，这个指令的具体工作内容就是从当前的yield执行到下一个yield，当找不到下一个yield时候就出发StopIteration
print("--------------------------")


def a():
    print('aaa')
    p1 = yield '123'
    print('bbb')
    if (p1 == 'hello'):
        print('p1是send传过来的')
    p2 = yield '234'
    print(p2)


r = a()
next(r)
r.send('hello')
