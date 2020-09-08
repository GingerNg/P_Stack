# sys
# Python确实有递归次数限制，默认最大次数为1000

import sys
sys.getrecursionlimit()
# import sys
# sys.setrecursionlimit(1500)
# def recursion(n):
#     if(n <= 0):
#         return
#     print(n)
#     recursion(n - 1)

# if __name__ == "__main__":
#     recursion(10000)
sys.getsizeof(1000.0)  # 字节

sys.maxsize  # 获取最大的Int值

sys.getsizeof(100)

print(sys.getprofile())