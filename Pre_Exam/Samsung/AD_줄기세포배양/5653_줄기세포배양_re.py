import sys
sys.stdin = open('5654.txt', 'r')


T = int(input())
# 세로 크기 N
# 가로 크기 M
# 배양 시간 K

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    boards = [list(map(int, input().split())) for _ in range(N)]
    cells = []
    XN = 700
    XM = 700
    board = [[0]*XN for _ in range(XM)]
    for y in range(N):
        for x in range(M):
            if boards[y][x]:
                cells.append((boards[y][x], y+350, x+350, 1, 0))
                board[y+350][x+350] = boards[y][x]
    # K만큼 돈다.
    cells = sorted(cells, reverse=True)
    # print(cells)
    for _ in range(K):
        fin = len(cells)
        # print(cells)
        while fin:
            fin -= 1
            life, y, x, status, cnt = cells.pop(0)
            cnt += 1
            if (cnt < life and status == 1) or (life+1 < cnt < life*2 and status == 2):
                cells.append((life, y, x, status, cnt))
            elif life == cnt and status == 1:
                cells.append((life, y, x, status+1, cnt))
            elif life+1 == cnt and status == 2:
                for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
                    iy = dy + y
                    ix = dx + x
                    # 새로짠 보드에 맞는 범위로 설정
                    if 0 <= iy < XN and 0 <= ix < XM:
                        if board[iy][ix] == 0:
                            board[iy][ix] = life
                            cells.append((life, iy, ix, 1, 0))
                        else:
                            continue
                if cnt != life*2 and status == 2:
                    cells.append((life, iy, ix, status, cnt))
    print(f'#{tc} {len(cells)}')




