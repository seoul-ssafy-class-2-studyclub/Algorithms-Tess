import sys
sys.stdin = open('2805.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    visit = [[False]*N for _ in range(N)]
    stack = []
    for y in range(N):
        if y == 0:
            stack.append((y, N//2))

        elif y < (N//2+1):
            for i in range(y+1):
                X = N // 2 - i # 2-
                X2 = N // 2 + i
                if 0 <= X < N or 0 <= X2 < N:
                    stack.append((y, X))
                    stack.append((y, X2))
        elif y >= (N//2+1):
            for i in range(N - y):
                X = N // 2 - i
                X2 = N // 2 + i
                if 0 <= X < N or 0 <= X2 < N:
                    stack.append((y, X))
                    stack.append((y, X2))

    new = 0
    while stack:
        y, x = stack.pop()
        if visit[y][x] == False:
            new += board[y][x]
            visit[y][x] = True
    print(f'#{tc}', new)


    #
    # temp = 0
    # for yi in range(N):
    #     temp += board[yi][N//2]
    # print(total, temp)
    # result = total - temp
    # print(f'#{tc}', result)

'''
23 결과

6 중복
'''



'''
#1 23
#2 1190 # 3 1187
#3 946 # 1
#4 112
#5 1886 # 4
#6 3000
#7 1032
#8 1330
#9 939
#10 2960
#11 547
#12 3016
#13 1712
#14 2049
#15 1294
#16 354
#17 1634
#18 1901
#19 2518
#20 1750
#21 2144
#22 940
#23 0
#24 1712
#25 1685
#26 559
#27 874
#28 75
#29 139
#30 3
'''