import sys
sys.stdin = open('5209.txt', 'r')

def dfs_backtracking(nowy, nowx, temp, vis):
    vis = [:]
    global mymin
    temp += board[nowy][nowx]
    # print(vis)
    if nowy == N-1: # 2면,
        print(vis)
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
        # vis[nowx] = False # 밖에있는 리스트는 카피하지않으면 계속 참조되어서 False로 다시 바꿔줘야함

for tc in range(int(input())):
    N = int(input())

    board = [ list(map(int, input().split())) for _ in range(N) ]

    mymin = float('inf')
    for x in range(N):
        visited = [False]*N
        dfs_backtracking(0, x, 0, visited)
    print(f'#{tc+1}', mymin)
'''
[True, False, False]
'''

# 0 0 0 0
# 1 1 1 1
# 2 2 2 3
# 3 3 4
# 4 4 3