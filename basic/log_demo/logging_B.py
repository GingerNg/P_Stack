import logging
import datetime
logging.basicConfig(level=logging.DEBUG,
                    format='asctime:        %(asctime)s \n'  # 时间
                           'filename_line:  %(filename)s_[line:%(lineno)d] \n'  # 文件名_行号
                           'level:          %(levelname)s \n'  # log级别
                           'message:        %(message)s \n',  # log信息
                    # filename='./log/server_{0}.log'.format(datetime.datetime.now().strftime("%Y-%m-%d")),
                    # sys.path[1]获取当前的工作路径
                    filemode='a')  # 如果模式为'a'，则为续写（不会抹掉之前的log）

logging.debug("this is an test1 debug!")