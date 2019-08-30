
import sys
sys.stdin = open('1974.txt', 'r')



T = int(input())


for tc in range(1, T+1):
    counting = []
    for i in range(1, 10):
        counting.append(i)

    result = []

    sdo = [list(map(int, input().split())) for _ in range(9)]

    #가로
    for i in sdo:
        if sum(i) != 45:
            result.append(0)
    #세로
    col_sdo = []
    for iy in range(9):
        new_sdo = []
        for ix in range(9):
            new_sdo.append(sdo[ix][iy])
        col_sdo.append(new_sdo)

    for i in col_sdo:
        if sum(i) != 45:
            result.append(0)

    #3*3
    for iy in range(0, 9, 3):
        for ix in range(0, 9, 3):
            total = 0
            for y in range(3):
                for x in range(3):
                    total += sdo[iy+y][ix+x]

            if total != 45:
                result.append(0)
    # 0이 들어있으면 틀린 것
    if len(result) != 0:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', 1)



