import sys
sys.stdin = open('2583.txt', 'r')

from pprint import pprint

M, N, K = map(int, input().split())
board = [[0]*(N) for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[j][i] = -1

def coloring(x, y, name):
    global vis, ans
    q = []
    q.append((x, y, 1))
    board[x][y] = name
    vis[x][y] = True
    while q:
        x, y, cnt = q.pop(0)
        for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
            iy, ix = dy+y, dx+x
            if 0 <= iy < N and 0 <= ix < M:
                if vis[ix][iy] == False and board[ix][iy] == 0:
                    board[ix][iy] = name
                    q.append((ix, iy, cnt + 1))
                    ans[name] += 1

ans = [1]*100001
name = 1
vis = [[False]*(N) for _ in range(M)]
for x in range(M):
    for y in range(N):
        if board[x][y] == 0 and vis[x][y] == False:
            coloring(x, y, name)
            name += 1
names = [i for i in range(1, name+1)]
answer = []
for n in names[:-1]:
    answer.append(ans[n])
print(name-1)
print(' '.join(map(str,list(sorted(answer)))))