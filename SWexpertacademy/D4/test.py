

# recursion dfs
def mpermut(pro=1, k=0):
    global mmax
    if k == N:
        if pro > mmax:
            mmax = pro
            return True
    for i in range(N): # 0-4
        if visited[i] == False:
            temp = pro * (board[k][i] / 100)
            if temp != 0 and (not mmax or temp > mmax):
                visited[i] = True
                mpermut(temp, k+1)
                visited[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N
    mmax = 0
    mpermut()
    print(f'#{tc} {mmax * 100:.6f}')