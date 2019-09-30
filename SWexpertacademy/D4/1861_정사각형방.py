import sys
sys.stdin = open('1861.txt', 'r')

'''
#1 6 8
#2 3 2
'''
# 모든 방을 돌면서, 상하좌우를 도는데,
# 돌 예정인 상하좌우중에서, 현재보다 +1만 큰 곳을 다음 이동할 곳으로 확정하고,
# 재귀를 호출한다. 이때 인자로 cnt+1을 넘겨준다. 시작방번호도 항상 들고있는다.
# 그렇지 않은 경우는 버린다. -> cnt 를 시작 방번호에 추가해준다.

def solve(y, x, cnt, start):

    if dp[start] < cnt:
        dp[start] = cnt

    for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
        iy = dy + y
        ix = dx + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == board[y][x] + 1:
                # print(board[iy][ix], board[y][x] + 1, start)
                solve(iy, ix, cnt+1, start)

for tc in range(int(input())):
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N) ]

    dp = dict()
    for y in range(N):
        for x in range(N):
            # y, x, count
            dp[board[y][x]] = 0
            solve(y, x, 1, board[y][x])

    myres = -9999
    myroom = []
    for value in dp.values():
        if value >= myres: # value가 가장 크거나 같은 것 중에,
            # print(value)
            myres = value

    for key, value in dp.items():
        if value == myres:
            myroom.append(key)
    # print(dp)
    print(f'#{tc+1}', min(myroom), myres)



# from collections import deque
# dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# for case in range(1, int(input()) + 1):
#     N = int(input())
#     house = [list(map(int, input().split())) for _ in range(N)]
#     dp = [[0] * N for _ in range(N)]
#     res = 0
#     idx = N ** 2
#     for r in range(N):
#         for c in range(N):
#             # not dp[r][c] -> 아직 확인한 적 없는 방이라면 시작.
#             if not dp[r][c]: # False라면, 비었다면
#                 queue = deque()
#                 queue.append((r, c))
#                 while queue:
#                     y, x = queue.popleft()
#                     for b, a in dxy:
#                         yi = y + b
#                         xi = x + a
#                         if 0 <= yi < N and 0 <= xi < N and house[yi][xi] == house[y][x] + 1:
#                             # dp[yi][xi]에 값이 있다면 이미 탐색을 끝낸 방이므로, 값을 가져오고 더 이상 진행하지 않는다.
#                             if dp[yi][xi]: # True 라면,
#                                 dp[r][c] += dp[yi][xi] + 1
#                             else:
#                                 # bfs로 탐색하면서 dp[r][c]에 방 갯수 저장.
#                                 # 중간에 들르는 방들은 어차피 답이 될 수 없으니 그냥 1로 둔다.
#                                 dp[r][c] += 1
#                                 dp[yi][xi] += 1
#                                 queue.append((yi, xi))
#             if dp[r][c] > res:
#                 res = dp[r][c]
#                 idx = house[r][c]
#             elif dp[r][c] == res and idx > house[r][c]:
#                 res = dp[r][c]
#                 idx = house[r][c]
#     print(house)
#     print(dp)
#     print(f'#{case} {idx} {res + 1}')