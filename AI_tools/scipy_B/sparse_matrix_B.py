# Sparse Matrix
# 高级数组之稀疏矩阵(https://www.cnblogs.com/chenzhijuan-324/p/10637028.html)
import numpy as np
import scipy.sparse as sp
A = np.array([[1, 0, 2, 0],
              [0, 0, 0, 0],
              [3, 0, 0, 0],
              [1, 0, 0, 4],
              [9, 5, 4, 5]])
print(A.shape)

# 压缩稀疏行（CSR，Compressed Sparse Row）
AR = sp.csr_matrix(A)
print(AR)
print(AR.indptr)  # 行偏移

# 稀疏列矩阵CSC（Compressed Sparse Column）
AS = sp.csc_matrix(A)
print(AS.data)
print(AS.indptr)  # 偏移量  矩阵元素的个数的累加量   列数+1
print(AS.indices)  # 索引  通过indptr来确定该元素属于哪一列(列索引)，通过列索引和行索引共同确认元素的位置
print(AS.nnz)
print(AS.toarray())
