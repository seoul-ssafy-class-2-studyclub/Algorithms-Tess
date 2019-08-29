
import sys
sys.stdin = open('2580.txt', 'r')



'''
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1
'''


essential = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 45

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]


# 하나가 미싱할때 체크하는 곳
for _ in range(9):

    #가로에서 확인
    stack = []
    x = 0
    for idx in range(9):
        cnt = 0
        temp = []
        for j in board[idx]:
            x += 1
            if j == 0:
                cnt += 1
                temp.extend(board[idx])

        if cnt == 1:
            if sum(board[idx]) != 45:
                x = board[idx].index(0)
                missing = 45 - sum(board[idx])
                stack.append((missing, idx, x))
                # [(1, 0, 0), (5, 3, 3), (7, 5, 5), (1, 8, 8)]
    if len(stack) > 0:
        for _ in range(len(stack)):
            missing, y, x = stack.pop()
            board[y][x] += missing

    # 추가하고, 그 보드에서 세로로 재시작
    # 세로
    col_board = []
    for iy in range(9):
        new_sdo = []
        for ix in range(9):
            new_sdo.append(board[ix][iy])
        col_board.append(new_sdo)

    x = 0
    for idx in range(9):
        cnt = 0
        temp = []
        for j in col_board[idx]:
            x += 1
            if j == 0:
                cnt += 1
                temp.extend(col_board[idx])

        if cnt == 1:
            if sum(col_board[idx]) != 45:
                x = col_board[idx].index(0)
                missing = 45 - sum(col_board[idx])
                stack.append((missing, x, idx))
                # [(4, 0, 2), (9, 2, 2), (3, 6, 6), (4, 8, 6)]
    if len(stack) > 0:
        for _ in range(len(stack)):
            missing, y, x = stack.pop()
            board[y][x] += missing

    # 재사용
    stack = []
    x = 0
    for idx in range(9):
        cnt = 0
        temp = []
        for j in board[idx]:
            x += 1
            if j == 0:
                cnt += 1
                temp.extend(board[idx])

        if cnt == 1:
            if sum(board[idx]) != 45:
                x = board[idx].index(0)
                missing = 45 - sum(board[idx])
                stack.append((missing, idx, x))
                # [(1, 0, 0), (5, 3, 3), (7, 5, 5), (1, 8, 8)]
    if len(stack) > 0:
        for _ in range(len(stack)):
            missing, y, x = stack.pop()
            board[y][x] += missing

    col_board = []
    for iy in range(9):
        new_sdo = []
        for ix in range(9):
            new_sdo.append(board[ix][iy])
        col_board.append(new_sdo)

    # 재사용
    x = 0
    for idx in range(9):
        cnt = 0
        temp = []
        for j in col_board[idx]:
            x += 1
            if j == 0:
                cnt += 1
                temp.extend(col_board[idx])

        if cnt == 1:
            if sum(col_board[idx]) != 45:
                x = col_board[idx].index(0)
                missing = 45 - sum(col_board[idx])
                stack.append((missing, x, idx))
                # [(4, 0, 2), (9, 2, 2), (3, 6, 6), (4, 8, 6)]
    if len(stack) > 0:
        for _ in range(len(stack)):
            missing, y, x = stack.pop()
            board[y][x] += missing


# 추가하고, 그 보드에서 3*3으로 재시작

queue = []
missing_list = []
for iy in range(0, 9, 3):
    for ix in range(0, 9, 3):
        total = 0
        for y in range(3):
            for x in range(3):
                total += board[iy + y][ix + x]
                if board[iy + y][ix + x] == 0:
                    queue.append((iy + y, ix + x))
        if total != 45:
            missing = 45 - total
            missing_list.append(missing)

if len(queue) > 0:
    for _ in range(len(queue)):
        y, x = queue.pop(0)
        board[y][x] += missing_list.pop(0)

### 모든 보드가 0으로만 이뤄져있을때 체크하는 곳

for line in board:
    print(' '.join(map(str,line)))


print('-----------')


counting = []
for i in range(1, 10):
    counting.append(i)

result = []

sdo = board

#가로
for i in sdo:
    if sum(i) != 45:
        result.append(0)
#세로
col_sdo = []
for iy in range(9):
    new_sdo = []
    for ix in range(9):
        new_sdo.append(sdo[ix][iy])
    col_sdo.append(new_sdo)

for i in col_sdo:
    if sum(i) != 45:
        result.append(0)

#3*3
for iy in range(0, 9, 3):
    for ix in range(0, 9, 3):
        total = 0
        for y in range(3):
            for x in range(3):
                total += sdo[iy+y][ix+x]

        if total != 45:
            result.append(0)
# 0이 들어있으면 틀린 것
print(result)
if len(result) != 0:
    print(0)
else:
    print(1)