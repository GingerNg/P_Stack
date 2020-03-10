#!/bin/bash

#nginx log path
NginxLog=/dep/go/log/nginx/go_access.log

while true
do

#busi log path
day=$(date '+%Y%m%d')
BusiLog=/dep/go/log/busi/busi.log.$day

#interval, execute monitor every minute, 60s, not used for now
Interval=60

##monitor aspects##
#service process count
countService=$(ps -ef | grep dds-server | wc -l)

#begin time(1 minute ago) nginx log format
BeginTimeNginx=$(date -d '1 minute ago' '+%d/%b/%Y:%H:%M:%S')
#successful QPS count
countQps=$(tac $NginxLog | awk -v BeginTimeN=$BeginTimeNginx 'BEGIN{numOK=0;numFail=0}{split($4,array,"[");if(array[2]<=BeginTimeN){exit}else if($9==200 && $7=="/api/dmp/orderRouteQry/"){numOK++} else{numFail++}}END{print numOK;print numFail;exit}')

#redis process count
redisNum=$(ps -ef | grep redis | wc -l)

#begin time(1 minute ago) busi log format
BeginTimeBusi=$(date -d '1 minute ago' '+%H%M%S')
#demand request count
reqCount='0 0 0'
if [  -d $BusiLog ];then
    reqCount=$(tac $BusiLog | awk -v BeginTimeB=$BeginTimeBusi -F'|@|' 'BEGIN{total=0;supCache=0;demCache=0}{if($4<=BeginTimeB){exit} else if($2=='22' || $2=='23') {total++; supCache++}else if($2=='24'){total++; demCache++}} END {print total;print supCache;print demCache;exit}')
fi

echo $countService $countQps $redisNum $reqCount $(date '+%H%M%S') > ./out 
sleep $Interval

done
