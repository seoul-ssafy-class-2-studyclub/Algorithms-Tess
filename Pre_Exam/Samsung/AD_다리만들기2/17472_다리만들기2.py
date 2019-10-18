# import sys
# # sys.stdin = open('17472.txt', 'r')
# # 9
# input = sys.stdin.readline
# import collections
# import heapq
# # from pprint import pprint
# # 모든 섬을 연결하는 다리 길이의 최솟값을 출력한다.
# # 모든 섬을 연결하는 것이 불가능하면 -1을 출력한다.
#
#
#
# # 0은 바다, 1은 땅을 의미한다.
# # 1을 만나면 땅이므로 번호를 매긴다.
#
# # 번호를 다 매기고,
# # 가장 첫번째 섬부터 시작해서 BFS로 만나는 다음 섬을 그 다음 부모로 두고 자식들을 찾아나간다.
# # 그렇게 만들어진 경로로 다리 비용을 구한다.
#
#
# def numbering(Y, X, num):
#     global numberingvisit, earth, startyx
#     q = collections.deque([])
#     q.append((Y, X))
#     numberingvisit[Y][X] = True
#     earth[Y][X] = num
#     startyx[number].append((Y, X))
#
#     while q:
#         y, x = q.pop()
#         for dy, dx in [(0,1), (1,0), (-1,0), (0,-1)]:
#             iy = dy + y
#             ix = dx + x
#             if 0 <= iy < N and 0 <= ix < M and earth[iy][ix] == 1 and numberingvisit[iy][ix] == False:
#                 earth[iy][ix] = num
#                 numberingvisit[iy][ix] = True
#                 q.append((iy, ix))
#                 startyx[num].append((iy, ix))
# #
# # def find(parent, y, x, visit, cost, total):
# #     global namevisit, adj_list
# #     # 방향만 처리해주면 될거같은데 말입니다..
# #     q = collections.deque([])
# #     q.append((parent, y, x, visit, cost, total))
# #     visit[y][x] = True
# #     # namevisit[parent] = True
# #     # 다리길이는 2이상 이여야 한다.
# #     while q:
# #         pnum, Y, X, visit, cost, total = q.popleft()
# #
# #
# #         for dy, dx in [(0,1), (1,0), (-1,0), (0,-1)]:
# #             iy = dy + Y
# #             ix = dx + X
# #             if 0 <= iy < N and 0 <= ix < M and visit[iy][ix] == False:
# #
# #                 # 바다가 아니고, 다른 섬을 만난 경우, 그리고 cost==다리길이기 2이상인경우
# #                 # parent 이름을 바꿔준다.
# #                 # 바꿔주고, 해당 parent가 가진 좌표들로 새로 시작한다.
# #                 if earth[iy][ix] != pnum and earth[iy][ix] != 0 and cost >= 2:
# #                     visited = [i[:] for i in visit]
# #                     visited[iy][ix] = True
# #                     # namevisit[pnum] = True
# #
# #                     adj_list[pnum].add((earth[iy][ix], cost))
# #                     pnum = earth[iy][ix]
# #
# #                     total += cost
# #                     cost = 0
# #                     while startyx[pnum]:
# #                         start = startyx[pnum].pop()
# #                         # 이처럼 모든 후보군을 넣어준 상태로 시작
# #                         find(pnum, start[0], start[1], visited, cost, total)
# #
# #
# #                 # 바다라서 움직여야 하는 경우,
# #                 elif earth[iy][ix] == 0 and earth[iy][ix] != pnum:
# #                     visited = [i[:] for i in visit]
# #                     visited[iy][ix] = True
# #                     q.append((pnum, iy, ix, visited, cost+1, total))
# # # 딕셔너리로 저장한 자식들로 바꿔주고 그 모든 자식들을 돈다.
# #     return total
# #
#
#
# N, M = map(int, input().split())
# earth = [list(map(int, input().split())) for _ in range(N)]
#
# numberingvisit = [[False]*M for _ in range(N)]
# number = 1
# startyx = {}
# for y in range(N):
#     for x in range(M):
#         if earth[y][x] == 1 and numberingvisit[y][x] == False:
#             startyx[number] = []
#             numbering(y, x, number)
#             number += 1
#
# name = [i for i in range(0, number)]
#
# # print(namevisit)
# def newfind(y, x, direction, parent):
#     global earth, newadj_list, adj_list
#     q = collections.deque([])
#     q.append((y, x, 0))
#     while q:
#         Y, X, cost = q.popleft()
#         dy, dx = direction
#         iy = dy + Y
#         ix = dx + X
#         if 0 <= iy < N and 0 <= ix < M:
#             if earth[iy][ix] != parent and earth[iy][ix] != 0 and cost >= 2:
#                 newadj_list[parent].add((earth[iy][ix], cost))
#                 newadj_list[earth[iy][ix]].add((parent, cost))
#                 adj_list[parent].append(earth[iy][ix])
#                 adj_list[earth[iy][ix]].append(parent)
#             elif earth[iy][ix] == 0 and earth[iy][ix] != parent:
#                 q.append((iy, ix, cost+1))
#
#
# adj_list = [[] for _ in range(number+1)]
# newadj_list = [set() for _ in range(number+1)]
# for i in range(1, number):
#     starts = startyx[i]
#     for start in starts:
#         if 0 <= start[1]+1 < M and earth[start[0]][start[1]+1] == 0:
#             newfind(start[0], start[1], (0, 1), i)
#         # if구분좀해!
#         if 0 <= start[0]+1 < N and earth[start[0]+1][start[1]] == 0:
#             newfind(start[0], start[1], (1, 0), i)
# # print(newadj_list)
#
# def isCC(start, visit, cnt, path):
#     global adj_list, res, temppath
#     newvisit = visit[:]
#     newvisit[start] = True
#
#     if cnt == (number-1):
#         res = cnt
#         temppath.append(path)
#         return
#
#     for child in adj_list[start]:
#         if newvisit[child] == False:
#             isCC(child, newvisit, cnt+1, path+[(start, child)])
# #
# # def solve(templist): # parent, child
# #     global finalresult
# #     result = 0
# #     for p, c in templist:
# #         # print(templist)
# #         # print(p, c)
# #         temp = 99999
# #         for children in newadj_list[p]:
# #             if children[0] == c and temp > children[1]:
# #                 temp = children[1]
# #                 # print(temp)
# #         # print('======', temp)
# #         result += temp
# #     print(result)
# #     if finalresult > result:
# #         finalresult = result
# #         # print(finalresult)
#
#
# # 연결요소의 개수 해서 한묶음인지보고
# # 묶음이라면 prim써서 하기
#
# def prim(start):
#     global cost
#     visit = [False]*number
#     cost[start] = 0
#     q = []
#     heapq.heappush(q, (0, 1))
#     while q:
#         cst, node = heapq.heappop(q)
#         visit[node] = True
#         for child, nxtcost in newadj_list[node]:
#             if visit[child] == True:
#                 continue
#             if cost[child] > nxtcost:
#                 cost[child] = nxtcost
#                 heapq.heappush(q, (nxtcost, child))
#
# finalresult = -1
#
# for i in range(1, number):
#     CCvisit = [True] + [False] * (number - 1)
#     res = 0
#     temppath = []
#     isCC(i, CCvisit, 1, [])
#     if res == (number-1): # 만약 섬의 개수와 res가 같다면, 0 묶음이다.
#         finalresult = 999999
#
# if finalresult == 999999:
#     cost = [99999] * (number)
#     prim(1)
#     print(sum(cost[1:]))
# else:
#     print(finalresult)
#
#
#
#
#
#
# #
# # mymin = 99999
# # adj_list = [ set() for i in range(number+1)]
# # for start in startyx[1]:
# #     visit = [[False] * M for _ in range(N)]
# #     # namevisit = [True] * number
# #     res = find(1, start[0], start[1], visit, 0, 0)
# #     if res < mymin:
# #         mymin = res
# # # print(mymin)
# # # print(adj_list)
# # for child in adj_list:
# #     print(child)
# # 이런경우 방향이 어찌되었든 사실 상관 없으려나? 아.. 쭉가다가 꺽는 경우가 문제라서 방향 처리를 해줘야하는구나.
# # 구한 인접리스트와 가중치를 가지고 돌면서 모든 섬을 돌고, 최소값인걸로 갱신해주면된다.


import sys

# sys.stdin = open('17472.txt', 'r')
input = sys.stdin.readline
import collections
import heapq


def numbering(Y, X, num):
    global numberingvisit, earth, startyx
    q = collections.deque([])
    q.append((Y, X))
    numberingvisit[Y][X] = True
    earth[Y][X] = num
    startyx[number].append((Y, X))

    while q:
        y, x = q.pop()
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < M and earth[iy][ix] == 1 and numberingvisit[iy][ix] == False:
                earth[iy][ix] = num
                numberingvisit[iy][ix] = True
                q.append((iy, ix))
                startyx[num].append((iy, ix))


N, M = map(int, input().split())
earth = [list(map(int, input().split())) for _ in range(N)]

numberingvisit = [[False] * M for _ in range(N)]
number = 1
startyx = {}
for y in range(N):
    for x in range(M):
        if earth[y][x] == 1 and numberingvisit[y][x] == False:
            startyx[number] = []
            numbering(y, x, number)
            number += 1

name = [i for i in range(0, number)]


def newfind(y, x, direction, parent):
    global earth, newadj_list, adj_list
    q = collections.deque([])
    q.append((y, x, 0))
    while q:
        Y, X, cost = q.popleft()
        dy, dx = direction
        iy = dy + Y
        ix = dx + X
        if 0 <= iy < N and 0 <= ix < M:
            if earth[iy][ix] != parent and earth[iy][ix] != 0 and cost >= 2:
                newadj_list[parent].add((earth[iy][ix], cost))
                newadj_list[earth[iy][ix]].add((parent, cost))
                adj_list[parent].append(earth[iy][ix])
                adj_list[earth[iy][ix]].append(parent)
            elif earth[iy][ix] == 0 and earth[iy][ix] != parent:
                q.append((iy, ix, cost + 1))


adj_list = [[] for _ in range(number + 1)]
newadj_list = [set() for _ in range(number + 1)]
for i in range(1, number):
    starts = startyx[i]
    for start in starts:
        if 0 <= start[1] + 1 < M and earth[start[0]][start[1] + 1] == 0:
            newfind(start[0], start[1], (0, 1), i)
        if 0 <= start[0] + 1 < N and earth[start[0] + 1][start[1]] == 0:
            newfind(start[0], start[1], (1, 0), i)

# 연결요소 부분 DFS 처리
def isCC(start, visit):
    global adj_list
    visit[start] = True

    for child in adj_list[start]:
        if visit[child] == False:
            isCC(child, visit)

# Prim 외워요
def prim(start):
    global cost
    visit = [False] * number
    cost[start] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        cst, node = heapq.heappop(q)
        visit[node] = True
        for child, nxtcost in newadj_list[node]:
            if visit[child] == True:
                continue
            if cost[child] > nxtcost:
                cost[child] = nxtcost
                heapq.heappush(q, (nxtcost, child))

finalresult = -1
CCvisit = [True] + [False] * (number - 1)
isCC(1, CCvisit)
if False not in CCvisit:
    cost = [99999] * (number)
    prim(1)
    print(sum(cost[1:]))
else:
    print(finalresult)