from sys import stdin
input = stdin.readline

stdin = open('17070.txt', 'r')
# 가로 0 세로 1 대각선 2
N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
print(dp)
dp[0][1][0] = 1
for r in range(N):
    for c in range(2, N):
        if r == 0:
            if house[r][c]:
                continue
            dp[r][c][0] = dp[r][c-1][0] 
        if not house[r][c] and not house[r-1][c] and not house[r][c-1]:
            dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]
        if not house[r][c]:
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
print(dp)
print(sum(dp[N-1][N-1]))