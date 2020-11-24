# 数据拆分
# 水平”是horizontal
# “竖直”是vertical
import numpy as np
b = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])  # (4,4)

print(np.split(b, 2, axis=1))  # split by 垂直

print(np.hsplit(b, 2))

print(np.vsplit(b, 2))  # 水平split


b = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])  # (4,4)
bb = np.dstack((b, b))
print(bb.shape)
print(np.dsplit(bb, 2)[0].shape)  # dsplit 按维度切分
