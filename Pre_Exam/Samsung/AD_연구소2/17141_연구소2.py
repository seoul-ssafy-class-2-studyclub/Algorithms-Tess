import sys
sys.stdin = open('17141.txt', 'r')
from pprint import pprint
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
        def_time_cnt += 1 # 한번들은 queue를 시작할때 += 1을 한다.
        for _ in range(len(queue)): # 들은 queue들의 원소가 다 소진될때까지 pop을 한다.
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

'''

5

'''

# 0 빈칸 1 벽 2 바이러스를 놓을 수 있는 위치
# N 행 열 M 바이러스 개수


d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
mymap = [list(map(int, input().split())) for _ in range(N)]
# 1. 바이러스를 2에 놓을 수 있는 모든 경우의 수를 찾는다. -> 2가 있는 곳의 좌표를 찾는다. 그리고 (중복조합)을 찾는다. M개의 수를 가진!
virus_candidates = []
for y in range(N):
    for x in range(N):
        if mymap[y][x] == 2:
            virus_candidates.append((y, x))

#print(virus_candidates)
virus_combinations = list(combinations(virus_candidates, M))
#print(virus_combinations)
result_time = []
survive_space = []

# 1-1. 모든 2가 있는 곳을 0으로 바꾸고, 시작할 준비를 한다. 완료
for candidate in virus_candidates:
    y, x = candidate
    mymap[y][x] = 0
#print(mymap)

for virus_combination in virus_combinations:
    # 1-2. 새로운 보드를 딥카피한다. 이 경우 시간을 줄이기 위해 딥카피 모듈을 사용하지 않는다. 완료
    temp_map = [i[:] for i in mymap]

    #print(temp_map)

    # 2. 찾은 조합에 바이러스 2를 놓는다. 완료
    temp_map = start_virus(temp_map, virus_combination)

    # 3. 바이러스를 놓고 퍼트린다.
    # 4. 상하좌우를 보면서 0에만 바이러스를 퍼트린다. -> BFS로 진행할 것
    # 한 번 퍼트릴때 카운트 1을 해주는데, 이건 각 2가 담고있는 정보가 한 번 나올때 동시에 카운트되는 시간을 말한다.

    #pprint(temp_map)
    time_cnt, temp_map = spread_virus(temp_map, virus_combination)
    #pprint(temp_map)
    # 5. 시간카운트는 result_time 리스트에 추가한다.
    result_time.append(time_cnt-1)

    # 6. 변화한 보드 전체를 돌면서 0이 몇개 있는지 카운트하고, survive_space 리스트에 추가한다.
    survive_cnt = survive_zero(temp_map)
    survive_space.append(survive_cnt)

# 7. 모든 result_time와 survive_space이 채워졌을때, 아래와 같은 검사를 통해 결과를 도출할건데,
# 8. survive_space 리스트의 min() 을 구하고 min이 0보다 큰 경우 모든 0이 2가 되는 경우가 없다는 뜻이므로 -1을 출력하고,
# 9. 그렇지 않은 경우에는 result_time의 min을 출력한다.


# 0이 하나도 없이 spread된 경우의 최단시간을 res로 받아야한다.
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

