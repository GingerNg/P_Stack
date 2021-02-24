from pydantic import BaseModel

class Person(BaseModel):
    name: str

p = Person(name="Tom")
p1 = Person(name=p)  # 默认转为字符串 强制类型转换， str type expected (type=type_error.str)
print(p1.name)
print(p.json())

def func(a:Person):
    print(a.json())


func(p1)