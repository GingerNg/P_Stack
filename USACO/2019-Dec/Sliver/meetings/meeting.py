"""
ID: gaox1
LANG: PYTHON3
TASK: meetings
"""
import time

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


def min_cows(Xs, Ds, L):
    """
    对剩余cow寻找最小gap
    """
    gap = L
    lrs = []
    for i in range(0, len(Ds) - 1):
        if abs(Xs[i] - Xs[i + 1]) < gap and Ds[i] > 0 and Ds[i + 1] < 0:
            lrs = [[i, i + 1]]
            gap = Xs[i + 1] - Xs[i]
        elif abs(Xs[i] - Xs[i + 1]) == gap and Ds[i] > 0 and Ds[i + 1] < 0:
            lrs.append([i, i + 1])
    return gap / 2, lrs


def hit_ops(Ws, Xs, Ds, N, L, N_hit, W_arrived, W_sum):
    arrived_index = []  # 本轮到达目的地的牛的列表
    gap, lrs = min_cows(Xs, Ds, L)
    #         print("gap",gap)
    ts = [gap for _ in range(len(Ds))]
    Xs = map(lambda x,y,z:x+y*z,Xs,Ds,ts)

    def is_arrived(X,D,W):
    
        for i in range(len(Ds)):
            Xs[i] += Ds[i] * ts  # 更新牛的位置
            if Xs[i] <= 0 or Xs[i] >= L:  # 判断牛是否到达
                W_arrived += Ws[i]
                arrived_index.append(i)
            #         print("Xs",Xs)
        if W_arrived >= W_sum / 2:
            return N_hit, W_arrived
    # 对相撞的牛更新方向
    dup_indexes = lrs
    for dup in dup_indexes:
        Ds[dup[0]] *= -1
        Ds[dup[1]] *= -1
        N_hit += 1
    for i in range(len(arrived_index)):
        del Ws[arrived_index[i] - i]
        del Ds[arrived_index[i] - i]
        del Xs[arrived_index[i] - i]
    return N_hit, W_arrived


def solve(Ws, Xs, Ds, N, L):
    #     print(Ws,Xs,Ds)
    ii = 0
    W_sum = sum(Ws)
    print("Wsum", W_sum)
    W_arrived = 0
    N_hit = 0
    while W_arrived <= (W_sum / 2.0):
        ii += 1
        N_hit, W_arrived = hit_ops(Ws, Xs, Ds, N, L, N_hit, W_arrived, W_sum)
    #         print(W_arrived)
    print("ii", ii)
    return N_hit

res = solve(sorted_Ws, sorted_Xs, sorted_Ds, N_cow, L)
print(res)
fout = open('meetings.out', 'w')
fout.write(str(res) + '\n')
fout.close()
print(time.time() - s)