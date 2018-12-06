# -*- coding:utf-8 -*-

from architecture.plugin_demo import foo

filename = "func.py"
def show_filename():
	return "filename: %s" % filename

if __name__ == '__main__':
	print (foo.call_func(show_filename))   # 将函数作为参数