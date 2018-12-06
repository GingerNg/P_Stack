#!/usr/bin/python
# -*- coding:utf-8 -*-
# https://www.cnblogs.com/Anker/archive/2013/03/04/2943498.html

"""print a Fibonnacci series up to n"""
def fib(n):
    a,b = 0,1
    while a<n:
        print (a),
    a,b=b,a+b

def fib_recursive(n):
	if n<2:  # 递归出口
		return n
	return fib_recursive(n-1)+fib_recursive(n-2)


# 尾递归就是把当前的运算结果（或路径）放在参数里传给下层函数
# 深层函数所面对的不是越来越简单的问题，而是越来越复杂的问题，因为参数里带有前面若干步的运算路径
def fib_tail_recursive(n,ret1,ret2):
	if n == 0:
		return ret1
	return fib_tail_recursive(n-1,ret2,ret1+ret2)

# fib(n)
if __name__ == "__main__":
	fib(10)
