"""
ID: ZGW
LANG: PYTHON3
TASK: berries
"""
import sys
import copy
sys.setrecursionlimit(100000)
fin = open ('berries.in.3', 'r')
lines = fin.readlines()
l1s = lines[0].split(" ")
N = int(l1s[0])
K = int(l1s[1])
Bs = list(map(int,lines[1].split(" ")))
Bs = sorted(Bs,reverse=True)

import math
def divide(s,dnum):
    if dnum == 0:
        return [s]
    """按整拆分,dnum:需要拆成的份数"""
    sd = s % dnum
    res = [math.floor(s / dnum)] * dnum
    if sd == 0:
        return res
    else:
        for i in range(int(sd)):
            res[i] +=1
        return res

def Avg(Bs, k):
    """
    k > len(Bs)
    sum(Bs) > k
    """
    if sum(Bs) < k:
        return 0
    r = k - len(Bs)
    if r<0:
        return 0
    if r==0:
        return sum(sorted(Bs,reverse=True)[int(k/2):])
    rBs = [r * s/min(Bs) for s in Bs]
    print(rBs)
    rs = [[math.floor(s / sum(Bs)), s % sum(Bs), int(s / r)] for s in rBs]
    rs = sorted(rs, key=lambda x: (x[1]), reverse=True)
    print(rs)
    ss = 0
    # print(rs)
    for s in rs:
        ss += s[0]
    for s in range(r - ss):
        rs[s][0] += 1
    # print(rs)
    ds = []
    for s in rs:
        ds += divide(s[2], s[0] + 1)
    ds = sorted(ds, reverse=True)
    print(ds)
    return sum(ds[int(k / 2):])

MMs = []
# Basks = []
# for i in range(0,N):
#     Basks.append(Bs[i])
#     CurBasks = copy.deepcopy(Basks)
#     t = Avg(CurBasks, K)
#     MMs.append(t)
    # print(S,i,t,Basks,CurBasks)

Avg(Bs=[150,30,15,15], k=8)

def Solve():
    return str(max(MMs))

result = Solve()

fout = open ('berries.out', 'w')
# for r in range(len(results)-1):
#     fout.write (str(results[r]) + '\n')
# fout.write (str(results[len(results)-1]))
fout.write(result)
fout.close()