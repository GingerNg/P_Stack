import subprocess
import os
from subprocess import Popen, PIPE

cmd = "tac /dep/go/log/busi/busi.log.20170510 | awk -F'\|@\|' 'BEGIN{num=0}{if($3<125900){exit} else if ($11=='24') {num++}} END{print num}'"
print "start process"
#out = os.popen(cmd).readline()
#p1 = subprocess.Popen(["tac /dep/go/log/busi/busi.log.20170510"], stdout=PIPE,shell=True)
#p2 = subprocess.Popen(["awk", "-F'\|@\|' 'BEGIN{num=0}{if($3<125900){exit} else if ($11=='24') {num++}} END{print num}'"], stdin=p1.stdout, stdout=PIPE,shell=True)
#p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
p = Popen(cmd, shell=True,stdout=PIPE).communicate()[0]
print p
print p
print p
    
#output = p2.communicate()[0]
#output = subprocess.check_output(cmd,shell=True)
#print output
#p = subprocess.Popen(cmd, shell=True)
#p.wait()
#out = os.popen(cmd).readline()
#print out
