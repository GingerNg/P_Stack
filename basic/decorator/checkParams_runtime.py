# coding:utf8
# author:ginger
import time
import datetime
import logging

#  ?
logging.basicConfig(level=logging.INFO)


def get_server_time():
    return (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")


def RunTime(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logging.warning("start-time is:{}".format(start_time))
        fn(*args, **kwargs)
        end_time = time.time()
        logging.info(
            'end-time is:{}; process time: {}'.format(end_time, str(end_time - start_time)))
    return wrapper


def checkParams(fn):
    def wrapper(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return fn(a, b)
        logging.warning("variable 'a' and 'b' can't be added")
        return

    return wrapper


@RunTime
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(3, 1)
