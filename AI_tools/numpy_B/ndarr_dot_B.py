import numpy as np

#
a = np.array([[3, 1, 2.0], [4, 6, 1]])
print(a.itemsize)  # itemsize属性返回数组中各个元素所占用的字节数大小。
print(a.size)
print(a.nbytes)  # size*itemsize

arr1 = np.array([2, 3]).T
print(arr1.shape)
arr1 = arr1.T
print(arr1.shape)
arr2 = np.array([3, 4])

print(arr1.dot(arr2))

arr5 = np.array([[2, 3], [4, 5]])
arr6 = np.array([[6, 7], [8, 9]])

print(arr5.dot(arr6))

X = np.array([[2, 3], [4, 5], [2, 3]])  # (3,2)
# pc = np.array([[2, 3], [2, 3]])
pc = np.array([[2, 3]])
num_row = 1
print(pc.shape)
pc_t = pc.transpose()
if num_row == 1:
    res = X.dot(pc_t) * pc
else:
    res = X.dot(pc_t).dot(pc)
print(res)


a = np.array([3, 1, 2])
b = np.array([4, 6, 2])
print(a * b)  # [12  6  4]
print(sum(a*b))

print(a**b)  # 逐项 a^b
