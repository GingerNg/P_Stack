#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: callback_func.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-21 下午10:40
 @desc: 
"""

def hello(name, callback):
    return callback(name)

def sayHi(name):
    return 'hi! ' + name

def sayHowAreYou(name):
    return 'how are you! ' + name

if __name__ == '__main__':
    print hello('ginger',sayHi)
    print hello('ginger',sayHowAreYou)