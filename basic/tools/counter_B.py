from collections import Counter

d = ["1", "1", "2", "4", "1"]

print(Counter(d))

print(Counter(d).most_common())


def f(x=[]):
    x.append(1)
    return x


print(f(), f())
