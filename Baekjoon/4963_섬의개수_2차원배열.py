import sys
sys.stdin = open('4963.txt', 'r')



import sys

while True:

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]


    def check(arr):

        result = 0
        for iy in range(H):
            for ix in range(W):
                if arr[iy][ix] == 1:
                    return 1
        return result


    def colouring(y, x):
        global board

        stack = []

        stack.append((y, x))

        while stack:

            y, x = stack.pop()
            board[y][x] = 0

            for idx in range(8):
                tempy = y + dy[idx]
                tempx = x + dx[idx]

                if 0 <= tempy <= H-1 and 0 <= tempx <= W-1 and board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))

        return 1

    W, H = map(int, sys.stdin.readline().split())

    if H == 0 and W == 0:
        break

    board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

    cnt = 0
    res = 1
    # while문 필요 없는 구간
    for iy in range(H):
        for ix in range(W):
            if H == 1 and W == 1:
                if board[iy][ix] == 1:
                    cnt = 1
                    res = 0
                    break
                elif board[iy][ix] == 0:
                    cnt = 0
                    res = 0
                    break

            else:
                if board[iy][ix] == 1:
                    cnt += colouring(iy, ix)
                    res = check(board)
                    if res == 0:
                        break
    print(cnt)
