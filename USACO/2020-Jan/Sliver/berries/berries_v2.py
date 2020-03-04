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
Basks = []

j = 0 # ?<ST<K
# Flag = True
# while(Flag):
#     Basks.append([Bs[j]])
Bs.append(0)
for i in range(j,min(N,K)):
    Basks.append([Bs[i]])
    CurBasks = copy.deepcopy(Basks)
    S = len(CurBasks)
    if len(CurBasks)%2 != 0:
        CurBasks = SplitBask(CurBasks)
        S +=1
    if S<K:
        for k in range(S+2,K+1,2):
            CurBasks = Up(CurBasks)
            print(CurBasks)
            t = CalT(CurBasks)
            if t < Bs[i+1]:
                break
        t = CalT(CurBasks)
    else:
        t = CalT(CurBasks)
    MMs.append(t)
    print(S,i,t,Basks,CurBasks)

def Solve():
    return str(max(MMs))

result = Solve()

fout = open ('berries.out', 'w')
# for r in range(len(results)-1):
#     fout.write (str(results[r]) + '\n')
# fout.write (str(results[len(results)-1]))
fout.write(result)
fout.close()