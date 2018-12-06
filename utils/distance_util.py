#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: distance_util.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-12-1 下午12:34
 @desc:
 python 各类距离公式实现
 http://blog.csdn.net/guojingjuan/article/details/50396254
"""

from numpy import *

vector1 = mat([1, 2, 3])

vector2 = mat([4, 5, 6])

def manhattan(vector1,vector2):
    """
    曼哈顿距离
    :param vector1:
    :param vector2:
    :return:
    """
    print (sum(abs(vector1 - vector2)))

def hamming(vector1,vector2):
    """
    汉明距离
    :param vector1:
    :param vector2:
    :return:
    """
    # vector_list = vector1.tolist()[0]  # mat 转list
    vectors = [vector1.tolist()[0],vector2.tolist()[0]]  # 防止浅copy
    matV = mat(vectors)
    smstr = nonzero(matV[0] - matV[1]);
    return shape(smstr[0])[0]
    print (matV)



matV = mat([[1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1, 1]])
smstr = nonzero(matV[0] - matV[1]);
print (shape(smstr[0])[0])

print (hamming(mat([1, 1, 0, 1, 0, 1, 0, 0, 1]),mat([0, 1, 1, 0, 0, 0, 1, 1, 1])))