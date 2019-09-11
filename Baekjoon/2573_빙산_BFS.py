import sys
sys.stdin = open('input/2573.txt', 'r')
import collections

def bfs(y, x):
    queue = collections.deque()
    queue.append((y, x))
    vis[y][x] = True

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
            xi = x + dx
            yi = y + dy
            if 0 <= xi < M and 0 <= yi < N and not vis[yi][xi]: # False면,
                if arctic[yi][xi] == 0 and arctic[y][x] > 0: #나를 기준으로 양수이고, 주위가 0이라면 있는 만큼 -1
                    arctic[y][x] -= 1
                elif arctic[yi][xi] >= 1: # 그게 아니라면,
                    vis[yi][xi] = True #
                    queue.append((yi, xi))
    return 1


N, M = map(int, input().split())
arctic = []
for _ in range(N):
    arctic.append(list(map(int, input().split())))

cnt = 0
time = -1
while cnt < 2: # 0,1일때 while # cnt가 2덩어리가 되면 break
    vis = [[False] * M for _ in range(N)]
    cnt = 0
    is_fin = True
    for j in range(N):
        for i in range(M):
            if arctic[j][i] > 0 and not vis[j][i]:
                is_fin = False
                cnt += bfs(j, i)

    time += 1
    if is_fin: # True면, 1이 넘어가면,
        time = 0
        break

print(time)
