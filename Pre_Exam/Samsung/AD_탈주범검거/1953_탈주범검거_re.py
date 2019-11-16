import sys
sys.stdin = open('1953.txt', 'r')

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
tunnel = {
    1: [0, 1, 2, 3],
    2: [2, 3],
    3: [0, 1],
    4: [0, 3],
    5: [0, 2],
    6: [1, 2],
    7: [1, 3]
}
nxt = {
    3: [1,2,5,6],
    2: [1,2,4,7],
    0: [7,6,3,1],
    1: [5,4,3,1]
}
def solve(y, x, l):
    global L, vis, path
    path.add((y, x))
    if l == 0:
        return
    for i in tunnel[board[y][x]]:
        dy, dx = dir[i]
        iy = dy + y
        ix = dx + x
        if 0 <= iy < N and 0 <= ix < M and vis[iy][ix] == False:
            if board[iy][ix] in nxt[i]:
                vis[iy][ix] = True
                solve(iy, ix, l-1)
                vis[iy][ix] = False
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(N) ]
    vis = [ [False]*M for _ in range(N) ]
    path = set()
    vis[R][C] = True
    solve(R, C, L-1)
    print(f'#{tc} {len(path)}')


