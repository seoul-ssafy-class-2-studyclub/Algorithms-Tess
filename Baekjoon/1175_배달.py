## BFS

import sys

from pprint import pprint
sys.stdin = open('1175.txt', 'r')

import heapq
def solve(status):
    global nbd
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    visit = [[False]*M for _ in range(N)]
    visit[minsik[0]][minsik[1]] = True # 처음에는 항상 True 처리 하고 시작한다.
    q = []
    # 시작의 status는 4가지 경우가 있다.
    heapq.heappush(q, (0, 0, minsik, status))
    while q:
        Cs, mins, current, status = heapq.heappop(q)
        cury, curx = current[0], current[1]

        # if Cs == -2:
        #     return mins

        for i in range(4):
            if i != status:
                nxty, nxtx = direction[i][0], direction[i][1]
                nxty = nxty + cury
                nxtx = nxtx + curx

                if 0 <= nxty < N and 0 <= nxtx < M and visit[nxty][nxtx] == False and nbd[nxty][nxtx] != '#':
                    if nbd[nxty][nxtx] == '.':
                        heapq.heappush(q, (Cs, mins+1, (nxty, nxtx), i))
                        visit[nxty][nxtx] = True
                        continue

                    if nbd[nxty][nxtx] == 'C' and Cs == 0:
                        heapq.heappush(q, (Cs-1, mins+1, (nxty, nxtx), i))
                        nbd[nxty][nxtx] = '.'
                        visit[nxty][nxtx] = True
                        visit = [[False]*M for _ in range(N)]
                        continue

                    if nbd[nxty][nxtx] == 'C' and Cs == -1:
                        heapq.heappush(q, (Cs-1, mins+1, (nxty, nxtx), i))
                        nbd[nxty][nxtx] = '.'
                        visit[nxty][nxtx] = True
                        return mins+1
    return 1e9

N, M = map(int, input().split())
bd = [list(input()) for _ in range(N)]

flag = True
for y in range(N):
    if flag:
        for x in range(M):
            if flag:
                if bd[y][x] == 'S':
                    minsik = (y, x)
                    bd[y][x] = '.'
                    flag = False

mymin = 1e9
for st in range(4):
    nbd = [i[:] for i in bd]
    result = solve(st)
    if mymin > result:
        mymin = result

if mymin == 1e9:
    print(-1)
else:
    print(mymin)
