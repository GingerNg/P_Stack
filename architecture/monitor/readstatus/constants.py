# -*- coding:utf-8 -*-
# Author:  chenhailong --<chenhailong@chinadep.com>
# Created: 2017/5/19
#

#  供方常量信息
#############################################################################

# supConf 供方配置文件
supPath = "/dep/go/conf/config.ini"

# busilog 日志分析：位置和步长
busilog = "/home/chinadep/busilog/busi.log.succ"
b_step = 10000
s_b_step = 500 #最小步长

# nginx 日志分析：位置和步长
nginxlog = "/dep/go/log/nginx/go_access.log"
n_step = 10000
s_n_step = 500 #最小步长

# DAS url
DasURL = "http://172.22.66.1:8080/api/v1/sysDatas/msg"

# queryPath
path = '/api/d/qryData/'
#path = '/busilog/1.0/1000001/dem/20170518/1/dayend/'

# CPU
cpu_rate = 0.95

# DISK
disk_rate = 0.95

#MEM
mem_rate = 0.95

#LOAD
load_rate = 0.95

# 供方QPS 最大值
sup_qps = 3000000

# 持久化地址
persistPath = "/dep/go/log/sup_monitor_json.log"
#persistPath = "D:/sup_monitor_json.log"

# 订单配置文件地址
orderPath = "/dep/go/data/order_info.xml"
###########################################################################


# redis config
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 6
#process path
PROCESS_RESULT = '/dep/readstatus/out/process.out'

#query info path
QUERY_RESULT = '/dep/readstatus/out/producer_busilog.out'

#busi log path
BUSI_LOG_PATH = '/dep/go/log/busi/'

#dem_role
DEM_ROLE="producer"

#qps_detail_file
QPS_DETAIL_FILE="qps_temp"
