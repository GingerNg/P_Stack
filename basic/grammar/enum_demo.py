#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: enum_demo.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-22 下午11:14
 @desc:
 @source https://www.cnblogs.com/codingmylife/archive/2013/05/31/3110656.html  Python: Enum枚举的实现
"""
from enum import Enum


def enum(**enums):
    return type('Enum', (), enums)


Numbers = enum(ONE=1,
               TWO=2,
               THREE='three'
               )


class EnumDemo(Enum):
    test = "1"


if __name__ == '__main__':
    print(Numbers.__dict__)
    print(Numbers.ONE)
    print(EnumDemo.test.value)
