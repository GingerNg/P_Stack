import pysnooper
"""
PySnooper输出信息主要包括以下几个部分：

局部变量值
代码片段
局部变量所在行号
返回结果
"""

@pysnooper.snoop()
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]

number_to_bits(6)