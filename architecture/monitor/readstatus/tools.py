# -*- coding:utf-8 -*-
# Author:  chenhailong --<chenhailong@chinadep.com>
# Created: 2017/5/19
#

from datetime import date, datetime
import decimal
#----------------------------------------------------------------------
def obj2Dic(obj):
    """obj对象内 属性 必须为非对象类型，否者异常并返回空列表"""
    try:
        objList = []
        for f in obj:
            objDic = {}
            for name in f.__dict__:
                if not  (name.startswith('_') or name.startswith('__')):
                    # Decimal 转 json 报错， 先转 string
                    if isinstance(getattr(f, name), decimal.Decimal) or isinstance(getattr(f, name), datetime):
                        objDic[name] = str(getattr(f, name))
                    else:
                        objDic[name] = getattr(f, name)
            objList.append(objDic)
        return objList
    except Exception, e:
        return []
if __name__ == "__main__" :
    '''this is the main method'''