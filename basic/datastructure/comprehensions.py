#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: comprehensions.py
 @author: ginger 
 @software: PyCharm  
 @time: 18-2-23 下午12:07
 @desc: 推导式comprehensions
"""
"""
https://www.cnblogs.com/tkqasn/p/5977653.html
列表(list)推导式
字典(dict)推导式
集合(set)推导式
"""

multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)
print type(multiples) # <type 'list'>


multiples = (i for i in range(30) if i % 3 is 0)
print(multiples)
print type(multiples) # <type 'generator'>