import sys
sys.stdin = open('2573.txt', 'r')

def bfs(y, x):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    queue = [x, y]
    vis[y][x] = True

    while queue:
        x = queue.pop(0)
        y = queue.pop(0)
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if 0 <= xi < M and 0 <= yi < N and not vis[yi][xi]:
                if arctic[yi][xi] == 0 and arctic[y][x] > 0:
                    arctic[y][x] -= 1
                elif arctic[yi][xi] >= 1:
                    vis[yi][xi] = True
                    queue.append(xi)
                    queue.append(yi)
    return 1


N, M = map(int, input().split())
arctic = []
for i in range(N):
    arctic.append(list(map(int, input().split())))

cnt = 0
time = -1
while cnt < 2:
    vis = [[False] * M for i in range(N)]
    cnt = 0
    is_fin = True
    for j in range(N):
        for i in range(M):
            if arctic[j][i] > 0 and not vis[j][i]:
                is_fin = False
                cnt += bfs(j, i)

    time += 1
    if is_fin:
        time = 0
        break

print(time)
