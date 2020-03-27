import sys
from collections import deque

input = sys.stdin.readline
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
M, N = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
room_num = 1
max_area = 0
broken = 0
for r in range(N):
    for c in range(M):
        if vis[r][c]:
            continue
        queue = deque()
        queue.append((r, c))
        vis[r][c] = [room_num, 1]
        while queue:
            y, x = queue.popleft()
            room = castle[y][x]
            for i in range(4):
                if not room & (1 << i):
                    yi = y + dy[i]
                    xi = x + dx[i]
                    if not vis[yi][xi]:
                        vis[yi][xi] = vis[r][c]
                        vis[yi][xi][1] += 1
                        queue.append((yi, xi))
        room_num += 1
        if vis[r][c][1] > max_area:
            max_area = vis[r][c][1]

for r in range(N):
    for c in range(M):
        for i in range(2, 4):
            ri = r + dy[i]
            ci = c + dx[i]
            if ri < N and ci < M and vis[r][c][0] != vis[ri][ci][0]:
                temp = vis[r][c][1] + vis[ri][ci][1]
                if temp > broken:
                    broken = temp

print(room_num - 1)
print(max_area)
print(broken)