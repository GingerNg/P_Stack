#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
print ("脚本名：", sys.argv[0])
for i in range(1, len(sys.argv)):
    print ("参数", i, sys.argv[i])


print(bool({}))  # False
print(bool({"1":"1"}))

w = 2
w /= 2
print(w)


