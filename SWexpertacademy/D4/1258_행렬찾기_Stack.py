import sys
sys.stdin = open('1258.txt', 'r')
# from heapq import heappush

'''
#1 2 2 1 1 4 
#########
#2 4 1 2 5 1 2 4 4 3
#3 6 1 2 2 3 8 1 3 7 5 8 9 5
#4 10 1 8 2 5 11 1 12 2 5 6 8 4 6 9 4 15 9 10 10 11
#5 8 1 6 10 2 2 15 6 11 7 14 11 10 17 7 15 17
#6 10 1 10 16 1 7 4 4 18 11 7 6 16 18 6 12 11 15 12 13 15
#7 13 1 13 6 3 19 1 3 12 8 6 12 4 4 14 7 11 15 8 14 10 11 15 10 19 13 20
#8 15 2 1 3 4 1 22 4 13 8 9 25 3 12 8 9 11 10 17 15 12 13 15 11 18 22 10 18 23 17 25
#9 18 8 2 3 7 4 10 15 3 9 6 14 4 11 8 7 16 6 21 16 9 10 17 21 14 27 11 17 18 18 20 26 15 20 23 23 27
#10 20 2 1 13 2 5 6 4 13 14 5 6 15 25 4 9 16 12 14 21 8 16 11 22 9 20 10 10 21 8 29 11 25 15 22 30 12 29 28 28 30
'''

def colouring(starty, startx):
    global board
    global xcnt, ycnt
    tempx = startx
    y = starty
    x = startx
    stack = []
    stack.append((y, x))

    while stack:
        y, x = stack.pop()
        board[y][x] = 0
        iy = y + dy[0]
        ix = x + dx[0]

        if 0 <= iy < n and 0 <= ix < n:
            if board[iy][ix] > 0: # 다음줄이 0이 아니라면,
                stack.append((iy, ix))
                xcnt += 1
            elif board[iy][ix] == 0 and board[y+1][x] != 0: # 앞부분이 0이면서 아래부분이 0이 아닌경우 더 진행해야한다.
                iy = y + 1
                ix = tempx
                ycnt += 1
                xcnt = 1
                stack.append((iy, ix))

        elif (n-1) < ix and board[iy+1][tempx] != 0:
            iy = y + 1
            ix = tempx
            ycnt += 1
            xcnt = 1
            stack.append((iy, ix))
    return (ycnt, xcnt)

dy = [0]
dx = [1]

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    yxcnt_list = []
    for Y in range(n):
        for X in range(n):
            if board[Y][X] != 0:
                xcnt = 1
                ycnt = 1
                yxcnt = colouring(Y, X)
                yxcnt_list.append(yxcnt)
    print(f'#{tc}', len(yxcnt_list), end=' ')
    res = []
    for idx in range(len(yxcnt_list)):
        y, x = yxcnt_list[idx]
        res.append((y*x, y, x))
    res = list(sorted(res))
    for r in res:
        t, y, x = r
        print(y, x, end=' ')
    print()