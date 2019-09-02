import sys
sys.stdin = open('4751.txt', 'r')
from pprint import pprint


# 문자열 하나일 때의 마름모꼴 장식이 문자열 하나하나 존재

# '.' '#' 'alphabet'

d = [(-2,0), (-1, 1), (0, 2), (1, 1), (2, 0), (1, -1), (0, -2), (-1, -1)]

T = int(input())
for tc in range(1, T+1):
    string = list(map(str, input()))

    N = len(string)
    Num = 5
    board = [['.']*(5) for _ in range(5)]
    pprint(board)

    #N//2
    #만들면서 색칠해야하나? 한줄씩 생성하면서..

    for char in string:
        for i in range(Num):
            if i%4 == 0:
                #중간처리
                board[2][i] = '#' # 겹치는 부분 x

                if 0 < i+2 < N:
                    board[2][i+2] = char# 알파벳 넣는 x
                    #print(2) # y는 2로 고정


                if 0 < i+1 < N:
                    # 첫줄처리
                    board[0][i+2] = '#'
                    board[4][i + 2] = '#'
                    #print(0) # y는 0으로 고정
                    #print(i + 2)  # '#' 넣는 x

            # 둘째줄처리 및 위 아래
            if i%2 == 0:
                if 0 < i+1 < N:
                    board[1][i+1] = '#'
                    board[3][i + 1] = '#'
                    #print('홀수야', i+1)
    pprint(board)

    




