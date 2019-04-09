from enum import Enum

WORKDAYS = 21.5

class EmploySalary(object):
    def __init__(self,employee):
        self.info = employee

    def full_salary(self):
        return self.info["salary"] + self.info["bonus"] + self.info["subsidies"]

    def calc_tax(self):
        pass

    def month_salary(self,attends=[]):
        cnt = 0
        for attend in attends:
            if attend["attendence"] == AttendType.normal.value:
                continue
            else:
                cnt +=1




# 员工信息
employee_template = {
    "employ_id":"",
    "employ_name":"",
    "salary":0.0,  # 基本工资
    "bonus":0.0, # 奖金
    "subsidies":0.0  # 补贴

}


# 每日员工考勤
employee_attend = {
    "employ_id":"",
    "daytime":"",

    "attendence":0,  # 考勤情况

}


class AttendType(Enum):
    """
    考勤类型
    """
    normal = 0 # 正常
    absence = 1  # 缺勤
    illness = 2 # 病假
    affair = 3  # 事假




# def month_salary(employ, now_month='2019-03'):
#     """
#
#     :param now_month:
#     :return:
#     """





if __name__ == '__main__':
    print(80.0/21.5)