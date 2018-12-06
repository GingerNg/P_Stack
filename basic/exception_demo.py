# ­*­ coding: utf­8 ­*­
"""
@file: exception_demo.py
"""

class DatabaseException(Exception):
    def __init__(self,err='数据库错误'):
        Exception.__init__(self,err)

class PreconditionsException(DatabaseException):
    def __init__(self,err='PreconditionsErr'):
        DatabaseException.__init__(self,err)

def testRaise():
    raise PreconditionsException()

try:
    testRaise()
except PreconditionsException as e:
    print (e)


class CustomError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self)  #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo

if __name__ == '__main__':
    try:
        raise CustomError('客户异常')
    except CustomError as e:
        print(e)