

dy = [0, 1, -1, 0] # 우선순위: 오른, 아래, 왼, 위
dx = [1, 0, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    board = [list(map(int, input())) for _ in range(N)]



    # 2에서 출발해서 네방향으로 0을ㅈ따라가고, 3을 찾을때까지 반복해야한다.
    start_point = []
    for i in range(N):
        if 2 in board[i]:
            start_point.append(i)
            start_point.append(board[i].index(2))
    #출발포인트

    xi, yi = 0, 0
    stack = []
    iy, ix = start_point
    stack.append((iy, ix))
    visited = [[False]*N for _ in range(N)]
    res = 0

    while stack:
        iy, ix = stack.pop()

        # if 0 <= xi < N and 0 <= yi < N:
        #     # 3 찾으면 리턴
        #     if board[yi][xi] == 3:
        #         print(1)
        #         break

        for idx in range(4):
            xi = ix + dx[idx]
            yi = iy + dy[idx]
            if 0 <= xi < N and 0 <= yi < N:
                if board[yi][xi] == 0 and not visited[yi][xi]:
                    stack.append((yi, xi))
                    visited[yi][xi] = True
                if board[yi][xi] == 3 and not visited[yi][xi]:
                    res = 1
                    break

    print(f'#{tc}', res)
    # 못찾고 스택이 비면 0 리턴