# coding=utf-8
from zope.interface import Interface
from zope.interface.declarations import implementer

# 定义接口
class MyMiss(Interface):
    def imissyouatlost(self,miss):
        """Say i miss you at lost to miss"""

@implementer(MyMiss) # 继承接口
class Miss:
    def imissyouatlost(self,somebody):
        """Say i miss you at lost to somebody"""
        return "i miss you at lost, %s!" % somebody

if __name__ == '__main__':
    z = Miss()
    hi = z.imissyouatlost('Zy')
    print(hi)

    