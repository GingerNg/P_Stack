
# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
myslice = slice(5)
arr = range(10)
print(arr)
print(arr[myslice])  # range(0, 5)

s2 = slice(1, 4)
print(arr[s2])  # range(1, 4)
