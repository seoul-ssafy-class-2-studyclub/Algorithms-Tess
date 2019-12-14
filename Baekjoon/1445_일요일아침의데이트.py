import sys
# sys.stdin = open('1445', 'r')

input = sys.stdin.readline
import heapq
N, M = map(int, input().split())
mymap = [list(input()) for _ in range(N)]
# S yx F yx
# 통과하거나 옆을 지나가면 +1을 한다.
# 인접은 어디까지가 인접인가? 상하좌우인가요?
# 최소로 마주친 수 중에 가장 가깝게 F 에 도착한걸 빼와야 하기 때문에 모든 경우의 수를 다 봐야할 거 같은데?
# S와 F는 세지 않는다
# 쓰레기를 마주친 수, 걸어다닌 수

def solve(sy, sx, fy, fx, mymap):
    global res
    q = []
    # fy,fx를 만나면 더이상 append를 하지 않을거니까
    heapq.heappush(q, (0, 0, sy, sx))
    vis = [[False]*M for _ in range(N)]
    vis[sy][sx] = True
    while q:
        for _ in range(len(q)):
            trashcnt, movedcnt, oy, ox = heapq.heappop(q)
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (oy + dy) == fy and (ox + dx) == fx:
                    res.append((trashcnt, movedcnt))

            for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                iy = dy + oy
                ix = dx + ox
                tcnt = 0
                sidecnt = 0
                # 지나가는거
                if 0 <= iy < N and 0 <= ix < M and mymap[iy][ix] == 'g':
                    tcnt = 1

                if 0 <= iy < N and 0 <= ix < M and mymap[iy][ix] == 'sideg':
                    sidecnt = 1

                if 0 <= iy < N and 0 <= ix < M and vis[iy][ix] == False:
                    # 이미 true로 해버려서 제대로 못가는거 같은데 어떡하지?
                    # 1을 가진애가 먼저 선점해버려서 문제다. 한 번 가는 애는 걔로 끝내야하는데.
                    vis[iy][ix] = True
                    if tcnt:
                        heapq.heappush(q, (trashcnt+tcnt, movedcnt, iy, ix))
                    if tcnt == 0 and sidecnt == 1:
                        heapq.heappush(q, (trashcnt, movedcnt+sidecnt, iy, ix))
                    if tcnt == 0 and sidecnt == 0:
                        heapq.heappush(q, (trashcnt, movedcnt, iy, ix))
gar = []
for y in range(N):
    for x in range(M):
        if mymap[y][x] == 'S':
            sy, sx = y, x
        if mymap[y][x] == 'F':
            fy, fx = y, x
        if mymap[y][x] == 'g':
            gar.append((y, x))

for y, x in gar:
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        iiy = dy + y
        iix = dx + x
        if 0 <= iiy < N and 0 <= iix < M and mymap[iiy][iix] == '.':
            mymap[iiy][iix] = 'sideg'

res = []
solve(sy, sx, fy, fx, mymap)
res = sorted(res)
ans = res[0]
# print(res)
print(f'{ans[0]} {ans[1]}')

#
# import sys
# from collections import deque
# input = sys.stdin.readline
# N, M = map(int, input().split())
# mymap = [list(input()) for _ in range(N)]
#
# def solve(sy, sx, fy, fx):
#     global mymap, vis, ans
#     q = deque([])
#     # fy,fx를 만나면 더이상 append를 하지 않을거니까
#     q.append([0, 0, sy, sx])
#     while q:
#         for _ in range(len(q)):
#             trashcnt, movedcnt, oy, ox = q.popleft()
#             # 도착점 바로 전
#             for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
#                 iy = dy + oy
#                 ix = dx + ox
#                 # 지나가는거
#                 if 0 <= iy < N and 0 <= ix < M:
#                 # # 내 인접한 곳에 쓰레기가 있는데, 그 칸을 지나간다면,
#                     if mymap[iy][ix] == 'g':
#                         if 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] > trashcnt:
#                             vis[iy][ix] = [trashcnt, movedcnt]
#                             q.append((trashcnt + 1, movedcnt, iy, ix))
#
#                         elif 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] == trashcnt and vis[iy][ix][1] > movedcnt:
#                             vis[iy][ix] = [trashcnt, movedcnt]
#                             q.append((trashcnt + 1, movedcnt, iy, ix))
#
#                     elif mymap[iy][ix] == 'sideg':
#                         if 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] > trashcnt:
#                             vis[iy][ix] = [trashcnt, movedcnt]
#                             q.append((trashcnt, movedcnt+1, iy, ix))
#
#                         elif 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] == trashcnt and vis[iy][ix][1] > movedcnt:
#                             vis[iy][ix] = [trashcnt, movedcnt]
#                             q.append((trashcnt, movedcnt+1, iy, ix))
#
#                     elif mymap[iy][ix] == '.':
#                         if 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] > trashcnt:
#                             vis[iy][ix] = [trashcnt, movedcnt]
#                             q.append((trashcnt, movedcnt, iy, ix))
#                         elif 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] == trashcnt and vis[iy][ix][1] > movedcnt:
#                             vis[iy][ix] = [trashcnt, movedcnt]
#                             q.append((trashcnt, movedcnt, iy, ix))
#
# gar = []
# for y in range(N):
#     for x in range(M):
#         if mymap[y][x] == 'S':
#             sy, sx = y, x
#             mymap[y][x] = '.'
#         if mymap[y][x] == 'F':
#             fy, fx = y, x
#             mymap[y][x] = '.'
#         if mymap[y][x] == 'g':
#             gar.append((y, x))
#
# # side walk가 될 부분을 미리 저장해 둠으로써 bfs를 돌면서 확인할 필요 없도록 한다.
# for y, x in gar:
#     for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         iiy = dy + y
#         iix = dx + x
#         if 0 <= iiy < N and 0 <= iix < M and mymap[iiy][iix] == '.':
#             mymap[iiy][iix] = 'sideg'
#
# INF = float('INF')
# vis = [[[INF,INF]]*M for _ in range(N)]
# vis[sy][sx] = [0, 0]
# solve(sy, sx, fy, fx)
# print(vis[fy][fx][0], vis[fy][fx][1])
#
#



''''''''''''''''

from collections import deque
near = [[-1,0],[0,1],[1,0],[0,-1]]
def go():
    q = deque([[0,0,sx,sy]])
    vis = [[[9999,9999] for i in range(m)] for i in range(n)]
    while q:
        cg,cn,x,y = q.popleft()
        for a,b in near:
            xi, yi = x+a, y+b
            if 0 <= xi < n and 0 <= yi < m:
                if bd[xi][yi] == 'g':
                    if vis[xi][yi][0] > cg:
                        vis[xi][yi] = [cg,cn]
                        q.append([cg+1, cn, xi, yi])
                    elif vis[xi][yi][0] == cg:
                        if vis[xi][yi][1] > cn:
                            vis[xi][yi] = [cg,cn]
                            q.append([cg+1, cn, xi, yi])
                elif bd[xi][yi] == 'n':
                    if vis[xi][yi][0] > cg:
                        vis[xi][yi] = [cg,cn]
                        q.append([cg, cn+1, xi, yi])
                    elif vis[xi][yi][0] == cg:
                        if vis[xi][yi][1] > cn:
                            vis[xi][yi] = [cg,cn]
                            q.append([cg, cn+1, xi, yi])
                elif bd[xi][yi] == '.':
                    if vis[xi][yi][0] > cg:
                        vis[xi][yi] = [cg,cn]
                        q.append([cg,cn,xi,yi])
                    elif vis[xi][yi][0] == cg:
                        if vis[xi][yi][1] > cn:
                            vis[xi][yi] = [cg,cn]
                            q.append([cg,cn,xi,yi])
    # for i in vis:
    #     print(i)
    return vis[fx][fy]
n,m = map(int,input().split())
bd = [list(input()) for i in range(n)]
gbg = []
for x in range(n):
    for y in range(m):
        if bd[x][y] == 'S':
            sx,sy = [x,y]
            bd[x][y] = '.'
        elif bd[x][y] == 'F':
            fx,fy = [x,y]
            bd[x][y] = '.'
        elif bd[x][y] == 'g':
            gbg.append([x,y])
for x,y in gbg:
    for a,b in near:
        xi, yi = x+a, y+b
        if 0 <= xi < n and 0 <= yi < m:
            if bd[xi][yi] == '.':
                bd[xi][yi] = 'n'
# for i in bd:
#     print(i)
for i in go():
    print(i,end=' ')

'''''

#
# import sys
# # sys.stdin = open('1445', 'r')
#
# from collections import deque
# from pprint import pprint
# input = sys.stdin.readline
# import heapq
# N, M = map(int, input().split())
# mymap = [list(input()) for _ in range(N)]
# # S yx F yx
# # 통과하거나 옆을 지나가면 +1을 한다.
# # 인접은 어디까지가 인접인가? 상하좌우인가요?
# # 최소로 마주친 수 중에 가장 가깝게 F 에 도착한걸 빼와야 하기 때문에 모든 경우의 수를 다 봐야할 거 같은데?
# # S와 F는 세지 않는다
# # 쓰레기를 마주친 수, 걸어다닌 수
#
# def solve(sy, sx, fy, fx):
#     global mymap, vis, ans
#     q = deque([])
#     # fy,fx를 만나면 더이상 append를 하지 않을거니까
#     q.append((0, 0, sy, sx))
#
#
#     while q:
#         for _ in range(len(q)):
#             trashcnt, movedcnt, oy, ox = q.popleft()
#             # 도착점 바로 전
#             # for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             #     if (oy + dy) == fy and (ox + dx) == fx:
#             #         # print(oy, ox, trashcnt, movedcnt)
#             #         ans.append((trashcnt, movedcnt))
#
#
#             for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
#                 iy = dy + oy
#                 ix = dx + ox
#                 tcnt = 0
#                 sidecnt = 0
#                 # 지나가는거
#                 if 0 <= iy < N and 0 <= ix < M and mymap[iy][ix] == 'g':
#                     tcnt = 1
#
#                 # 내 인접한 곳에 쓰레기가 있는데, 그 칸을 지나간다면,
#                 for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                     iiy = dy + iy
#                     iix = dx + ix
#                     if 0 <= iiy < N and 0 <= iix < M and mymap[iiy][iix] == 'g':
#                         sidecnt = 1
#
#                 # print(vis)
#                 if tcnt:
#                     if 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] > trashcnt:
#                         vis[iy][ix] = [trashcnt, movedcnt]
#                         q.append((trashcnt + tcnt, movedcnt, iy, ix))
#
#                     elif 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] == trashcnt and vis[iy][ix][1] > movedcnt:
#                         vis[iy][ix] = [trashcnt, movedcnt]
#                         q.append((trashcnt + tcnt, movedcnt, iy, ix))
#
#                 if sidecnt:
#                     if 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] > trashcnt:
#                         vis[iy][ix] = [trashcnt, movedcnt]
#                         q.append((trashcnt, movedcnt+sidecnt, iy, ix))
#                     elif 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] == trashcnt and vis[iy][ix][1] > movedcnt:
#                         vis[iy][ix] = [trashcnt, movedcnt]
#                         q.append((trashcnt, movedcnt+sidecnt, iy, ix))
#
#
#                 if tcnt == 0 and sidecnt == 0:
#                     if 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] > trashcnt:
#                         vis[iy][ix] = [trashcnt, movedcnt]
#                         q.append((trashcnt, movedcnt, iy, ix))
#                     elif 0 <= iy < N and 0 <= ix < M and vis[iy][ix][0] == trashcnt and vis[iy][ix][1] > movedcnt:
#                         vis[iy][ix] = [trashcnt, movedcnt]
#                         q.append((trashcnt, movedcnt, iy, ix))
#
#
#
#
#                     # pprint(vis)
#
#
#
#
#
# for y in range(N):
#     for x in range(M):
#         if mymap[y][x] == 'S':
#             sy, sx = y, x
#             mymap[y][x] = '.'
#         if mymap[y][x] == 'F':
#             fy, fx = y, x
#             mymap[y][x] = '.'
#
# INF = float('INF')
# vis = [[[INF,INF]]*M for _ in range(N)]
# # print(vis)
# vis[sy][sx] = [0, 0]
#
# ans = []
# solve(sy, sx, fy, fx)
# ans = sorted(ans)
# # print(ans)
# # # print(vis)
# # for v in vis:
# #     print(v)
# print(vis[fy][fx][0], vis[fy][fx][1])
#
