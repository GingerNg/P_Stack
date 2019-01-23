import re

if __name__ == "__main__":
    ress = re.search('[a-zA-Z\u4e00-\u9fa5]{2,}', "2019金融数据科技qwqa")
    print(ress)