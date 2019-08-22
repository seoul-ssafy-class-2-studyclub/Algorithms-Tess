'''
2
0 0 10 10
2 2 6 6

64
36
'''


#15 -> 101로 변경

import sys
sys.stdin = open('10163.txt', 'r')

def check(arr):
    cnt_list = []
    for n in num:
        cnt = 0
        for iy in range(101):
            for ix in range(101):
                if arr[iy][ix] == n:
                    cnt += 1
        cnt_list.append(cnt)
    return cnt_list

N = int(input())
board = [ [0]*101 for _ in range(101) ]
num = [ _ for _ in range(1, N+1, 1) ]

for n in range(1, N+1):
    ix, iy, ix2, iy2 = map(int, input().split())
    # ix+ix2 끝점
    # iy+iy2 끝
    for y in range(iy, (iy+iy2)): # 너비와 높이를 포함해서 +1을 할 필요가 없다.
        for x in range(ix, (ix+ix2)):
            board[y][x] = n

res = check(board)

for result in res:
    print(result)


