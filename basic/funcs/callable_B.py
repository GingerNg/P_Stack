#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: callable_demo.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-20 下午11:21
 @desc:

 (1) id(): CPython implementation detail: This is the address of the object in memory.
 (2)  callable():  https://segmentfault.com/q/1010000002562254

"""

class A():
    pass

class B():
    def __init__(self):
        pass


if __name__ == '__main__':


    """
    callable(object) -> bool

    Return whether the object is callable (i.e., some kind of function).
    Note that classes are callable, as are instances with a __call__() method.
    """
    print (callable(A))

    print (callable(B))

    b = B()
    print (callable(b))