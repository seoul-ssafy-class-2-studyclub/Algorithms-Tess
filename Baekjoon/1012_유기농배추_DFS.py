import sys
sys.stdin = open('1012.txt', 'r')

def DFS(Y, X, name):
    stack = []
    stack.append((Y, X))
    while stack:
        y, x = stack.pop()
        mymap[y][x] = name
        for dy, dx in [(0,1), (1,0), (-1,0), (0,-1)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < M and mymap[iy][ix] == -1:
                stack.append((iy, ix))

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    mymap = [[0]*(M) for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        mymap[Y][X] = -1

    counting = 0
    for y in range(N):
        for x in range(M):
            if mymap[y][x] == -1:
                counting += 1 
                DFS(y, x, counting)
    print(counting)