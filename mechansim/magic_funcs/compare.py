# rich comparison
# 运算符号与方法名称的对应关系如下：
# x<y 调用 x.__lt__(y)     less than
# x<=y 调用 x.__le__(y)、   less equal
# x==y 调用 x.__eq__(y)、
# x!=y 调用 x.__ne__(y)、
# x>y 调用 x.__gt__(y)、
# x>=y 调用 x.__ge__(y)
class GTA_car():
    def __init__(self, name, top_speed, accelerate):
        self.name = name
        self.top_speed = top_speed
        self.accelerate = accelerate

    def __eq__(self, other):
        print('__eq__ function is proceeded!')

    def __ne__(self, other):
        print('__nq__ function is proceeded!')

    def __gt__(self, other):
        print('__gt__ function is proceeded!')

    def __ge__(self, other):
        print('__ge__ function is proceeded!')

    def __lt__(self, other):
        print('__lt__ function is proceeded!')

    def __le__(self, other):
        print('__le__ function is proceeded!')


def print_cars(car_list):
    for car in car_list:
        print(car.name)


car01 = GTA_car('Obey9F', '0.83', '0.82')
car02 = GTA_car('Karin Futo', '0.72', '0.72')
car03 = GTA_car('Buffal S', '0.77', '0.72')
car04 = GTA_car('Annis Elegy RH8', '0.81', '0.82')
car05 = GTA_car('Albany', '0.83', '0.85')
car_list = [car01, car02, car03, car04, car05]
print_cars(car_list)
car_list.sort()
print_cars(car_list)


class LargerNumKey(str):
    def __lt__(self, other):
        return self+other > other+self


print(LargerNumKey('20') < LargerNumKey('21'))
