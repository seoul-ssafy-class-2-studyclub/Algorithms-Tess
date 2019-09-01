import sys
sys.stdin = open('5356.txt', 'r')

'''

A A B C D D

a f z z

0 9 1 2 1

a 8 E W g 6

P 5 h 3 k x

Aa0aPAf985Bz1EhCz2W3D1gkD6x

Aa0aPAf985Bz1EhCz2W3D1gkD6x
'''

# 1. 보드를 받는다

# 2. 5 길이를 가지지 않은 보드에 -1을 extend하여 채워준다.
# 2. 받은 보드를 가로로 돌린다.

def result():
    string = []
    for y in range(15):
        for x in range(5):
            if board[x][y] != -1:
                string.append(board[x][y])
    return string

def board_start():
    for bd in board:
        if len(bd) != 15:
            need = 15 - len(bd)
            need_board = [-1]*need
            bd += need_board[:]

T = int(input())
for tc in range(1, T+1):
    board = [list(map(str, input())) for _ in range(5)]
    board_start()
    string = result()
    print(f'#{tc}', ''.join(string))



