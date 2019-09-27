import sys
sys.stdin = open('1861.txt', 'r')


from collections import deque
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for case in range(1, int(input()) + 1):
    N = int(input())
    house = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    res = 0
    idx = N ** 2
    for r in range(N):
        for c in range(N):
            # not dp[r][c] -> 아직 확인한 적 없는 방이라면 시작.
            if not dp[r][c]: # False라면, 비었다면
                queue = deque()
                queue.append((r, c))
                while queue:
                    y, x = queue.popleft()
                    for b, a in dxy:
                        yi = y + b
                        xi = x + a
                        if 0 <= yi < N and 0 <= xi < N and house[yi][xi] == house[y][x] + 1:
                            # dp[yi][xi]에 값이 있다면 이미 탐색을 끝낸 방이므로, 값을 가져오고 더 이상 진행하지 않는다.
                            if dp[yi][xi]: # True 라면,
                                dp[r][c] += dp[yi][xi] + 1
                            else:
                                # bfs로 탐색하면서 dp[r][c]에 방 갯수 저장.
                                # 중간에 들르는 방들은 어차피 답이 될 수 없으니 그냥 1로 둔다.
                                dp[r][c] += 1
                                dp[yi][xi] += 1
                                queue.append((yi, xi))
            if dp[r][c] > res:
                res = dp[r][c]
                idx = house[r][c]
            elif dp[r][c] == res and idx > house[r][c]:
                res = dp[r][c]
                idx = house[r][c]
    print(house)
    print(dp)
    print(f'#{case} {idx} {res + 1}')