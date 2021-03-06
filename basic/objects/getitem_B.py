# __getitem__()
# 如果在类中定义了__getitem__()方法，那么他的实例对象（假设为P）就可以这样P[key]取值。
# 当实例对象做P[key]运算时，就会调用类中的__getitem__()方法。
class DataTest:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.d = {"id": self.id,
                  "add": self.address
                  }

    def __getitem__(self, key):
        # return "hello"
        return self.d.get(key, None)

    def __setitem__(self, key, value):
        self.d.__setitem__(key, value)


data = DataTest(1, "192.168.2.11")
print(data["id"])

data["ii"] = 333
print(data["ii"])

print(data["iii"])