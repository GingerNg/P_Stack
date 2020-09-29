# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: codecs_demo.py
@time: 2018/5/10 15:25
原有编码 -> 内部编码 -> 目的编码
python的内部是使用unicode来处理的
https://blog.csdn.net/zhaoweikid/article/details/1642015
"""

# 用codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode

test = 12>1