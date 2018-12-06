#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: number_coversion.py
 @author: ginger 
 @software: PyCharm
 @desc: 
"""
"""
先将m进制转换为10进制，再将10进制转为n进制。
进制转换: m->10从低位到高位按权展开即可。
10->n 除留取余，逆序排列 
"""
def toTen(m,number):
    ten = 0
    index = 0;
    revered = str(number)[::-1]
    for i in revered:
        ten = ten + int(i)*m**index
        index = index+1
    return ten

def ten2n(n,ten):
    shang = ten/n
    remainer = ten%n
    nums = [remainer]
    while(shang != 0):
        remainer = shang%n
        nums.append(remainer)
        shang = shang/n
    return nums[::-1]


# if __name__ == "__main__":
#     print toTen(8,1356) #750
#     print 10%3
#     print 10/3
#
#     print ten2n(16,65036)   # FE0C