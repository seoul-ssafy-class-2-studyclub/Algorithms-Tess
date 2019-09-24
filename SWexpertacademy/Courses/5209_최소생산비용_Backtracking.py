import sys
sys.stdin = open('5209.txt', 'r')

def dfs_backtracking(nowy, nowx, temp, vis):
    global mymin
    temp += board[nowy][nowx]
    # print(vis)
    if nowy == N-1: # 2면,
        if mymin > temp:
            mymin = temp
            return

    elif nowy < N and vis[nowx] == False: # 3전, 0 1 2
        if mymin < temp: # 가지치기
            return
        vis[nowx] = True
        for i in range(N):
            if vis[i] == False:
                dfs_backtracking(nowy+1, i, temp, vis)
        vis[nowx] = False

for tc in range(int(input())):
    N = int(input())

    board = [ list(map(int, input().split())) for _ in range(N) ]

    mymin = float('inf')
    for x in range(N):
        vis = [False]*N
        dfs_backtracking(0, x, 0, vis)
    print(f'#{tc+1}', mymin)