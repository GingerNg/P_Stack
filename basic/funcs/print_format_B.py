# 格式化输出(%用法和fomat用法)
# https://blog.csdn.net/lanluyug/article/details/80245220

#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: format_demo.py
 @author: ginger
 @software: PyCharm
 @desc: https://www.cnblogs.com/benric/p/4965224.html
"""
print('{0:*>10}'.format(10))
print('{0:.2f}'.format(1/3))

print('{我}今天{action}'.format(我='拦路雨', action='在写博客'))

grade = {'I': '拦路雨', '状态': '写博客'}
print('{I}比较无聊，在{状态}'.format(**grade))  # 字典前加上**·
print('{:^20}'.format('拦路雨'))  # 居中 :^ 宽度14
print('{:>20}'.format('拦路雨'))  # 右对齐 :> 宽度14
print('{:<20}'.format('拦路雨'))  # 左对齐 :< 宽度14
print('{:*<20}'.format('拦路雨'))  # :后边可跟填充物,只允许一个字符
print('{:@>20}'.format('拦路雨'))
print('{:,}'.format(100000000))
print('{:,}'.format(235445.234235))  # 只对数字生效
