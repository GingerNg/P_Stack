#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: attr_builtin_func.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-21 下午11:34
 @desc:
 @source: https://www.cnblogs.com/cenyu/p/5713686.html
"""
class Food():
    price = '10'
    raw = 'meat'
    def taste(self):
        return 'good'

def goodBad():
    return 3

if __name__=='__main__':
    food = Food()
    print (hasattr(food,'raw'))
    print (hasattr(food,"taste"))
    print (getattr(food,'taste'))  # 如果没有属性报错
    print (getattr(food,'time'))



    setattr(food,'time','20171125')
    setattr(food,'goodbad',goodBad)

    print (getattr(food,'goodbad'))

    setattr(Food,'time','201711250049')  # 可以为class动态增加属性
    food1 = Food()
    print (getattr(food1, 'time'))
