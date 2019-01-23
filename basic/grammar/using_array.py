# using array
from array import array
from collections import defaultdict

a = array('H', [4000, 10, 70, 22222])
print(sum(a))
print(a[1:3])  # left close while right open


def dict2list(dt):
    """
    kv 2 
    :param dict
    :return: list(tuple)
    """
    return sorted(dt.items(), key=lambda d: d[-1], reverse=True)


if __name__ == '__main__':
    print("test")

    ll = [1, 2, 3, 4, 5]
    print(ll[-1])  # 取最后一个元素

    """
    defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值
    """
    dd = defaultdict(int)
    print(dd["1"])

    new_ll = ["^"] + ll
    print(new_ll)

    pdict = {"test1": 1, "test2": 2}

    # setdefault() 函数和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值
    print("---,%s" % pdict.setdefault("test3",3))
    print("---,%s" % pdict.get("test3"))
    print(pdict)

    pp = dict2list(pdict)
    print(pp)
    for k, v in pp:
        print(k, v)
