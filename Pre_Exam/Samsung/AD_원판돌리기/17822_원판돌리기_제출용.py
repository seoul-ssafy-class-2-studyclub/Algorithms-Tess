import collections
def checkBFS():
    global board
    tempcnt = 0
    q = []
    for y in range(1, N+1):
        for x in range(M):
            for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                iy = y + dy
                ix = x + dx
                if 1 <= iy < N+1 and board[y][x] != 0:
                    if ix == -1: # ix가 -1인 경우,
                        ix = M-1
                        if board[y][x] == board[iy][ix]:
                            q.append((y, x))
                            q.append((iy, ix))
                            tempcnt = 1

                    elif ix == M: #ix가 M인 경우,
                        ix = 0
                        if board[y][x] == board[iy][ix]:
                            q.append((y, x))
                            q.append((iy, ix))
                            tempcnt = 1

                    # 모두 괜찮은 경우
                    elif board[y][x] == board[iy][ix]:
                        q.append((y, x))
                        q.append((iy, ix))
                        tempcnt = 1
    while q:
        y, x = q.pop()
        board[y][x] = 0

    return tempcnt

N, M, T = map(int, input().split())
board = []
temp = collections.deque([0]*M)
board.append(temp)

for _ in range(N):
    data = collections.deque(list(map(int, input().split())))
    board.append(data)

for _ in range(T):
    xi, di, ki = map(int, input().split())
    for par in range(xi, N+1, xi):
        cnt = 0
        if di == 0:
            while cnt != ki:
                temp = board[par].pop()
                board[par].appendleft(temp)
                cnt += 1

        if di == 1:
            while cnt != ki:
                temp = board[par].popleft()
                board[par].append(temp)
                cnt += 1
    fin = checkBFS()
    if fin == 0:
        # 인접한게 없을때만 작동
        res = 0
        num = 0
        for y in range(N+1):
            for x in range(M):
                if board[y][x] != 0:
                    res += board[y][x]
                    num += 1
        try:
            res = res/num
        except ZeroDivisionError:
            res = 0

        for y in range(N+1):
            for x in range(M):
                # 순서가 존재하는 if로 해야한다.
                if float(board[y][x]) > res and board[y][x] != 0:
                    # res가 더 작다.
                    # 평균보다 큰 수이다.
                    board[y][x] = board[y][x]-1
                elif float(board[y][x]) < res and board[y][x] != 0:
                    board[y][x] = board[y][x]+1

res = 0
for y in range(1, N+1):
    for x in range(M):
        res += board[y][x]
print(res)