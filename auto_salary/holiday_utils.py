import requests


def holiday_api(day):
    """
    1、接口地址：http://api.goseek.cn/Tools/holiday?date=数字日期，支持https协议。
    2、返回数据：正常工作日对应结果为 0, 法定节假日对应结果为 1, 节假日调休补班对应的结果为 2，休息日对应结果为 3
    3、节假日数据说明：本接口包含2017年起的中国法定节假日数据，数据来源国务院发布的公告，每年更新1次，确保数据最新
    :param day:
    :return:
    """
    res = requests.get("http://api.goseek.cn/Tools/holiday?date=20170528")
    print(res.json())

if __name__ == '__main__':
    holiday_api(day=1)