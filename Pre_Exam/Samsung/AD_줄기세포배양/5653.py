d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    XM = 600
    XN = 600​
    board = [ list(map(int, input().split())) for _ in range(N)]

    chk = [[0]*XN for _ in range(XM)]
    cells_info = []
    for y in range(N):
        for x in range(M):
            if board[y][x] != 0:
                chk[y+300][x+300] = board[y][x]
                cells_info.append([board[y][x], 1, y+300, x+300, 0])
    cells_info = sorted(cells_info, reverse=True)
    for k in range(K):
        fin = len(cells_info)
        while fin:
            fin -= 1
            lifes, status, y, x, cnt = cells_info.pop(0)
            cnt += 1
            if cnt == lifes and status == 1:
                cells_info.append((lifes, status+1, y, x, cnt))
            elif (cnt < lifes and status == 1) or (lifes*2 > cnt > lifes + 1 and status == 2):
                cells_info.append((lifes, status, y, x, cnt))
            elif cnt == lifes + 1 and status == 2:
                for iy, ix in [(0,1), (1, 0), (0,-1), (-1,0)]:
                    dy = iy + y
                    dx = ix + x
                    if 0 <= dy < XM and 0 <= dx < XN:
                        if chk[dy][dx] == 0:
                            chk[dy][dx] = lifes
                            cells_info.append((lifes, 1, dy, dx, 0))
                        else:
                            continue
                if lifes*2 == cnt and status == 2:
                    # 아래 continue를 하면 가장 가까운 반복문(while)을 넘어간다.
                    continue
                cells_info.append((lifes, status, y, x, cnt))
    #    print(len(cells_info))
    print(len(cells_info))