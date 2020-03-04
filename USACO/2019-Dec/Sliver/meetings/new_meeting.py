"""
ID: gaox1
LANG: PYTHON3
TASK: meetings
"""
import time
import numpy as np

s = time.time()
fin = open('meetings1.in', 'r')
lines = fin.readlines()

N_cow, L = map(int, lines[0].split())
# print(N_cow,L)

Ws_cow = []
Xs_cow = []
Ds_cow = []
# W_sum = 0
for i in range(1, len(lines)):
    wxd = list(map(int, lines[i].strip().split(" ")))
    #     S_cow.append(wxd)
    #     W_sum += wxd[0]
    Ws_cow.append(wxd[0])
    Xs_cow.append(wxd[1])
    Ds_cow.append(wxd[2])


def sort(A, B, C):
    # 先按 x[0] 进行排序，若 x[0] 相同，再按照 x[1] 排序
    zipped = zip(A, B, C)
    sort_zipped = sorted(zipped, key=lambda x: (x[0], x[1]))
    result = zip(*sort_zipped)
    x_axis, y_axis, z_axis = [list(x) for x in result]
    #     print(x_axis,y_axis,z_axis)
    return x_axis, y_axis, z_axis


sorted_Xs, sorted_Ws, sorted_Ds = sort(Xs_cow, Ws_cow, Ds_cow)

xs = np.array([0]+sorted_Xs+[L]).astype("float64")
vs = np.array([-1]+sorted_Ds+[1]).astype("float64")
ws = np.array([0]+sorted_Ws+[0]).astype("float64")
#
#
# print(np_Xs)
# print(np_Vs)
# print(np_Ws)
# W = 0
W_sum = sum(ws)
min_gap = np.min(np.diff(xs))
xs += vs * (min_gap / 2)
W = sum(ws[np.where(xs <= 0)]) + sum(ws[np.where(xs >= L)])
# print(xs)
N_hit = 0

def getts(vs,xs):
    vd = np.diff(vs)
    # np.where(vd==np.min(vd))[0]
    xd = np.diff(xs)
    gap_xd = np.where(vd==-2)
    xd = xd[gap_xd]
    xd = xd[xd > 0]
    if len(xd)>0:
        min_gap = np.min(xd)
    else:
        min_gap = L
    # print("min_gap",min_gap)
    return min_gap


while W_sum/2 > W:
    # print(xs)
    # hit
    di = np.diff(xs)  # 计算数组的相邻元素之间的差异
    poses = np.where(di==0)[0] # hit
    # for p in poses:
    #     print(p[0])
    cvs = np.ones(N_cow+2)
    for p in poses:
        cvs[p] = -1
        cvs[p+1] = -1
        N_hit += 1

    vs = vs * cvs
    min_gap = getts(vs,xs)
    # min_gap = 1
    xs += vs * (min_gap / 2)
    W = sum(ws[np.where(xs <= 0)]) + sum(ws[np.where(xs >= L)])
    # print(W)
    # print(N_hit)

print(N_hit)


# res = solve(sorted_Ws, sorted_Xs, sorted_Ds, N_cow, L)
# print(res)
# fout = open('meetings.out', 'w')
# fout.write(str(res) + '\n')
# fout.close()
print(time.time() - s)