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


    # final에 담긴 요소중에 5가 있다면, total을 하나씩 더한다.
    total = 0
    for item in final:
        if item == 5:
            total += 1

    if total >= 3:
        return 3

    else:
        return 0

# 빙고판 생성, 2차원 배열
Bingo_Board = [list(map(str, input().split())) for _ in range(5)]

# 사회자가 말할 보드 생성, 1차원 배열
speakers = []
for _ in range(5):
    speakers.extend(list(map(str, input().split())))

## while 안에서 flag 사용법 확인
## break는 for문 하나만 break하기때문에, break를 각 for문마다 넣어서 while문을 제어한다.
flag = False
cnt = 0
while flag == False:
    # 사회자가 말하는 만큼의 인덱스를 뽑아오고,
    for si in range(len(speakers)):
        if flag == True:
            break
        # 빙고 보드판을 돌 인덱스를 뽑아온다.
        for col in range(5):
            if flag == True:
                break
            for row in range(5):

                # cnt가 12가 될때부터 빙고가 될 가능성이 있기때문에, 그리고 cnt를
                # if문 안에서 하기 때문에 11 미만이거나,
                if cnt < 11:
                    if Bingo_Board[col][row] == speakers[si]:
                        Bingo_Board[col][row] = 'B'
                        cnt += 1
                # 11과 같거나 크면
                elif cnt >= 11:
                    if Bingo_Board[col][row] == speakers[si]:
                        Bingo_Board[col][row] = 'B'
                        cnt += 1
                        res = check(Bingo_Board) # 그때부터 빙고가 3개인지 아닌지 판단한다.

                        # 만약 res가 3으로 나온다면, 모든 for문을 break해서 빠져나온다.
                        if res == 3:
                            flag = True
                            break
print(si)

