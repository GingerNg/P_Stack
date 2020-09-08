### OrderedDict
# OrderedDict 也是 dict 的子类，其最大特征是，它可以“维护”添加 key-value 对的顺序。
# 简单来说，就是先添加的 key-value 对排在前面，后添加的 key-value 对排在后面。

from collections import OrderedDict
my_data = {'Python': 20, 'Swift':32, 'Kotlin': 43, 'Go': 25}
# 创建基于key排序的OrderedDict
d1 = OrderedDict(sorted(my_data.items(), key=lambda t: t[0]))
# 创建基于value排序的OrderedDict
d2 = OrderedDict(sorted(my_data.items(), key=lambda t: t[1]))
print(d2)