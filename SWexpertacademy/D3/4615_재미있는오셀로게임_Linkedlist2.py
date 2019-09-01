import sys
sys.stdin = open('4615.txt', 'r')
from pprint import pprint

d = [(-1, 0),(-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1),(-1,-1)]

for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    c = N // 2 # N 을 2로 나눈다.
    board = [[0] * N for i in range(N)]

    # 기본으로 놓여지는 흑, 백 바둑판
    # 1은 흑, 2는 백
    board[c-1][c-1] = 2
    board[c][c] = 2
    board[c-1][c] = 1
    board[c][c-1] = 1

    for m in range(M):
        x, y, color = map(int, input().split())
        #print(x, y, color)
        #놓여지는 좌표는 1이 더 많기때문에 편의상 1씩 빼준다.
        x -= 1
        y -= 1
        # 만약 1의 차례라면 상대편은 2이다. 를 명시
        if color == 1:
            another = 2
        else:
            another = 1

        # 놓을 곳에 해당 돌을 놓는다.
        board[y][x] = color

        #그리고 8번을 돌면서,
        for dy, dx in d:
            xi = x + dx
            yi = y + dy
            # 범위제한,
            if xi < 0 or yi < 0 or xi >= N or yi >= N:
                continue

            # 범위안에 있는 좌표에 상대방이 있는 경우
            if board[yi][xi] == another:
                # 카운트 시작
                cnt = 0
                # 범위안에 상대방이 있을때까지 카운트를 한다.
                while board[yi][xi] == another:
                    cnt += 1

                    # 만든 범위에 또 더해주고,
                    xi += dx
                    yi += dy

                    # 만약에 범위를 벗어나거나, 보드가 0이라면, 바꿔줄 필요가 없으므로
                    if xi < 0 or yi < 0 or xi >= N or yi >= N or board[yi][xi] == 0:
                        # 카운트를 0으로 만들고 브레이크해서 while을 빠져나온다.
                        # 0으로 하지 않으면 카운트가 남아있는 상태에서 아래의 while문으로 들어가기때문에 초기화
                        cnt = 0

                        break

                # 처음위치 초기화
                xi = x + dx
                yi = y + dy

                # 카운트가 0이 아니라면 반복 시작
                while cnt != 0:
                    # 해당 부분에 내가 있다면,
                    board[yi][xi] = color

                    # 만든 범위에 또 더해주고,
                    xi += dx
                    yi += dy
                    # 카운트를 빼준다.
                    cnt -= 1


    # 최종적으로 결과 산출 코드
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f'#{case} {black} {white}')