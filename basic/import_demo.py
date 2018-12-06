# coding=utf-8

from utils.file_util import find_all_file

module_name = "foo"

module = __import__(module_name)   # 模块对象

print (module)

function_name = "call_func"

print (getattr(module, function_name))   # 函数对象

print (find_all_file("/XXX/some"))

