# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: file_replace.py
@time: 2018/8/2 15:14
"""
from os import replace

f = open("C:\\PATH\\test\\ask.html", 'rb')
#
# print(f.read())

file_obj = str(f.read())
if file_obj.lower().find("charset=utf-8") == -1:
    # file_obj = replace("<head>").replace('<head><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">')
    file_obj = file_obj.replace("<head>", '<head><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">')\
                .replace("<HEAD>", '<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">')
    print(file_obj)