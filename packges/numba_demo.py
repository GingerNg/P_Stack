import numpy as np
from numba import jit
import time

# numba是一款可以将python函数编译为机器代码的JIT编译器，经过numba编译的python代码（仅限数组运算），其运行速度可以接近C或FORTRAN语言

@jit
def sum_jit(arr):
    s_time = time.time()
    m = arr.shape[0]
    result = 0.0
    for i in range(m):
        result += arr[i]
    e_time = time.time()
    return (e_time-s_time)


def sum(arr):
    s_time = time.time()
    m = arr.shape[0]
    result = 0.0
    for i in range(m):
        result += arr[i]
    e_time = time.time()
    return (e_time-s_time)


def main():
    n = int(50.0*1e6)
    array = np.random.random(n)
    t1 = sum_jit(array)
    t2 = sum(array)
    print("Time with JIT:", t1)
    print("Time without JIT:", t2)


if __name__ == '__main__':
    main()
