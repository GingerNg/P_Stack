import sys  # 　Python 解释器关系密切的标准库。


# Python有递归次数限制，默认最大次数为1000
print(sys.getrecursionlimit())  # 返回递归限制的当前值，即Python解释器堆栈的最大深度
# import sys
# sys.setrecursionlimit(1500)
# def recursion(n):
#     if(n <= 0):
#         return
#     print(n)
#     recursion(n - 1)

# if __name__ == "__main__":
#     recursion(10000)
print(sys.getsizeof(1000.0))  # 查看变量所占字节的大小
print(sys.getsizeof(100))  # int占内存的字节大小
print(sys.maxsize)  # 平台的Py_ssize_t类型支持的最大正整数

# print(sys.modules)

print(sys.platform)

print(sys.getprofile())
print(sys.exc_info())  # 此函数返回三个值的元组，这些值提供有关当前正在处理的异常的信息
