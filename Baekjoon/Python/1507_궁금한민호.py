'''
55
'''

import sys
sys.stdin = open('1507.txt', 'r')
import heapq


N = int(input())
weights = [list(map(int, input().split())) for _ in range(N)]
# print(weights)
# print(sum([6, 2, 9, 4, 16, 18]))

# weight이 가장 작은 것을 기준으로 i-j 정보와 함께 넣는다.
edges = []
for i in range(N - 1):
    for j in range(i + 1, N):
        heapq.heappush(edges, (weights[i][j], i, j))

inf = float('inf')
new_board = [[inf] * N for _ in range(N)]
result = 0

while edges:
    v, s, e = heapq.heappop(edges)
    print(v, s, e)
    temp = []
    heapq.heappush(temp, inf)

    for k in range(N):
        if s == k or e == k:
            continue
        else:
            if new_board[s][k] == inf or new_board[s][k] == inf:
                continue
            heapq.heappush(temp, new_board[s][k] + new_board[k][e])
    tt = heapq.heappop(temp)
    if tt > v:
        result += v
        new_board[s][e] = new_board[e][s] = v
    else:
        new_board[s][e] = new_board[e][s] = tt

flag = True
for i in range(N - 1):
    for j in range(i + 1, N):
        if weights[i][j] != new_board[i][j]:
            flag = False
            break
    if flag is False:
        break

if flag is False:
    print(-1)
else:
    print(result)



'''
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
road = [[1]*N for _ in range(N)]
res = 0
# 플로이드 와샬
for z in range(N):
    for x in range(N):
        for y in range(N):
            if x == y or y == z or x == z:
                continue
            if board[x][y] > board[x][z] + board[z][y]:
                res = -1
            if board[x][y] == board[x][z] + board[z][y]:
                road[x][y] = 0
if res != -1:
    for x in range(N):
        for y in range(N):
            if road[x][y] == 1:
                res += board[x][y]
print(res//2)
'''