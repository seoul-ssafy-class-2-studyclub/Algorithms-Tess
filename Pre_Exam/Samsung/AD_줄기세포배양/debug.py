import sys
sys.stdin = open('5654.txt', 'r')
from pprint import pprint

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for tc in range(1): # 테케1만
    N, M, K = map(int, input().split())
    XM = 100
    XN = 100
    board = [ list(map(int, input().split())) for _ in range(N)]
    chk = [[0]*XN for _ in range(XM)]
    # pprint(chk)

    cells_info = []
    for y in range(N):
        for x in range(M):
            if board[y][x] != 0:
                chk[y+100][x+100] = board[y][x]
                cells_info.append([board[y][x], 1, y+50, x+50, 0])
    cells_info = list(reversed(list(sorted(cells_info))))

    for k in range(0, K+1):
        fin = len(cells_info)
        count = 0
        while fin != count:
            lifes, status, y, x, cnt = cells_info.pop(0)
            count += 1
            if cnt == lifes and status == 1:
                cells_info.append((lifes, status+1, y, x, cnt))
            if cnt < lifes and status == 1:
                cells_info.append((lifes, status, y, x, cnt+1))
            if cnt == lifes and status == 2:
                for iy, ix in [(0,1), (1, 0), (0,-1), (-1,0)]:
                    dy = iy + y
                    dx = ix + x
                    if 0 <= dy < XM and 0 <= dx < XN: # and lifes > chk[dy][dx]
                        if chk[dy][dx] < lifes:
                            chk[dy][dx] = lifes
                            cells_info.append((chk[dy][dx], 1, dy, dx, 0))
                        else:
                            continue
                cells_info.append((lifes, status, y, x, cnt+1))
            if lifes*2 == cnt and status == 2:
                continue
    print(len(cells_info))