class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


As = [A(1, 2), A(2, 3), A(2, 1), A(0, 5)]

RAs = sorted(As, key=lambda x: [x.a])

for a in RAs:
    print(a.__dict__)

RAs = sorted(As, key=lambda x: [x.a, x.b])  # 先按a排序，再按b排序
for a in RAs:
    print(a.__dict__)
