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
    sd = s % dnum
    res = [math.floor(s / dnum)] * dnum
    if sd == 0:
        return res
    else:
        for i in range(sd):
            res[i] +=1
        return res

def SortBask(Basks):
    return sorted(Basks, key=lambda x: (x[-1],sum(x)), reverse=True)

def one_step(Basks,remainBs):
    E = Basks[0]
    newE = divide(sum(E),len(E)+1)
    if newE[-1] < remainBs[0]:
        Basks.append([remainBs[0]])
    else:
        del Basks[0]
        Basks.append(newE)
        Basks = SortBask(Basks)
    return Basks,remainBs

def situation(Basks,remainBs):
    Basks, remainBs = one_step(Basks, remainBs)
    Basks, remainBs = one_step(Basks, remainBs)
    Bas = []
    for B in Basks:
        Bas += B
    Bas = sorted(Bas, reverse=True)
    return sum(Bas[int(len(Bas)/2):]),Basks,remainBs


def situation1(Basks,remainBs):
    IsContinue = True
    if len(remainBs)<2:
        return 0,Basks,remainBs,False
    Basks = copy.deepcopy(Basks)
    remainBs = copy.deepcopy(remainBs)
    Basks.append([remainBs[0]])
    Basks.append([remainBs[1]])
    del remainBs[0]
    del remainBs[0]
    Bas = []
    for B in Basks:
        Bas += B
#     print(Bas)
    Bas = sorted(Bas,reverse=True)
    Basks = SortBask(Basks)
    # if Basks
    return sum(Bas[int(len(Bas)/2):]),Basks,remainBs,IsContinue

def Situation2(Basks,remainBs):
    IsContinue = True
    if len(remainBs)<1:
        return 0,Basks,remainBs,False
    Basks = copy.deepcopy(Basks)
    remainBs = copy.deepcopy(remainBs)
    E = Basks[0]
    newE = divide(sum(E),len(E)+1)
    del Basks[0]
    Basks.append(newE)
    Basks.append([remainBs[0]])
    del remainBs[0]
    Bas = []
    for B in Basks:
        Bas += B
#     print(Bas)
    Bas = sorted(Bas,reverse=True)
    Basks = SortBask(Basks)
    if Bas[-1] < remainBs[0]:
        IsContinue = False
    return sum(Bas[int(len(Bas)/2):]),Basks,remainBs,IsContinue

def Situation3(Basks,remainBs):
    IsContinue = True
    Basks = copy.deepcopy(Basks)
    E = Basks[0]
    newE = divide(sum(E),len(E)+1)
    del Basks[0]
    Basks.append(newE)
    Basks = SortBask(Basks)
    E = Basks[0]
    newE = divide(sum(E),len(E)+1)
    del Basks[0]
    Basks.append(newE)
    Basks = SortBask(Basks)
    Bas = []
    for B in Basks:
        Bas += B
    Bas = sorted(Bas,reverse=True)
    if Bas[-1] < remainBs[0]:
        IsContinue = False
    return sum(Bas[int(len(Bas)/2):]),Basks,remainBs,IsContinue


if Bs[0]/2 > Bs[1]:
    Basks = [divide(Bs[0],2)]
    remainBs = Bs[1:]
else:
    Basks = [[Bs[0]], [Bs[1]]]
    remainBs = Bs[2:]

MM = 0
MMs = {}
for k in range(0,K + 1,2):
    MMs[k] = 0
MMs[2] = 0
def one_epoch(Basks,remainBs,loops):
    """每次迭代"""
    # print(loops)

    # 1.加两个新树
    t1, Basks1, remainBs1,IsContinue1 = situation1(Basks, remainBs)
    print(loops,t1,Basks1,remainBs1,IsContinue1)
    # 2.拆一颗老的，加一颗新的
    t2, Basks2, remainBs2,IsContinue2 = Situation2(Basks, remainBs)
    print(loops, t2, Basks2,remainBs2,IsContinue2)
    # 3 拆两个老的
    t3, Basks3, remainBs3,IsContinue3 = Situation3(Basks, remainBs)
    print(loops, t3, Basks3,remainBs3,IsContinue3)
    # t, Basks, remainBs = situation(Basks, remainBs)
    max_t = max([t1, t2, t3])
    max_tt = max(MMs[loops], max_t,MMs[loops-2])
    # if t1 == max_tt:
    # if len(list(set([t1, t2, t3]))) != 3:
    #     print(max_tt)
    print(max_tt)
    MMs[loops] = max_tt
    if t1 == max_tt:
        IsContinue1 &= True
    else:
        IsContinue1 = False
    if t2 == max_tt:
        IsContinue2 &= True
    else:
        IsContinue2 = False
    if t3 == max_tt:
        IsContinue3 &= True
    else:
        IsContinue3 = False

    loops += 2
    if loops > K:
        return
    if IsContinue1:
        one_epoch(Basks1, remainBs1, loops)
    # if t2 == max_tt:
    elif IsContinue2:
        one_epoch(Basks2, remainBs2, loops)
    # if t3 == max_tt:
    elif IsContinue3:
        one_epoch(Basks3, remainBs3, loops)


    # one_epoch(Basks, remainBs, loops)


one_epoch(Basks,remainBs,4)
print(MMs)
MM = MMs[K]
# for k in range(4, K + 1, 2):
#
#
#     MM = max([t1, t2, t3])
#     print(MM)
#     if t3 == MM:
#         Basks = Basks3
#         remainBs = remainBs3
#     if t2 == MM:
#         Basks = Basks2
#         remainBs = remainBs2
#     else:
#         Basks = Basks1
#         remainBs = remainBs1
#     print(Basks)

def Solve():
    return str(MM)

result = Solve()

fout = open ('berries.out', 'w')
# for r in range(len(results)-1):
#     fout.write (str(results[r]) + '\n')
# fout.write (str(results[len(results)-1]))
fout.write(result)
fout.close()