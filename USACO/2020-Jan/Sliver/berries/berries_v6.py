"""
ID: ZGW
LANG: PYTHON3
TASK: berries
"""
import sys
import copy
sys.setrecursionlimit(100000)
fin = open ('berries.in.2', 'r')
lines = fin.readlines()
l1s = lines[0].split(" ")
N = int(l1s[0])
K = int(l1s[1])
Bs = list(map(int,lines[1].split(" ")))
Bs = sorted(Bs,reverse=True)

import math
def divide(s,dnum):
    """按整拆分,dnum:需要拆成的份数"""
    sd = s % dnum
    res = [math.floor(s / dnum)] * dnum
    if sd == 0:
        return res
    else:
        for i in range(sd):
            res[i] +=1
        return res

def SplitBask(Basks):
    """"""
    E = Basks[0]
#     print(E)
    newE = divide(sum(E),len(E)+1)
    del Basks[0]
    Basks.append(newE)
    Basks = sorted(Basks, key=lambda x:x[-1],reverse=True)
    return Basks

def Up(Basks):
    Basks = copy.deepcopy(Basks)
    Basks = SplitBask(Basks)
    Basks = SplitBask(Basks)
    return Basks

def CalT(Basks):
    Bas = []
    for B in Basks:
        Bas += B
    Bas = sorted(Bas,reverse=True)
    return sum(Bas[int(len(Bas)/2):])

MMs = []
MaxM = 0
Basks = []

j = 0 # ?<ST<K
# Flag = True
# while(Flag):
#     Basks.append([Bs[j]])
# Bs.append(0)

LBasks = []
LAvgs = []
LLs = []
S = 0
for i in range(j,min(N,K)):
    S += Bs[i]
    Basks.append([Bs[i]])
    LAvgs.append(S/2)
    # LLs.append(i+1)
    LBasks.append(copy.deepcopy(Basks))
MaxM = 0
curMaxM = CalT(Basks)

k = 0

startI = 0
endI = min(N,K)

for i in range(endI-1,startI,-1):
    d = K - (i+1)
    if d <= 0:
        continue
    else:
        # LLs[i] = K
        for j in range(d):
            LBasks[i] = SplitBask(LBasks[i])
        t = CalT(LBasks[i])
        curMaxM = max(curMaxM, t)
    if curMaxM>MaxM:
        MaxM = curMaxM
        cur = startI
        # print(MaxM)
        # 缩小X
        while(LAvgs[cur] < MaxM):
            # print(LAvgs[cur])
            cur += 1
        startI = cur


def Solve():
    return str(curMaxM)

result = Solve()

fout = open ('berries.out', 'w')
# for r in range(len(results)-1):
#     fout.write (str(results[r]) + '\n')
# fout.write (str(results[len(results)-1]))
fout.write(result)
fout.close()