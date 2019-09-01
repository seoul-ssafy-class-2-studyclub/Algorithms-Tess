import sys
sys.stdin = open('4751.txt', 'r')


# 문자열 하나일 때의 마름모꼴 장식이 문자열 하나하나 존재

# '.' '#' 'alphabet'

d = [(-2,0), (-1, 1), (0, 2), (1, 1), (2, 0), (1, -1), (0, -2), (-1, -1)]

T = int(input())
for tc in range(1, T+1):
    string = list(map(str, input()))

    N = len(string)
    board = [['.']*N for _ in range(5)]
    print(board)

    #N//2

    for i in range(N):
        if i%4 == 0:
            #중간처리
            print(i) # 겹치는 부분 x
            print(i+2) # 알파벳 넣는 x
            print(2) # y는 2로 고정


            # 첫줄처리
            print(0) # y는 0으로 고정
            print(i + 2)  # '#' 넣는 x

        # 둘째줄처리 및 위 아래
        if i%2 == 0:
            print('홀수야', i+1)








