

"""
ID: ZGW
LANG: PYTHON3
TASK: berries
"""
import sys
sys.setrecursionlimit(100000)
fin = open ('berries.in.2', 'r')
lines = fin.readlines()
l1s = lines[0].split(" ")
N = int(l1s[0])
K = int(l1s[1])
Bs = list(map(int,lines[1].split(" ")))
Bs = sorted(Bs,reverse=True)
# print("Bs",Bs)
import math,copy
def divide(s,dnum):
    """按整拆分,dnum:需要拆成的份数"""
    if dnum == 0:
        return [s]
    sd = s % dnum
    res = [math.floor(s / dnum)] * dnum
    if sd == 0:
        return res
    else:
        for i in range(sd):
            res[i] +=1
        return res

def merge(s):
    return divide(sum(s),len(s)-1)

def SortBask(Basks):
    return sorted(Basks, key=lambda x: (x[-1],sum(x)), reverse=True)

def SplitBask(orgBasks,remainBs=[]):
    Basks = copy.deepcopy(orgBasks)
    if len(Basks) == 0:
        orgBasks.append([remainBs[0]])
        del remainBs[0]
        return orgBasks
    E = Basks[0]
#     print(E)
    newE = divide(sum(E),len(E)+1)
    del Basks[0]
    Basks.append(newE)
    Basks = SortBask(Basks)
    # Bas = []
    # for B in Basks:
    #     Bas += B
    # Bas = sorted(Bas,reverse=True)
    if len(remainBs)>1:
        if remainBs[0] >= Basks[-1][-1]:
            orgBasks.append([remainBs[0]])
            del remainBs[0]
            return orgBasks
        else:
            return Basks
    return Basks


def Up(Basks,remainBs):
    """增加篮子"""
    Basks = copy.deepcopy(Basks)
    Basks = SplitBask(Basks,remainBs)
    Basks = SplitBask(Basks,remainBs)
    return Basks

def CalT(Basks):
    Bas = []
    for B in Basks:
        Bas += B
    Bas = sorted(Bas,reverse=True)
    print(len(Bas))
    if len(Bas) == K:
        return sum(Bas[int(len(Bas)/2):])
    else:
        return 0

def MergeBask(Basks):
    Basks = copy.deepcopy(Basks)
    Basks = sorted(Basks, key=lambda x: (x[-1],-sum(x)),reverse=True)
    E = Basks[-1]
    # if len(E) == 1:
    #     return Basks,False
    newE = merge(E)
    del Basks[-1]
    Basks.append(newE)
    Basks = SortBask(Basks)
    return Basks

def Right(orgBasks,remainBs):
    """增加新的树"""
    Basks = sorted(orgBasks, key=lambda x: (-len(x),x[-1]), reverse=True)
    # while(Basks[-1][-1] <= remainBs[0]):
    Basks = MergeBask(Basks)
    Basks.append([remainBs[0]])
    del remainBs[0]
    return Basks

Basks = []
remainBs = Bs
k = 0
MMs = []
while(k<K):
    Basks = Up(Basks,remainBs)
    print(Basks)
    k += 2
n = len(Basks)
MMs.append(CalT(Basks))









# while(len(remainBs)>0):
#     Basks = Right(Basks,remainBs)
#     MMs.append(CalT(Basks))
# # while(n < N):
# #     Basks = Right(Basks,remainBs)
# #     n += 1
# print(n)
# MMs.append(CalT(Basks))
def Solve():
    return str(max(MMs))

result = Solve()
print(result)
fout = open ('berries.out', 'w')
# for r in range(len(results)-1):
#     fout.write (str(results[r]) + '\n')
# fout.write (str(results[len(results)-1]))
fout.write(result)
fout.close()