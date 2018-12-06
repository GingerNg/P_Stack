#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: setup_demo.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-14 下午11:32
 @desc: http://blog.csdn.net/pfm685757/article/details/48651389
 setuptools是Python distutils增强版的集合，它可以帮助我们更简单的创建和分发Python包，尤其是拥有依赖关系的
"""

from setuptools import setup, find_packages
setup(
    name = "demo",
    version = "0.1",
    packages = find_packages(),
)