import numpy as np

l = [0, 1, 3, 3]
r = np.arange(4)
e = np.equal(l, r)
print(e)  # [ True  True False  True]
res = np.where(l == r)  # 两个数组的比较
print(res)  # (array([0, 1, 3]),)
xs1 = np.array([-0.5, 1.5, 1.5, 2.5, 5.5])
xs2 = np.array([1.5, 1.5, 2.5, 5.5, -0.5])

ises = np.equal(xs1, xs2).astype("int") # [0 1 0 0 0]
print(ises)
