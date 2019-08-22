import sys
sys.stdin = open('2578.txt', 'r')


def check(board):
    final = []

    # 가로
    for col in range(5):
        row_cnt = 0
        for row in range(5):
            if board[col][row] == 'B':
                row_cnt += 1
        final.append(row_cnt)

    # 세로
    for col in range(5):
        col_cnt = 0
        for row in range(5):
            if board[row][col] == 'B':
                col_cnt += 1
        final.append(col_cnt)

    # 대각선 왼쪽부터
    left_cnt = 0
    for col in range(0, 5):
        if board[col][col] == 'B':
            left_cnt += 1
    final.append(left_cnt)

    # 대각선 오른쪽부터
    # 4,0 3,1 2,2 1,3 0,4
    right_cnt = 0
    for col in range(4, -1, -1):
        if board[col][4-col] == 'B':
            right_cnt += 1
    final.append(right_cnt)

    total = 0
    for item in final:
        if item == 5:
            total += 1

    if total >= 3:
        return 3

    else:
        return 0


Bingo_Board = [list(map(str, input().split())) for _ in range(5)]
speakers = []
for _ in range(5):
    speakers.extend(list(map(str, input().split())))

## while 안에서 flag 사용법
flag = False
cnt = 0
while flag == False:
    for si in range(len(speakers)):
        if flag == True:
            break
        for col in range(5):
            if flag == True:
                break
            for row in range(5):
                if cnt < 11:
                    if Bingo_Board[col][row] == speakers[si]:
                        Bingo_Board[col][row] = 'B'
                        cnt += 1
                # 안에서 카운트
                elif cnt >= 11:
                    if Bingo_Board[col][row] == speakers[si]:
                        Bingo_Board[col][row] = 'B'
                        cnt += 1
                        res = check(Bingo_Board)
                        if res == 3:
                            flag = True
                            break
print(si)

