

"""
ID: ZGW
LANG: PYTHON3
TASK: berries
"""
import sys
sys.setrecursionlimit(100000)
fin = open ('berries.in', 'r')
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

def SplitBask(Basks):
    Basks = copy.deepcopy(Basks)
    E = Basks[0]
#     print(E)
    newE = divide(sum(E),len(E)+1)
    del Basks[0]
    Basks.append(newE)
    Basks = SortBask(Basks)
    return Basks

def MergeBask(Basks):
    Basks = copy.deepcopy(Basks)
    Basks = sorted(Basks, key=lambda x: (len(x),-x[-1]))
    E = Basks[-1]
    if len(E) == 1:
        return Basks,False
    newE = merge(E)
    del Basks[-1]
    Basks.append(newE)
    Basks = SortBask(Basks)
    return Basks,True

def Up(Basks):
    """增加篮子"""
    Basks = copy.deepcopy(Basks)
    Basks = SplitBask(Basks)
    Basks = SplitBask(Basks)
    Bas = []
    for B in Basks:
        Bas += B
    Bas = sorted(Bas,reverse=True)
    return sum(Bas[int(len(Bas)/2):]),Basks

def Right(Basks,remainBs):
    """增加新的树"""
    if len(remainBs)<1:
        return 0,Basks,remainBs
    Basks = copy.deepcopy(Basks)
    remainBs = copy.deepcopy(remainBs)
    Basks,Flag = MergeBask(Basks)
    if Flag:
        Basks.append([remainBs[0]])
        # Basks.append([remainBs[1]])
        del remainBs[0]
        # del remainBs[0]
        Bas = []
        for B in Basks:
            Bas += B
        Bas = sorted(Bas,reverse=True)
        return sum(Bas[int(len(Bas)/2):]),Basks,remainBs
    else:
        return 0,Basks,remainBs



Basks = [divide(Bs[0],2)]
remainBs = Bs[1:]


k = 2
n = 1
MMs = []
while(k<K or n<N):
    if k<K:
        ut,uBasks = Up(Basks)
    else:
        ut = 0
    if n < N:
        rt,rBasks,rremainBs = Right(Basks,remainBs)
    else:
        rt = 0
    if ut > rt:
        Basks = uBasks
        k += 2
    else:

        Basks = rBasks
        remainBs = rremainBs
        n +=1

    if k == K:
        print(max(ut,rt),Basks)
        MMs.append(max(ut,rt))

def Solve():
    return str(max(MMs))

result = Solve()

fout = open ('berries.out', 'w')
# for r in range(len(results)-1):
#     fout.write (str(results[r]) + '\n')
# fout.write (str(results[len(results)-1]))
fout.write(result)
fout.close()