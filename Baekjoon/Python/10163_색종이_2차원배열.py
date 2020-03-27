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
'''
차례로 색종이를 놓고
차례로 놓인 색종이들이 보이는 면적을 
순서대로 출력해야 하므로
색종이들은 이름을 가지고 있어야 한다.
'''


def check(arr):
    cnt_list = []
    # 색종이의 이름 == 숫자와 보드에 있는 숫자와 동일한것의 개수를 세고,
    # 그 개수를 리스트에 넣은 다음에 리턴한다.
    for n in num:
        cnt = 0
        for iy in range(101):
            for ix in range(101):
                if arr[iy][ix] == n:
                    cnt += 1
        cnt_list.append(cnt)
    return cnt_list

# 색종이 수
N = int(input())
# 보드판
board = [ [0]*101 for _ in range(101) ]
# 색종이 이름 == 숫자 (명시적으로!, 그냥 1, N+1로 해도 됨)
num = [ _ for _ in range(1, N+1, 1) ]
# 1 부터 색종이가 들어오는 수 만큼 숫자로 이름을 가진 리스트를 만든다.

for n in range(1, N+1):
    # ix, iy 시작점  ix2 너비 iy2 높이
    ix, iy, ix2, iy2 = map(int, input().split())
    # ix+ix2 끝점
    # iy+iy2 끝
    for y in range(iy, (iy+iy2)): # 너비와 높이를 포함해서 +1을 할 필요가 없다. ! 중요
        for x in range(ix, (ix+ix2)):
            # 받는 그 인덱스가 곧 색종이가 가진 이름과 동일하다.
            board[y][x] = n

# 색칠이 끝나면 check한다.
res = check(board)

# res에서 받은 cnt_list 의 원소를 하나 하나 차례로 출력한다.
for result in res:
    print(result)


