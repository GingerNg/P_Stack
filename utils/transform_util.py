#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: transform_util.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-12-1 下午2:17
 @desc: 
"""
import itertools
def lists_to_list(lists): # https://www.zhihu.com/question/27010691
    return list(itertools.chain.from_iterable(lists))


if __name__=='__main__':
    a = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
    print (lists_to_list(a))