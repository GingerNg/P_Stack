

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

def SortBask(Basks):
    return sorted(Basks, key=lambda x: (sum(x)/len(x),sum(x)), reverse=True)

def SplitBask(Basks):
    Basks = sorted(Basks, key=lambda x: (len(x),x[-1]), reverse=True)
    E = Basks[-1]
    del Basks[-1]

    if len(E)>1:
        return []
    for s in range(len(E)):
        Basks = SortBask(Basks)
        B = Basks[0]
        del Basks[0]
        # 拆分之后可能排到单个元素的后面
        # 每次拆分，都会接近平均值
        # 当固定Trees个数时，篮子越多越平均
        # 当固定篮子个数，拆分最大值，赶走最小值，拆分出来的数要大于最小值
        # 如果一个被拆分后的数合并后，那么它一定比在它前面的同len的数要大；
        newB = divide(sum(B), len(B) + 1)  #　总是拆分最大的那个,　经过拆分过的Tree　已经是“平均”的
        Basks.append(newB)
        # Basks = SortBask(Basks)
#     print(E)
    return Basks

def CalT(Basks):
    Bas = []
    for B in Basks:
        Bas += B
    Bas = sorted(Bas,reverse=True)
    return sum(Bas[int(len(Bas)/2):])


def Left(Basks):
    """
    k > len(Bs)
    sum(Bs) > k
    """
    # Basks = sorted(Basks, key=lambda x: x[-1], reverse=True)
    Basks = copy.deepcopy(Basks)
    Basks = SplitBask(Basks)
    t = CalT(Basks)
    # Basks = sorted(Basks, key=lambda x: (sum(x)), reverse=True)
    return t,Basks

MMs = []
Basks = []
for i in range(N):
    Basks.append([Bs[i]])

if len(Basks) < K:
    for i in range(K-len(Basks)):
        print(Basks)
        B = Basks[0]
        del Basks[0]
        newB = divide(sum(B), len(B) + 1)
        Basks.append(newB)
        Basks = SortBask(Basks)
elif len(Basks) > K:
    Basks = Basks[0:K]

t = CalT(Basks)
# Basks = sorted(Basks, key=lambda x: (sum(x)), reverse=True)
MMs.append(t)

print(Basks)
while len(Basks)>1:
    CurBasks = copy.deepcopy(Basks)
    t,CurBasks = Left(CurBasks)
    MMs.append(t)
    Basks = CurBasks
    # print(Basks)
    # print(S,i,t,Basks,CurBasks)
# print(Basks)
# Avg(Bs=[150,30,15,15], k=8)

def Solve():
    return str(max(MMs))

result = Solve()

fout = open ('berries.out', 'w')
# for r in range(len(results)-1):
#     fout.write (str(results[r]) + '\n')
# fout.write (str(results[len(results)-1]))
fout.write(result)
fout.close()