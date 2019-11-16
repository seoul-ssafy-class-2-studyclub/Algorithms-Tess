# import sys
# sys.stdin = open('5650.txt', 'r')
T = int(input())
dir = [(-1,0), (1,0), (0,-1), (0,1)]
first = {
    (-1, 0) : (1, 0), #
    (1, 0): (0, 1), #
    (0, -1): (-1, 0), #
    (0, 1): (0, -1), #
}
second = {
    (-1, 0): (0, 1), #
    (1, 0): (-1, 0), #
    (0, -1): (1, 0), #
    (0, 1): (0, -1), #
}
third = {
    (-1, 0): (0, -1), #
    (1, 0): (-1, 0),
    (0, -1): (0, 1),
    (0, 1): (1, 0),
}
fourth = {
    (-1, 0): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (0, 1),
    (0, 1): (-1, 0),
}
fifth = {
    (-1, 0): (1, 0),
    (1, 0): (-1, 0),
    (0, -1): (0, 1),
    (0, 1): (0, -1),
}
def solve(y, x, dy, dx, sty, stx):
    global mymax, board
    stack = []
    stack.append((y, x, dy, dx, 0))
    while stack:
        y, x, dy, dx, cnt = stack.pop()
        iy = y + dy
        ix = x + dx
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == -1 or (iy == sty and ix == stx):
                mymax = max(mymax, cnt)
                return
            elif board[iy][ix] == 0:
                stack.append((iy, ix, dy, dx, cnt))
            elif board[iy][ix] == 1:
                newdir = first[(dy, dx)]
                stack.append((iy, ix, newdir[0], newdir[1], cnt + 1))
            elif board[iy][ix] == 2:
                newdir = second[(dy, dx)]
                stack.append((iy, ix, newdir[0], newdir[1], cnt + 1))
            elif board[iy][ix] == 3:
                newdir = third[(dy, dx)]
                stack.append((iy, ix, newdir[0], newdir[1], cnt + 1))
            elif board[iy][ix] == 4:
                newdir = fourth[(dy, dx)]
                stack.append((iy, ix, newdir[0], newdir[1], cnt + 1))
            elif board[iy][ix] == 5:
                newdir = fifth[(dy, dx)]
                stack.append((iy, ix, newdir[0], newdir[1], cnt + 1))
            elif board[iy][ix] > 5:
                mytemp = warmhole[board[iy][ix]]
                for tmp in mytemp:
                    if tmp != (iy, ix):
                        stack.append((tmp[0], tmp[1], dy, dx, cnt))
        elif iy == N and 0 <= ix < N:
            stack.append((iy, ix, -1, 0, cnt+1))
        elif iy == -1 and 0 <= ix < N:
            stack.append((iy, ix, 1, 0, cnt+1))
        elif ix == N and 0 <= iy < N :
            stack.append((iy, ix, 0, -1, cnt+1))
        elif ix == -1 and 0 <= iy < N:
            stack.append((iy, ix, 0, 1, cnt+1))
    return
for tc in range(1, T+1):
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N)]
    warmhole = {}
    start = []
    for y in range(N):
        for x in range(N):
            if 6 <= board[y][x] <= 10:
                if warmhole.get(board[y][x]) == None:
                    warmhole[board[y][x]] = []
                warmhole[board[y][x]].append((y, x))
            if board[y][x] == 0:
                start.append((y, x))
    mymax = -1e9
    for st in start:
        for dy, dx in dir:
            solve(st[0], st[1], dy, dx, st[0], st[1])
    print(f'#{tc} {mymax}')