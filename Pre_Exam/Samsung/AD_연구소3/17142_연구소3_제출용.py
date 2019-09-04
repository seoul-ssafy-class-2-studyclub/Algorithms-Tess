from itertools import combinations

def check(check_arr):
    flag = 1
    for cy in range(N):
        for cx in range(N):
            if check_arr[cy][cx] == 0:
                flag = 0
                return flag
    return flag

def spreadvirus(arr, combi, zeros):
    time_cnt = 0
    queue = []
    for com in combi:
        queue.append(com)

    while queue:
        time_cnt += 1
        for _ in range(len(queue)):
            yx = queue.pop(0)

            for dy, dx in d:
                iy = yx[0] + dy
                ix = yx[1] + dx
                if 0 <= iy < N and 0 <= ix < N:
                    if arr[iy][ix] == 0:
                        zeros -= 1
                        arr[iy][ix] = 3
                        queue.append((iy, ix))
                        if zeros == 0:
                            return time_cnt

                    if arr[iy][ix] == 2:
                        arr[iy][ix] = 3
                        queue.append((iy, ix))
    if zeros > 0:
        return -1

d = [(0,1), (0,-1), (1,0), (-1,0)]
N, M = map(int, input().split())
tempmap = [ list(map(int, input().split())) for _ in range(N) ]
temp_xy = []
for y in range(N):
    for x in range(N):
        if tempmap[y][x] == 2:
            temp_xy.append((y, x))
temp_combinations = list(combinations(temp_xy, M))
result_list = []
for tempcombi in temp_combinations:
    case_map = [i[:] for i in tempmap]
    for tempy, tempx in tempcombi:
        case_map[tempy][tempx] = 3

    myzeros = 0
    for y in range(N):
        for x in range(N):
            if case_map[y][x] == 0:
                myzeros += 1
    cnt = spreadvirus(case_map, tempcombi, myzeros)
    if cnt == -1:
        continue
    else:
        result_list.append(cnt)
result = 0
for y in range(N):
    for x in range(N):
        if tempmap[y][x] == 0:
            if result_list == []:
                result = -1
            else:
                result = min(result_list)
print(result)
