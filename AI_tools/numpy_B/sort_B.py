import numpy as np

dt = np.dtype([('name',  'S10'), ('age',  int)])
a = np.array([("raju", 21), ("anil", 25),
              ("ravi",  17),  ("amar", 27)], dtype=dt)
print(np.sort(a, order='name'))
# numpy.argsort()
# 函数返回的是数组值从小到大的索引值。
x = np.array([3,  1,  2])
print(np.argsort(x)[0:2])

# numpy.lexsort() 用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列
nm = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.y.',  's.y.',  's.y.',  'f.y.')
print(np.lexsort((dv, nm)))

# 求array中出现次数最多的元素
c = np.array([1, 2, 5, 9, 9, 9, 3])
# 和列表list.count(a)统计a在列表中出现的次数很像，但又不同;返回的是0–序列最大值在这个array中出现的次数
d = np.argmax(np.bincount(c))
print(d)

print(np.newaxis)
