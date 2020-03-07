#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: first.py
 @author: ginger 
 @software: PyCharm  
 @time: 18-2-8 下午5:44
 @desc: 
"""
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()                   # connect to the JVM
random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
number1 = random.nextInt(10)              # call the Random.nextInt method
number2 = random.nextInt(10)
print(number1,number2)

stack = gateway.entry_point.getStack()
stack.push("First %s" % ('item'))
print (stack.pop())  # jvm保持运行, 当stack为空时,会报异常
internal_list = stack.getInternalList() # 获得stack内部的list

# 一个JavaGateway允许你列出某个对象中所有可用的成员
# http://blog.csdn.net/u010159842/article/details/69251773
