#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: random_util.py
 @author: ginger 
 @software: PyCharm
 @desc:
 https://www.cnblogs.com/yd1227/archive/2011/03/18/1988015.html
"""
import os
import random
print (random.randint(12, 20))


def sample():
    test = [1, 2, 3, 4, 5]
    """Chooses k unique random elements from a population sequence or set"""
    print(random.sample(test,4))


def shuffle():
    test = [1,2,3,4,5]
    random.shuffle(test)
    print(test)


if __name__ == "__main__":
    shuffle()
    sample()


    rootdir="C:\\data"
    for parent,dirnames,filenames in os.walk(rootdir):
        print(filenames)
