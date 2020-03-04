"""
ID: simith
LANG: PYTHON3
TASK: race
"""
fin = open ('race.in', 'r')
lines = fin.readlines()
K = int(lines[0].split(" ")[0])
N = int(lines[0].split(" ")[1])
Hs = []
for i in range(N):
    Hs.append(int(lines[i+1].strip()))
print((Hs))
def UpDownDist(max_s,H):
    return (1+max_s)*(max_s)/2 + (max_s-1+H)*max(0,(max_s-H))/2

import math
MaxS = int(math.pow(K,1/2))-1

def GetMaxSpeed(H):
    global MaxS
    # print(MaxS)
    # print("range",int(math.pow(K,1/2))-1,int(math.pow(2*K,1/2))+2)
    while UpDownDist(MaxS,H) <=K:
        MaxS += 1
    # MaxS -= 1
    return MaxS - 1

    # for max_s in range(int(math.pow(K,1/2))-1,int(math.pow(2*K,1/2))+2):
    #     if UpDownDist(max_s,H) > K:
    #         return max_s - 1

def GetTime(H):
    max_s = GetMaxSpeed(H)
    # print(max_s)
    # if max_s < H:
    #     return max_s
    # else:
    updowndist = UpDownDist(max_s,H)
    residuedist1 = K - updowndist
    pt1 = residuedist1/max_s
    residuedist2 = residuedist1 % max_s
    # pt2 =  residuedist2/H
    print(H, updowndist, max_s)
    if residuedist2 > 0:
        return max_s+max(0,max_s-H) + pt1 + 1

    # if (K - updowndist) % max_s > 0:
    #     return max_s+max_s-H+1 + (K - updowndist) / max_s +1
    return max_s+max(0,max_s-H) + pt1



def Solve():
    result = []
    HHs = {}
    for h in range(100001):
        HHs[h] = int(GetTime(h))
    for H in Hs:
        result.append(HHs[H])
    return result

results = Solve()

fout = open ('race.out', 'w')
for r in range(len(results)-1):
    fout.write (str(results[r]) + '\n')
fout.write (str(results[len(results)-1]))
# fout.write(result)
fout.close()