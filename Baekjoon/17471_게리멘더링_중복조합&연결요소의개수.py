import sys
sys.stdin = open('17471.txt', 'r')
import itertools
input = sys.stdin.readline

N = int(input()) # 구역의 개수
neighbors = [0] + list(map(int, input().split())) # 인구수

# N개의 줄에 각 구역과 인접한 구역의 정보
# 각 정보의 첫 번째 정수는
# 그 구역과 인접한 구역의 수
# 이후 인접한 구역의 번호

adj_list = [[] for _ in range(N+1)] # 인접리스트
for i in range(1, N+1): # 1부터 시작해서 N+1까지이다. 인덱스 반드시 확인해주어야한다.
    print(i)
    se = list(map(int, input().split()))

    for j in range(1, se[0]+1):
        adj_list[i].append(se[j])

# 1. 두 그룹으로 나눌 수 있는 경우의 수를 구한다.
mylist = [i for i in range(1, N)]
temp = []
for i in itertools.product(mylist, repeat=2):
    if sum(i) == N:
        temp.append(i)
# (1,5) (2,4) (3,3) (4,2) (5,1)

# 2. 경우의 수만큼 부분집합을 구한다.
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

# 3. 부분 집합을 돌리면서 딱 2로 나눠지는 부분집합인 경우(한 그룹의 자식노드가 다른 그룹에 있는지 없는지 판단하면서)면,
# 그 부분집합에 따라 인구수 차이를 계산한다

# 부분집합안에서 그래프가 완성되는지 안되는지 다른 그룹에 속한 구역을빼고 모두 방문하는 함수
def check(ii):
    global avaliable, visited, total_visited

    if visited[ii] == False:
        visited[ii] = True
        for adj in adj_list[ii]:
            if total_visited[adj] == True:
                check(adj)
    return


# 인구수 차이를 구하기 위한 함수
def find(f, s):
    onecnt = 0
    secondcnt = 0
    for i in f:
        onecnt += neighbors[i]
    for j in s:
        secondcnt += neighbors[j]
    return onecnt, secondcnt


avaliable = []
mymin = 999999999
for group in groups:
    cnt = 0

    for grou in group:
        visited = [True] + [False] * N
        total_visited = [True] + [False] * N

        # 자신의 그룹에 해당하는 자식만 방문하기 위한 total_visitied
        for c in grou:
            total_visited[c] = True

        # 자신의 그룹에 해당하는 자식만 방문하기로한다.
        for i in grou:
            if visited[i] == False:
                cnt += 1
                check(i)

    if cnt == 2:
        first, second = find(group[0], group[1])
        diff = abs(first - second)
        if mymin > diff:
            mymin = diff

# 결과 출력
if mymin == 999999999:
    print(-1)
else:
    print(mymin)