# 类型注解
from typing import List, Union, Optional


def f(a: Optional[List[int]]) -> int:
    if a is None:
        return len(a)
    else:
        return 0


f([1, 2, 3])

# Python3提供一种语法，用于为函数声明中的参数和返回值附加元数据。


def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None


print(clip.__annotations__)
