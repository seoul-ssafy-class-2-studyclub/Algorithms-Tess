import sys
sys.stdin = open('1445', 'r')

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
            if oy == fy and ox == fx:
                res.append([trashcnt, movedcnt])
                continue

            for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                iy = dy + oy
                ix = dx + ox
                tcnt = 0
                sidecnt = 0
                # 지나가는거
                if 0 <= iy < N and 0 <= ix < M and mymap[iy][ix] == 'g':
                    tcnt = 1

                # 내 인접한 곳에 쓰레기가 있는데, 그 칸을 지나간다면,
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    iiy = dy + iy
                    iix = dx + ix
                    if 0 <= iiy < N and 0 <= iix < M and mymap[iiy][iix] == 'g':
                        sidecnt = 1

                if 0 <= iy < N and 0 <= ix < M and vis[iy][ix] == False:
                    # 이미 true로 해버려서 제대로 못가는거 같은데 어떡하지?
                    # 1을 가진애가 먼저 선점해버려서 문제다. 한 번 가는 애는 걔로 끝내야하는데.
                    vis[iy][ix] = True
                    heapq.heappush(q, (trashcnt+tcnt, movedcnt+sidecnt, iy, ix))

for y in range(N):
    for x in range(M):
        if mymap[y][x] == 'S':
            sy, sx = y, x
        if mymap[y][x] == 'F':
            fy, fx = y, x
res = []
solve(sy, sx, fy, fx, mymap)
res = sorted(res)
ans = res[0]
print(f'{ans[0]} {ans[1]}')

#
# import sys
# sys.stdin = open('1445', 'r')
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
# def solve(sy, sx, fy, fx, mymap):
#     global res
#     q = []
#     # fy,fx를 만나면 더이상 append를 하지 않을거니까
#     heapq.heappush(q, (0, 0, sy, sx))
#     vis = [[[99,99]]*M for _ in range(N)] # vis를 F/T거를 두개쓴다.
#     # print(vis)
#     vis[sy][sx] = [0, 0]
#     while q:
#         for _ in range(len(q)):
#             trashcnt, movedcnt, oy, ox = heapq.heappop(q)
#             if oy == fy and ox == fx:
#                 res.append([trashcnt, movedcnt])
#                 return
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
#                 if 0 <= iy < N and 0 <= ix < M and sum(vis[iy][ix]) > trashcnt+tcnt+movedcnt+sidecnt:
#                     # 이미 true로 해버려서 제대로 못가는거 같은데 어떡하지?
#                     # 1을 가진애가 먼저 선점해버려서 문제다. 한 번 가는 애는 걔로 끝내야하는데.
#                     vis[iy][ix] = [trashcnt+tcnt, movedcnt+sidecnt]
#                     # pprint(vis)
#                     heapq.heappush(q, (trashcnt+tcnt, movedcnt+sidecnt, iy, ix))
#
# for y in range(N):
#     for x in range(M):
#         if mymap[y][x] == 'S':
#             sy, sx = y, x
#         if mymap[y][x] == 'F':
#             fy, fx = y, x
# res = []
# solve(sy, sx, fy, fx, mymap)
# res = sorted(res)
# ans = res[0]
# print(f'{ans[0]} {ans[1]}')