# coding=utf8
# using_iterator

# function iter()
s = 'abc'
it = iter(s) # it is the iterator of s  迭代器对象
print (it.next)

# 使用迭代器遍历
try:
	while True:
		print (it.next())
except StopIteration:
	pass



# function next()

# using generator to create iterator
# 带有 yield 的函数在 Python 中被称之为 generator（生成器）  ??
def reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]




if __name__ == '__main__':
	for char in reverse('gold'):
		print (char)