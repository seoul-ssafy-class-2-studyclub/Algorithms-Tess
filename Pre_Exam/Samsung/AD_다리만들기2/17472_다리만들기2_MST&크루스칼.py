import sys
from collections import deque
# disjoint set의 union-find 함수.
def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    return True

def find_path(y, x, dy, dx, past):
    cnt = 0
    while y < N and x < M and not country[y][x]:
        cnt += 1
        y += dy
        x += dx
    if y >= N or x >= M:
        return
    now = country[y][x]
    if cnt >= 2 and past != now:
        if adj[past][now] > cnt:
            adj[past][now] = cnt
            adj[now][past] = cnt
    return

def kruskal():
    # 간선의 가중치가 무한대가 아니라면 (= 두 섬을 잇는 간선이 존재한다면) edges 리스트에 추가한다.
    edges = []
    for r in range(num):
        for c in range(r + 1, num):
            if adj[r][c] != INF:
                edges.append((r, c, adj[r][c]))

    # 가중치를 기준으로 오름차순 정렬해 union-find를 시작한다.
    edges.sort(key=lambda x: x[2])
    res = 0
    chk = 0
    for n1, n2, w in edges:
        # union에 성공했다면 가중치를 더해주고, 간선이 하나 추가되었음을 표시한다.
        if union(n1, n2):
            res += w
            chk += 1
    # 간선의 수가 섬의 개수 - 1보다 작다면 모든 섬이 이어지지 않은 것이니 -1을 return한다.
    if chk < num - 3:
        return -1
    return res

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
input = sys.stdin.readline
INF = float('inf')
N, M = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
# 섬의 번호를 2부터 매겨준다. input 받을 때 0은 바다 1은 섬으로 되어 있기 때문에...
num = 2
for r in range(N):
    for c in range(M):
        if country[r][c] == 1:
            country[r][c] = num
            queue = deque([(r, c)])
            while queue:
                y, x = queue.popleft()
                for dy, dx in dxy:
                    yi = y + dy
                    xi = x + dx
                    if 0 <= yi < N and 0 <= xi < M and country[yi][xi] == 1:
                        country[yi][xi] = num
                        queue.append((yi, xi))
            num += 1

# 간선의 가중치가 저장될 인접 행렬
adj = [[INF] * num for _ in range(num)]
for r in range(N):
    for c in range(M):
        if not country[r][c]:
            continue
        for dy, dx in dxy[1:3]:
            yi = r + dy
            xi = c + dx
            # 바다에 맞닿은 섬이라면 바다쪽으로 탐색을 시작한다.
            if yi < N and xi < M and not country[yi][xi]:
                find_path(yi, xi, dy, dx, country[r][c])

root = [i for i in range(num)]
rank = [0] * num
res = kruskal()
print(res)