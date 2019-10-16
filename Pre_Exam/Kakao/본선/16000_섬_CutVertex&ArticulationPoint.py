import sys
sys.stdin = open('16000.txt', 'r')
from collections import deque, defaultdict
sys.setrecursionlimit(10**7)


def bfs(cur):
    vis[r][c] = num
    queue = deque()
    queue.append((r, c))
    while queue:
        y, x = queue.popleft()
        for dy, dx in dxy:
            yi = y + dy
            xi = x + dx
            if 0 <= yi < N and 0 <= xi < M:
                nxt = vis[yi][xi]
                if pacific[yi][xi] == cur and not nxt:
                    queue.append((yi, xi))
                    vis[yi][xi] = num
                elif pacific[yi][xi] != cur and nxt:
                    if con[nxt] == num:
                        continue
                    adj[num].append(nxt)
                    adj[nxt].append(num)
                    con[num] = num
                    con[nxt] = num

def init():
    for i in range(num):
        con[i] = 0
    for r in range(N):
        for c in range(M):
            if pacific[r][c] == '#':
                is_sum[vis[r][c]] = 1

def go(now):
    global order
    ret = num - 1
    discovered[now] = order
    order += 1
    stack.append(now)
    for nxt in adj[now]:
        if not discovered[nxt]:
            go(nxt)
            if is_sum[now] and discovered[nxt] == discovered[now]:
                while stack and stack[-1] != now:
                    con[stack.pop()] = 1
            stack.append(now)
        ret = min(ret, discovered[nxt])
    discovered[now] = ret
    return

input = sys.stdin.readline
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
pacific = [list(input().strip()) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
adj = [[]]
con = defaultdict(list)
islands = []
ocean = []
num = 1
for r in range(N):
    for c in range(M):
        if not vis[r][c]:
            adj.append([])
            bfs(pacific[r][c])
            if pacific[r][c] == '.':
                ocean.append(num)
            else:
                islands.append(num)
            num += 1
is_sum = [0] * num
discovered = [False] * num
stack = deque()
order = 1

init()
go(1)


for r in range(N):
    for c in range(M):
        if pacific[r][c] == '.':
            continue
        num = vis[r][c]
        if con[num] and discovered[num] != 1:
            pacific[r][c] = 'X'
        else:
            pacific[r][c] = 'O'
for r in range(N):
    print(''.join(pacific[r]))


# import sys
# sys.stdin = open('16000.txt', 'r')
# from collections import deque
# sys.setrecursionlimit(10**10)
#
# def bfs(cur):
#     vis[r][c] = num
#     queue = deque()
#     queue.append((r, c))
#     while queue:
#         y, x = queue.popleft()
#         for dy, dx in dxy:
#             yi = y + dy
#             xi = x + dx
#             if 0 <= yi < N and 0 <= xi < M:
#                 nxt = vis[yi][xi]
#                 if pacific[yi][xi] == cur and not nxt:
#                     queue.append((yi, xi))
#                     vis[yi][xi] = num
#                 elif pacific[yi][xi] != cur and nxt:
#                     if con[nxt] == num:
#                         continue
#                     adj[num].append(nxt)
#                     adj[nxt].append(num)
#                     con[num] = num
#                     con[nxt] = num
#
# def init():
#     for i in range(num):
#         con[i] = 0
#     for r in range(N):
#         for c in range(M):
#             if pacific[r][c] == '#':
#                 is_sum[vis[r][c]] = 1
#
# def go(now):
#     global order
#     ret = num - 1
#     discovered[now] = order
#     order += 1
#     stack.append(now)
#     for nxt in adj[now]:
#         if not discovered[nxt]:
#             go(nxt)
#             if is_sum[now] and discovered[nxt] == discovered[now]:
#                 while stack and stack[-1] != now:
#                     con[stack.pop()] = 1
#                     # print(con)
#             stack.append(now)
#         ret = min(ret, discovered[nxt])
#     discovered[now] = ret
#     return
#
# input = sys.stdin.readline
# dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# N, M = map(int, input().split())
# pacific = [list(input().strip()) for _ in range(N)]
# vis = [[False] * M for _ in range(N)]
# adj = [[]]
# con = [0] * 4000001
# islands = []
# ocean = []
# num = 1
# for r in range(N):
#     for c in range(M):
#         if not vis[r][c]:
#             adj.append([])
#             bfs(pacific[r][c])
#             if pacific[r][c] == '.':
#                 ocean.append(num)
#             else:
#                 islands.append(num)
#             num += 1
# is_sum = [0] * num
# discovered = [False] * num
# stack = deque()
# order = 1
#
# init()
# go(1)
#
# for r in range(N):
#     for c in range(M):
#         if pacific[r][c] == '.':
#             continue
#         num = vis[r][c]
#         if con[num] and discovered[num] != 1:
#             pacific[r][c] = 'X'
#         else:
#             pacific[r][c] = 'O'
# for r in range(N):
#     print(''.join(pacific[r]))

'''

import sys
from collections import deque
​
def bfs(cur):
    vis[r][c] = num
    queue = deque()
    queue.append((r, c))
    while queue:
        y, x = queue.popleft()
        for dy, dx in dxy:
            yi = y + dy
            xi = x + dx
            if 0 <= yi < N and 0 <= xi < M:
                nxt = vis[yi][xi]
                if pacific[yi][xi] == cur and not nxt:
                    queue.append((yi, xi))
                    vis[yi][xi] = num
                elif pacific[yi][xi] != cur and nxt:
                    if con[nxt] == num:
                        continue
                    adj[num].append(nxt)
                    adj[nxt].append(num)
                    con[num] = num
                    con[nxt] = num
​
​
input = sys.stdin.readline
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
pacific = [list(input().strip()) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
adj = [[]]
con = [0] * 4000001
islands = []
ocean = []
num = 1
for r in range(N):
    for c in range(M):
        if not vis[r][c]:
            adj.append([])
            bfs(pacific[r][c])
            if pacific[r][c] == '.':
                ocean.append(num)
            else:
                islands.append(num)
            num += 1
​
is_island = [False] * num
for i in islands:
    is_island[i] = True
​
tree = [[] for _ in range(num)]
discovered = [False] * num
safe = [True] * num
is_cut = [False] * num
order = 1
def dfs_tree(node=1):
    global order
    discovered[node] = order
    order += 1
    ret = discovered[node]
    for i in adj[node]:
        nxt = discovered[i]
        if nxt:
            ret = min(ret, nxt)
            continue
        tree[node].append(i)
        low = dfs_tree(i)
        if low >= discovered[node]:
            is_cut[node] = True
        ret = min(ret, low)

    return ret
​
​
dfs_tree()
visited = [False] * num
def chk_unsafe(start):
    stack = deque()
    stack.append(start)
    while stack:
        node = stack.pop()
        visited[node] = True
        for child in tree[node]:
            safe[child] = False
            stack.append(child)
​
​
for i in range(1, num):
    if visited[i]:
        continue
    visited[i] = True
    if is_island[i] and is_cut[i]:
        chk_unsafe(i)

for r in range(N):
    for c in range(M):
        if pacific[r][c] == '.':
            continue
        cur = vis[r][c]
        if safe[cur]:
            pacific[r][c] = 'O'
        else:
            pacific[r][c] = 'X'

    print(''.join(pacific[r]))


'''