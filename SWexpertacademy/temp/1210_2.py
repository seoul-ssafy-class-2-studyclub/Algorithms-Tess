import sys
sys.stdin = open('1210.txt', 'r')
for _ in range(10):
    T = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    tempdy = 99
    tempdx = mat[99].index(2)
    while tempdy >= 0:
        if tempdy == 0:
            print(f'#{T}', tempdx)
            break
        elif tempdx == 0:
            for dy, dx in [[0, 1], [-1, 0]]:
                if mat[tempdy+dy][tempdx+dx] == 1:
                    mat[tempdy + dy][tempdx + dx] = 3
                    tempdy, tempdx = tempdy + dy, tempdx + dx
        elif tempdx == 99:
            for dy, dx in [[0, -1], [-1, 0]]:
                if mat[tempdy + dy][tempdx + dx] == 1:
                    mat[tempdy + dy][tempdx + dx] = 3
                    tempdy, tempdx = tempdy + dy, tempdx + dx
        elif 1 <= tempdx < 99:
            for dy, dx in [[0, 1],[0, -1],[-1, 0]]:
                if mat[tempdy + dy][tempdx + dx] == 1:
                    mat[tempdy + dy][tempdx + dx] = 3
                    tempdy, tempdx = tempdy + dy, tempdx + dx