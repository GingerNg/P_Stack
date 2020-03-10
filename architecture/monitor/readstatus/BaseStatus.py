# -*- coding:utf-8 -*-
# Author:  chenhailong --<chenhailong@chinadep.com>
# Created: 2017/5/19

########################################################################
class BaseStatus(object):
    """状态基类"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass
    def readStatus(self):
        '''implement'''
        raise NotImplementedError
    def toJson(self):
        '''implement'''
        raise NotImplementedError
    


if __name__ == "__main__" :
    '''this is the main method'''