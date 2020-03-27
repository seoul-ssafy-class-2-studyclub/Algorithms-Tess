## BFS

import sys

from pprint import pprint
sys.stdin = open('1175.txt', 'r')


'''
3 6
.SC#C.
..##..
......
'''

#
# import heapq
# def solve(status):
#     global nbd
#     direction = [(-1,0), (1,0), (0,-1), (0,1)]
#     visit = [[False]*M for _ in range(N)]
#     visit[minsik[0]][minsik[1]] = True # 처음에는 항상 True 처리 하고 시작한다.
#     q = []
#     # 시작의 status는 4가지 경우가 있다.
#     heapq.heappush(q, (0, 0, minsik, status))
#     while q:
#         Cs, mins, current, status = heapq.heappop(q)
#         cury, curx = current[0], current[1]
#
#         for i in range(4):
#             if i != status:
#                 nxty, nxtx = direction[i][0], direction[i][1]
#                 nxty = nxty + cury
#                 nxtx = nxtx + curx
#
#                 if 0 <= nxty < N and 0 <= nxtx < M and visit[nxty][nxtx] == False and nbd[nxty][nxtx] != '#':
#                     if nbd[nxty][nxtx] == '.':
#                         heapq.heappush(q, (Cs, mins+1, (nxty, nxtx), i))
#                         visit[nxty][nxtx] = True
#                         # continue
#
#                     if nbd[nxty][nxtx] == 'C' and C[0] == (nxty, nxtx):
#                         heapq.heappush(q, (Cs-1, mins+1, (nxty, nxtx), i))
#                         nbd[nxty][nxtx] = '.'
#                         visit[nxty][nxtx] = True
#                         visit = [[False]*M for _ in range(N)]
#                         # continue
#
#                     if nbd[nxty][nxtx] == 'C' and C[1] == (nxty, nxtx):
#                         heapq.heappush(q, (Cs-1, mins+1, (nxty, nxtx), i))
#                         nbd[nxty][nxtx] = '.'
#                         visit[nxty][nxtx] = True
#                         # print(nxty, nxtx, mins)
#
#                         return mins+1
#     return 1e9
#
# N, M = map(int, input().split())
# bd = [list(input()) for _ in range(N)]
#
# C = []
# # flag = True
# for y in range(N):
#     for x in range(M):
#         if bd[y][x] == 'S':
#             minsik = (y, x)
#             bd[y][x] = '.'
#         if bd[y][x] == 'C':
#             C.append((y, x))
#
# mymin = 1e9
# for st in range(4):
#     nbd = [i[:] for i in bd]
#     result = solve(st)
#     if mymin > result:
#         mymin = result
#
# if mymin == 1e9:
#     print(-1)
# else:
#     print(mymin)



#
# import heapq
# def solve(status):
#     global nbd
#     direction = [(-1,0), (1,0), (0,-1), (0,1)]
#     visit = [[False]*M for _ in range(N)]
#     visit[minsik[0]][minsik[1]] = True # 처음에는 항상 True 처리 하고 시작한다.
#     q = []
#     # 시작의 status는 4가지 경우가 있다.
#     heapq.heappush(q, (0, 0, minsik, status))
#     while q:
#         Cs, mins, current, status = heapq.heappop(q)
#         cury, curx = current[0], current[1]
#
#         for i in range(4):
#             if i != status:
#                 nxty, nxtx = direction[i][0], direction[i][1]
#                 nxty = nxty + cury
#                 nxtx = nxtx + curx
#
#                 if 0 <= nxty < N and 0 <= nxtx < M and visit[nxty][nxtx] == False and nbd[nxty][nxtx] != '#':
#                     if nbd[nxty][nxtx] == '.':
#                         heapq.heappush(q, (Cs, mins+1, (nxty, nxtx), i))
#                         visit[nxty][nxtx] = True
#                         # continue
#
#                     if nbd[nxty][nxtx] == 'C' and Cs == 0:
#                         heapq.heappush(q, (Cs-1, mins+1, (nxty, nxtx), i))
#                         nbd[nxty][nxtx] = '.'
#                         visit[nxty][nxtx] = True
#                         visit = [[False]*M for _ in range(N)]
#                         # continue
#
#                     if nbd[nxty][nxtx] == 'C' and Cs == -1:
#                         heapq.heappush(q, (Cs-1, mins+1, (nxty, nxtx), i))
#                         nbd[nxty][nxtx] = '.'
#                         visit[nxty][nxtx] = True
#                         # print(nxty, nxtx, mins)
#
#                         return mins+1
#     return 1e9
#
# N, M = map(int, input().split())
# bd = [list(input()) for _ in range(N)]
#
# flag = True
# for y in range(N):
#     if flag:
#         for x in range(M):
#             if flag:
#                 if bd[y][x] == 'S':
#                     minsik = (y, x)
#                     bd[y][x] = '.'
#                     flag = False
#
# mymin = 1e9
# for st in range(4):
#     nbd = [i[:] for i in bd]
#     result = solve(st)
#     if mymin > result:
#         mymin = result
#
# if mymin == 1e9:
#     print(-1)
# else:
#     print(mymin)

# import sys
# input = sys.stdin.readline



import sys
input = sys.stdin.readline
direction = [(-1,0), (1,0), (0,-1), (0,1)]
def solve(status):
    global nbd, mymin
    # 4차원으로 관리해야했는데............

    visit = [[[[False]*3 for _ in range(4)] for _ in range(M)] for _ in range(N)]
    pprint(visit)
    # visit[minsik[0]][minsik[1]][status][0] = True # 처음에는 항상 True 처리 하고 시작한다.
    q = []
    # 시작의 status는 4가지 경우가 있다.
    q.append((0, 0, minsik, status))
    while q:
        Cs, mins, current, status = q.pop(0)
        cury, curx = current[0], current[1]
        mins += 1

        for i in range(4):
            if i != status:
                nxty, nxtx = direction[i][0], direction[i][1]
                nxty = nxty + cury
                nxtx = nxtx + curx
                if 0 <= nxty < N and 0 <= nxtx < M:

                    if nbd[nxty][nxtx] == '#':
                        continue

                    if visit[nxty][nxtx][i][Cs] == False:
                        if nbd[nxty][nxtx] == '.':
                            q.append((Cs, mins, (nxty, nxtx), i))
                            visit[nxty][nxtx][i][Cs] = True
                            continue

                        if nbd[nxty][nxtx] == 'C' and C[0] == (nxty, nxtx):
                            if Cs == 0:
                                q.append((1, mins, (nxty, nxtx), i))
                                visit[nxty][nxtx][i][1] = True
                                continue

                            elif Cs == 2: # 2인 상태에서 나한테 도착했다면, 두번째이므로
                                if mymin > mins:
                                    mymin = mins

                        if nbd[nxty][nxtx] == 'C' and C[1] == (nxty, nxtx):
                            if Cs == 0:
                                q.append((2, mins, (nxty, nxtx), i))
                                visit[nxty][nxtx][i][2] = True
                                continue

                            elif Cs == 1: # 1인 상태에서 나한테 도착했다면, 두번째이므로
                                if mymin > mins:
                                    mymin = mins

N, M = map(int, input().split())
bd = [list(input()) for _ in range(N)]

C = []
for y in range(N):
    for x in range(M):
        if bd[y][x] == 'S':
            minsik = (y, x)
            bd[y][x] = '.'
        if bd[y][x] == 'C' and C:
            C.append((y, x))
        if bd[y][x] == 'C' and not C:
            C.append((y, x))
mymin = 1e9
for st in range(4):
    nbd = [i[:] for i in bd]
    solve(st)

if mymin == 1e9:
    print(-1)
else:
    print(mymin)
