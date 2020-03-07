
import schedule
import time

# 定义要完成的任务
def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
# 每10分钟执行一次
schedule.every(10).minutes.do(job)
# 每小时执行一次
schedule.every().hour.do(job)
# 每天10:30执行一次
schedule.every().day.at("10:30").do(job)
# 每周一执行一次
schedule.every().monday.do(job)
# 每周三的13:15执行一次
schedule.every().wednesday.at("13:15").do(job)
# 每小时的第17分钟执行一次
schedule.every().minute.at(":17").do(job)

"""
独立进程
占用系统资源
"""
while True:
    schedule.run_pending()
time.sleep(1)