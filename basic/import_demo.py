# coding=utf-8

from utils.file_util import find_all_file

module_name = "obj_property"

module = __import__(module_name)   # 模块对象

print(module)

function_name = "prn_obj"

print(getattr(module, function_name))   # 函数对象

# 三目运算符
a = 2
b = 1
h = "变量1" if a > b else "变量2"
print(h)
