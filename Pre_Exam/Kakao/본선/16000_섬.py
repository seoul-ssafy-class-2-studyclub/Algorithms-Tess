import sys
sys.stdin = open('16000.txt', 'r')
from pprint import pprint

'''
1. 0.0 에서 가장 먼저 닿는 곳을 방문한다.
2. 번호를 매긴다. -> 한번 매길때,
3. 번호 안에 있는 섬의 번호를 매긴다.
각 네면에 존재하는 섬들이 연결된 섬들인가?
동
서
남
북

4. 모든 섬에 번호를 매기고, 번호를 매긴 섬들이 어떤 다른섬들을 상하좌우로 시작해서 갔을때, 만나는지 확인한다. 마치 다리를 연결하듯
5. 한 섬에서 시작해서 네방향으로 나아갈때, 그 섬이 도착한 번호가 2개 이상이라 선택지가 많다면, 즉, 매긴 번호 수만큼 있다면, 선택지가 다양하다는 것이다.
6. 즉 한 섬에만 둘러쌓인 것이 아니라는 뜻.


그래프로한다.
어느 한 정점에서 시작해서 어느 하나를 지웠을때 최외곽으로 도달하지 못한다면, 한 섬에 둘러쌓인 것과 마찬가지이다.

한 지점에서 최외곽으로 도달 가능한지 확인한다.
그리고 자기 자신을 만나서도 안된다. visit로 확인
'''

import sys
import collections
input = sys.stdin.readline

def find(y, x, named):
    global earth, landname, firstvisited
    q = collections.deque([])
    q.append((y, x))
    firstvisited[y][x] = True
    earth[y][x] = named
    while q:
        y, x = q.popleft()
        for dy, dx in [(0,1), (0,-1), (1, 0), (-1, 0)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < M and firstvisited[iy][ix] == False and earth[iy][ix] == '#':
                firstvisited[iy][ix] = True
                q.append((iy, ix))
                earth[iy][ix] = named

def secondfind(y, x, stop):
    global earth
    tempvisit = [ [False]*M for _ in range(N) ]
    q = collections.deque([])
    q.append((y, x))
    forreturn = []
    while q:
        y, x = q.popleft()
        for dy, dx in [(0,1), (0,-1), (1, 0), (-1, 0)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < M and tempvisit[iy][ix] == False:
                if earth[iy][ix] == '.':
                    tempvisit[iy][ix] = True
                    q.append((iy, ix))
                if earth[iy][ix] != stop and earth[iy][ix] != '.':
                    forreturn.append(earth[iy][ix])
    return forreturn


def getinfo(start):
    global earth
    mychildren = set()
    used = [ [False]*M for _ in range(N) ]
    for i in range(N):
        for j in range(M):
            if earth[i][j] == start and used[i][j] == False:
                used[i][j] = True
                info = secondfind(i, j, start)
                mychildren.update(info)
    return list(mychildren)

N, M = map(int, input().split())

# 최외곽을 -2로 바꾼다. -> 우리들의 도착점이다.
earth = [ list(input()) for _ in range(N) ]
final = [i[:] for i  in earth]

landname = []
firstvisited = [ [False]*M for _ in range(N) ]
name = 0
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0 or i == N-1 or j == M-1:
            earth[i][j] = -2

        if earth[i][j] == '#':
            name += 1
            landname.append(name)
            find(i, j, name)

adj_list = [ [] for i in range(name+1)]
for one in landname:
    children = getinfo(one)
    adj_list[one].extend(children)
# print(adj_list)

# print('--', adj_list)
# 시간초과
# landname을 하나씩 돌면서, -2가 자식에 있다면 안전한 것 또는 -2를 만난다면 안전한것, 그렇지 않다면 안전하지 않다.
#
# safe = []
# for one in landname:
#     if -2 in adj_list[one]:
#         safe.append(one)
#
# # 1은 무조건 safe한 섬이다.
#
# shouldbechecked = set(landname) - set(safe)
# # shouldbechecked = list(shouldbechecked)
# danger = []
# for one in shouldbechecked:
#     if len(adj_list[one]) == 1:
#         danger.append(one)
# # print(adj_list)
# neutral = set(landname) - set(safe) - set(danger)
# # print(safe, danger, neutral)
# # neutral = list(neutral)
# for y in range(N):
#     for x in range(M):
#         if earth[y][x] in safe or earth[y][x] in neutral:
#             final[y][x] = 'O'
#         elif earth[y][x] in danger:
#             final[y][x] = 'X'
#
# for res in final:
#     print(''.join(res))



# 판단 다시
#
#
# myfinalvisit = [False]*(name+1)
# safe = []
# inner = []
# cnt = 0
# for one in landname:
#     if -2 in adj_list[one]:
#         cnt += 1
#         myfinalvisit[one] = True
#         safe.append(one)
#         for i in adj_list[one]:
#             # print(adj_list[one])
#             # print(i)
#             if i != -2:
#                 inner.append(i)
#         adj_list[one] = [-2]
# # print(inner) # 2가 1의 inner에 들어있는 정점이라는 소리다. 가장 안쪽에 있는게 단말노드이다.
# # print(adj_list)
# # print(cnt)
#
# # -2를 자식으로 가지면 무조건 safe한 섬이다.
# # -2를 가지면 가장 바깥쪽에 있는 섬이며, -2 를 제외하고 (그 섬들이 다수인 경우 그 안에 있는 섬들도 안전하고),
#
#
# def divide(o, visit):
#
#     if len(adj_list[o]) == 1 or visit[o] == True:
#         visit[o] = True
#         return o
#
#     for i in adj_list[o]:
#         visit[i] = True
#         divide(i, visit)
#
#     return False
#
#
#
# danger = []
# if len(inner) == 1:
#     danger.append(inner)
# else:
#     # 다수인 경우,
#     for one in inner:
#         if myfinalvisit[one] == False:
#             if len(adj_list[one]) == 1:
#                 danger.append(one)
#             else:
#                 myfinalvisit[one] = True
#                 ok = divide(one, myfinalvisit)
#                     # 안에있는 자식을 하나만 가지거나 아무것도 가지지 않을때까지진행한다.
#                 if ok == False:
#                     danger.append(one)
#                     break
# # 그 섬이 가진 자식이 하나라면(공통되며, 하나라면), 그 자식은 안전하지만 그 안에있는 자식은 안전하지 않다.
# # 그러므로 안전하다고 판단된 자식들을 제외하고는 모두 안전하지 않은 것이 된다.
# # print(danger)
# # print(inner)
# if danger != []:
#     oklands = set(landname) - set(danger[0])
#     innerdanger = set(landname) - (set(oklands) & set(danger[0]))
# else:
#     oklands = set(landname) - set(danger)
#     innerdanger = set(landname) - (set(oklands) & set(danger))
#
# for y in range(N):
#     for x in range(M):
#         if earth[y][x] in oklands:
#             final[y][x] = 'O'
#         elif earth[y][x] in danger or earth[y][x] in innerdanger:
#             final[y][x] = 'X'
#
# for res in final:
#     print(''.join(res))
#
#
#
#

# adj_list = [set() for _ in range(name+1)]
# for r in range(1, N):
#     cur = -2
#     for c in range(1, M):
#         if earth[r][c] != '.' and earth[r][c] != cur:
#             new = earth[r][c]
#             adj_list[cur].add(new)
#             adj_list[new].add(cur)
#             cur = new
# for c in range(1, M):
#     cur = -2
#     for r in range(1, N):
#         if earth[r][c] != '.' and earth[r][c] != cur:
#             new = earth[r][c]
#             adj_list[cur].add(new)
#             adj_list[new].add(cur)
#             cur = new
# adj = [list(i) for i in adj_list]
# print(adj)
safe = [False] * (name+1)
# print(name)
for i in range(1, name+1):
    # print(i)
    if -2 in adj_list[i]:
        safe[i] = True
# print(safe)
# print(adj)
for i in range(1, name+1):
    if safe[i]:
        continue
    for j in range(1, name+1):
        if i == j:
            continue
        vis = [False] * (name+1)
        stack = collections.deque([])
        stack.extend(adj_list[i])
        flag = True
        while stack:

            node = stack.pop()
            # print(node)
            if node == -2:
                flag = False
                break
            if not vis[node] and node != j:
                vis[node] = True
                stack.extend(adj_list[node])
        if flag:
            # print(flag)
            break
    if not flag:
        safe[i] = True
        # print(safe[i])
# print(safe)

for r in range(N):
    for c in range(M):
        if earth[r][c] == '.':
            continue
        island = earth[r][c]
        if not island:
            earth[r][c] = '.'
        elif safe[island]:
            earth[r][c] = '0'
        else:
            earth[r][c] = 'X'

for r in range(N):
    for c in range(M):
        if r == 0 or c == 0 or r == N - 1 or c == M - 1:
            earth[r][c] = '.'


for r in range(N):
    print(''.join(earth[r]))