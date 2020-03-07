
# 比较大小的规则是以ASCII码表为基准, 从两个列表中的第一个字符开始进行比较, 返回值为布尔类型.
import operator
a = [1, 2]
b = [1, 3]
print(operator.eq(a, b))
