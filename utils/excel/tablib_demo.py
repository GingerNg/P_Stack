#!/usr/bin/python
# -*- coding:utf-8 -*-


import tablib
headers = ('area', 'user', 'recharge')
data = [
    ('1', 'Rooney', 20),
    ('2', 'John', 30),
]
data = tablib.Dataset(*data, headers=headers)

#然后就可以通过下面这种方式得到各种格式的数据了。
# data.xlsx
# data.xls
# data.ods
# data.json
# data.yaml
# data.csv
# data.tsv
# data.html

#增加行
data.append(['3', 'Keven', 18])
#增加列
data.append_col([22, 20, 13], header='Age')
print (data.csv)

#删除行
del data[1:3]
#删除列
del data['Age']
print (data.csv)

key = ["t1","t2"]
value = [23,24]
col3 = [3,4]

for i in range(len(key)):
    data.append([key[i],value[i],col3[i]])

# 写
open("tablib_demo.csv","wb").write(data.csv)

# 读 ??



