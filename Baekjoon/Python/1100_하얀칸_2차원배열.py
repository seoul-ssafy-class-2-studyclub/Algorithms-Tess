import sys
sys.stdin = open('1100.txt', 'r')

board = [ list(input()) for _ in range(8)]

cnt = 0
for iy in range(8):
    for ix in range(8):
        if iy%2 == 0:
            if ix%2 == 0:
                if board[iy][ix] == 'F':
                    cnt += 1
        elif iy%2 == 1:
            if ix%2 == 1:
                if board[iy][ix] == 'F':
                    cnt += 1

print(cnt)