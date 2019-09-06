import sys
sys.stdin = open('1949.txt', 'r')


def search(y, x, k, cnt):
    global res

    if res < cnt+1:
        res = cnt+1

    visitied[y][x] = True
    for dy, dx in delta:
        iy = dy + y
        ix = dx + x
        if 0 <= iy < N and 0 <= ix < N and visitied[iy][ix] == False:
            if board[y][x] > board[iy][ix]:
                search(iy, ix, k, cnt+1)
            elif board[y][x] > board[iy][ix] - k:
                temp = board[iy][ix]
                board[iy][ix] = board[y][x] - 1
                # 나를 깍는이유? 나를 기준으로 -1을 한 값을 나보다 큰 숫자에 아예 덮어씌움으로써 나보다는 작지만,
                # 높은 최장 거리를 유지할 수 있다.
                search(iy, ix, 0, cnt+1)
                board[iy][ix] = temp
    visitied[y][x] = False

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리는?
    my_highest = 0
    for y in range(N):
        for x in range(N):
            if my_highest < board[y][x]:
                my_highest = board[y][x]

    # 높은 봉우리들이 있는 좌표는?
    highest_yx = []
    for y in range(N):
        for x in range(N):
            if board[y][x] == my_highest:
                highest_yx.append((y, x))

    # main 함수 시작
    res = 0
    visitied = [[False]*N for _ in range(N)]
    for start_yx in highest_yx:
        search(start_yx[0], start_yx[1], K, 0)

    print(f'#{tc}', res)