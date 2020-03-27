import sys
from collections import deque

knight = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
bishop = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
rook = [(1, 0), (0, 1), (-1, 0), (0, -1)]
input = sys.stdin.readline


def calc_dis(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)


def move_knight(y, x, j, i):
    vis = [[False] * N for _ in range(N)]
    queue = deque()
    queue.append((y, x, 0))
    vis[y][x] = True
    while queue:
        r, c, cnt = queue.popleft()
        for b, a in knight:
            ri = r + b
            ci = c + a
            if 0 <= ri < N and 0 <= ci < N and not vis[ri][ci]:
                if ri == j and ci == i:
                    return cnt + 1
                queue.append((ri, ci, cnt + 1))
                vis[ri][ci] = True
    return 0


def move_bishop(y, x, j, i):
    if calc_dis(y, x, j, i) % 2:
        return 0
    if abs(x - i) > 0 and abs(y - j) / abs(x - i) == 1:
        return 1
    else:
        return 2


def move_rook(y, x, j, i):
    if y == j or x == i:
        return 1
    else:
        return 2


N = int(input())
length = N ** 2 + 1
board = [list(map(int, input().split())) for _ in range(N)]
idx = [0] * length
# knight, bishop, rook
dis = [[987654321, 987654321, 98765321] for _ in range(length)]
dis[1] = [0, 0, 0]
for r in range(N):
    for c in range(N):
        idx[board[r][c]] = (r, c)

for i in range(2, length):
    ri, ci = idx[i - 1]
    rj, cj = idx[i]
    temp = [move_knight(ri, ci, rj, cj), move_bishop(ri, ci, rj, cj), move_rook(ri, ci, rj, cj)]
    for past in range(3):
        if i >= 3 and not dis[i - 1][past]:
            continue
        for cur in range(3):
            if not temp[cur]:
                dis[i][cur] = 0
                continue
            if past == cur:
                dis[i][cur] = min(dis[i - 1][past] + temp[cur], dis[i][cur])
            else:
                dis[i][cur] = min(dis[i - 1][past] + temp[cur] + 1, dis[i][cur])

res = min([i for i in dis[length - 1] if i])
print(dis)
print(res)