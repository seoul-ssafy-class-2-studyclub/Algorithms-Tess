import sys
sys.stdin = open('2001.txt', 'r')

for tc in range(1, int(input())+1):

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]


    counting = []
    for ny in range(N-M+1): # 이 부분 핸들링 중요!
        for nx in range(N-M+1):
            cnt = 0
            for my in range(M):
                for mx in range(M):
                    Y = ny + my
                    X = nx + mx
                    # 매우 유용!
                    if 0 <= Y < N-1 or 0 <= X < N-1:
                        cnt += board[Y][X]
            counting.append(cnt)
    print(f'#{tc}', max(counting))


'''
#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242
'''