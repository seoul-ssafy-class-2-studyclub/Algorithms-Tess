import sys
# sys.stdin = open('17471.txt', 'r')
import itertools
input = sys.stdin.readline

# 구역의 개수
'''
6
'''
N = int(input())

# 구역의 인구가 1번 구역부터 N번 구역
'''
5 2 3 4 1 2
'''
neighbors = [0] + list(map(int, input().split()))
# print(neighbors)

# N개의 줄에 각 구역과 인접한 구역의 정보
'''
2 개수 2 4 인접 구역 번호 1이 인접한 것
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
'''

# 1. 각 정보의 첫 번째 정수는
# 그 구역과 인접한 구역의 수
# 이후 인접한 구역의 번호

adj_list = [[] for _ in range(N+1)] # 1부터 6까지
for i in range(1, N):
    se = list(map(int, input().split()))

    for j in range(1, se[0]+1):
        adj_list[i].append(se[j]) # 한방향으로 먼저 진행
    # [[], [2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], []]
# print(adj_list)

# 6구역이면,

mylist = [i for i in range(1, N)]
# print(mylist)
temp = []
for i in itertools.product(mylist, repeat=2):
    if sum(i) == N:
        temp.append(i)
# print(temp)
# (1,5) (2,4) (3,3) (4,2) (5,1)
# 중복이 존재하는 부분집합으로 접근후

candidates = [i for i in range(1, N+1)]

groups = []
for i, j in temp:
    firstgroup = list(itertools.combinations(candidates, i))
    secondgroup = []
    for first in firstgroup:
        second = []
        for one in candidates:
            if one not in first:
                second.append(one)
        groups.append((first, second))


# 부분집합안에서 그래프가 완성 되었는지 안되었는지 dfs/bfs
def check(ii):
    global avaliable, visited

    if visited[ii] == False:
        visited[ii] = True
        for adj in adj_list[ii]:
            check(adj)
    return


def find(f, s):
    onecnt = 0
    secondcnt = 0
    for i in f:
        onecnt += neighbors[i]
    for j in s:
        secondcnt += neighbors[j]

    return onecnt, secondcnt


avaliable = []
mymin = 99999
for group in groups:
    cnt = 0
    for grou in group:
        # print(grou)
        visited = [True] + [False] * N
        for i in grou:
            if visited[i] == False:
                cnt += 1
                check(i)
        # print(visited)

    if cnt == 2: # 한 그룹에서 시작해서 모든 그룹을 도는가? 그걸 확인해야한다. 확인하는 방법 찾기
        # avaliable.append(group)
        first, second = find(group[0], group[1])
        diff = abs(first - second)
        # print(group[0], group[1])
        if mymin > diff:
            mymin = diff
# print(len(avaliable))
# print(mymin)

if mymin == 99999:
    print(-1)
else:
    print(mymin)
# 나눈후에 한 그룹에서 시작해서 모든 그룹을 도는지 확인하고, 모든 그룹을 돈다면 가능한 부분집합이므로,
# 인구 차이를 센 후
# 계속 update

# output
# 첫째 줄에 백준시를 두 선거구로 나누었을 때,
# 두 선거구의 인구 차이의 최솟값을 출력한다.
# 두 선거구로 나눌 수 없는 경우에는 -1을 출력한다.