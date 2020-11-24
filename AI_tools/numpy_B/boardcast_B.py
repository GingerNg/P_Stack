import numpy as np
# broadcast
# 当数组跟一个标量进行数学运算时，标量需要根据数组的形状进行扩展(广播)，然后执行运算。
a = np.array([[1, 3, 4], [4, 5, 6]])
print(a*2)

