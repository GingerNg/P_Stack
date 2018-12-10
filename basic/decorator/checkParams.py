# coding:utf8
# author:ginger
import logging

#  ?
logging.basicConfig(level=logging.INFO)


def checkParams(fn):
    def wrapper(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return fn(a, b)

        logging.warning("variable 'a' and 'b' can't be added")
        return

    return wrapper


@checkParams
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(3, 'hello')
