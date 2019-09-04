from itertools import combinations

def start_virus(arr, temp_combinations):
    for temp_combi in temp_combinations:
        y, x = temp_combi
        arr[y][x] = 2
    return arr

def spread_virus(arr, temp_combinations):
    def_time_cnt = 0
    queue = []
    for temp in temp_combinations:
        queue.append(temp)
    while queue:
        def_time_cnt += 1
        for _ in range(len(queue)):
            xy = queue.pop(0)
            for dy, dx in d:
                iy = xy[0] + dy
                ix = xy[1] + dx
                if 0 <= iy < N and 0 <= ix < N and arr[iy][ix] == 0:
                    arr[iy][ix] = 2
                    queue.append((iy, ix))
    return def_time_cnt, arr

def survive_zero(arr):
    def_survive_cnt = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 0:
                def_survive_cnt += 1


    return def_survive_cnt


d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
mymap = [list(map(int, input().split())) for _ in range(N)]
virus_candidates = []
for y in range(N):
    for x in range(N):
        if mymap[y][x] == 2:
            virus_candidates.append((y, x))
virus_combinations = list(combinations(virus_candidates, M))
result_time = []
survive_space = []
for candidate in virus_candidates:
    y, x = candidate
    mymap[y][x] = 0

for virus_combination in virus_combinations:
    temp_map = [i[:] for i in mymap]
    temp_map = start_virus(temp_map, virus_combination)
    time_cnt, temp_map = spread_virus(temp_map, virus_combination)
    result_time.append(time_cnt-1)
    survive_cnt = survive_zero(temp_map)
    survive_space.append(survive_cnt)

name_result = []
for idx in range(len(result_time)):
    if survive_space[idx] == 0:
        name_result.append(idx)

final_result = []
for idx2 in name_result:
    final_result.append(result_time[idx2])

if min(survive_space) > 0:
    print(-1)
elif min(survive_space) == 0:
    print(min(final_result))

