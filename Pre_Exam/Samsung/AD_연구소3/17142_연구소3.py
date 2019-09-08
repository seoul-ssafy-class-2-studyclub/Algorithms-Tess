import sys
sys.stdin = open('17142.txt', 'r')
from pprint import pprint
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
        for _ in range(len(queue)): # 같은 계층의 queue를 돌기위해서 queue안에서 뺀다.
            yx = queue.pop(0)

            for dy, dx in d:
                iy = yx[0] + dy
                ix = yx[1] + dx

                # zero를 제거했는지 안했는지가 문제에서 중요하기때문에 zero에 대한 정보를 미리 구해놓고 제어하는것이 필요한 문제
                if 0 <= iy < N and 0 <= ix < N: # 두가지 분기로 나뉘는데 0이있을때와 2가 있을때다.
                    if arr[iy][ix] == 0: # 0이있는 경우에는 3으로 바꾸고 append할 뿐만아니라 zero도 -1 해줘야 한다.
                        #print(zeros)
                        zeros -= 1 # 0을 없앨때만 줄여준다.
                        arr[iy][ix] = 3
                        queue.append((iy, ix))
                        if zeros == 0: # 0이 다 사라지는 경우에만 카운트를 반환
                            return time_cnt

                    if arr[iy][ix] == 2: # 2는 이미 바이러스를 말하고, 이 경우 활성화 시킨다.
                        arr[iy][ix] = 3 # 2는 zero가 아니므로 -1할 필요가 없다.
                        queue.append((iy, ix))
    if zeros > 0: # 0이 다 사라지지않고 큐가 끝났으므로 -1을 리턴한다.
        return -1

    # 5-1. BFS로 상하좌우 0과 2가있으면, 바이러스를 퍼트리고, 아니면 그냥 버려지도록 한다.
    # 5-2. 이때 한 번 queue가 시작되는 계층을 1초로 봐야하므로 queue의 for문 전에 time_cnt를 한다.
    # 6. 0이 존재하는지 보드를 검사하고,
    # 7. 0이 하나라도 있다면, 여태까지의 time_cnt는 필요없다. 그러므로 버린다.
    # 8. 0이 하나도 없는 시도의 time_cnt만 반환해서 바깥 리스트에 append한다.




d = [(0,1), (0,-1), (1,0), (-1,0)]
N, M = map(int, input().split())
tempmap = [ list(map(int, input().split())) for _ in range(N) ]

# 1. 2가 있는 좌표를 찾는다.
temp_xy = []
for y in range(N):
    for x in range(N):
        if tempmap[y][x] == 2:
            temp_xy.append((y, x))
# 2. 2가 있는 좌표에 대한 중복조합을 M개 만큼 구한다.
temp_combinations = list(combinations(temp_xy, M))


result_list = []
# 2-1. 구한 중복조합의 수만큼 for문을 돈다.
for tempcombi in temp_combinations:

# 3. 딥카피해서 사용할 보드를 준비한다.
    case_map = [i[:] for i in tempmap]

# 4. 중복조합의 좌표를 이용해 active할 virus를 3으로 설정한다.
# ** 앞으로 선택된 바이러스로 상하좌우 움직일때 바이러스가 될 0과 비활성화의 2는 3이 될 것이다.
    for tempy, tempx in tempcombi:
        case_map[tempy][tempx] = 3

    myzeros = 0
    for y in range(N):
        for x in range(N):
            if case_map[y][x] == 0:
                myzeros += 1 # zero의 수가 사라질때, 더이상 할 필요가 없으므로 멈추기 위한 제어용
    #print(myzeros)


# 5. 바이러스를 퍼트린다.
    cnt = spreadvirus(case_map, tempcombi, myzeros)
    #print(cnt)
    if cnt == -1:
        continue
    else:
        result_list.append(cnt)

# 9. 이렇게 해서 append할때, 리스트가 비었을 경우, 모든 0을 없애는 경우가 존재하지 않는 것이므로 -1을 출력
# 10. 리스트가 비지 않은 경우 리스트에서 가장 최소값을 출력
#print(result_list)
result = 0
for y in range(N):
    for x in range(N):
        if tempmap[y][x] == 0:
            if result_list == []:
                result = -1
            else:
                result = min(result_list)
print(result)
