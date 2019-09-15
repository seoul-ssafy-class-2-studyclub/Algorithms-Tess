import sys
# sys.stdin = open('7576.txt', 'r')
import collections

'''
1에 대한 좌표를 계속 0,0 부터 끝까지 찾아서 함수에 넣는건 시간초과가 걸리기때문에
함수 안에서 bfs로 같은 계층이 끝나면 다음 계층으로 시작하고, 
새 시작하는 경우 그때 day += 1을 하는 방법으로 시간초과 문제를 해결
'''

def bfs():
    global zeros
    global day
    q = collections.deque([])
    for y in range(N):
        for x in range(M):
            if tomatos[y][x] == 1 and visited[y][x] == False:
                visited[y][x] = True
                q.append((y, x))
    while q:
        day += 1
        for _ in range(len(q)):
            y, x = q.popleft()
            for dy, dx in [(0,1), (0,-1), (1,0), (-1, 0)]:
                iy = dy + y
                ix = dx + x
                if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == False:
                    if tomatos[iy][ix] == 0:
                        zeros -= 1
                        tomatos[iy][ix] = 1
                        q.append((iy, ix))
                        if zeros == 0:
                            return day
    return -1

M, N = map(int, sys.stdin.readline().split())
tomatos = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

zeros = 0
for y in range(N):
    for x in range(M):
        if tomatos[y][x] == 0:
            zeros += 1
res = -1
day = 0
while True:
    if zeros == 0:
        res = 0
        break
    res = bfs()
    if res > -1:
        break
    else:
        break
print(res)


