## 백트래킹 : 주어진 문제의 답을 구하기 위해 현재 상태에서 가능한 모든 후보군에 따라 들어가며 탐색하는 알고리
# 1. 시작점의 좌표를 구한다.
# 2. 해당 좌표에 후보 번호(1-9)들을 넣어본다. 이때 행과 열을 보면서 가능한지 False or True
# 3. 후보 번호들을 넣으면서 맞는 번호가 있으면 temperately fix 한다.
# 4. 반복하다가
'''
# 5. [Backtracking] False가 나오는 경우가 있으면 Backtracking을 시작한다.
현재위치에서 이전에 했던 것을 지우고 
이전 위치에서 넣었던 번호를 제외하고 가능한 번호를 넣는다. 
만약 그것도 잘 되지 않는다면,
그 이전 위치에서 더 이전 위치에서 해당 검사를 반복한다.
'''


sys.stdin = open('2580.txt', 'r')


import sys
sys.setrecursionlimit(10000000)

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# main, inside of itself

def solve(bo):
    find = find_empty(bo)  # 시작점에서 가능한 곳인지 확인

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if vaild(bo, i, (row, col)):
            bo[row][col] = i  # 만약 valid하다고 판단되었다면, 위와 같이 보드에 추가해준다.

            if solve(bo):
                return True

            bo[row][col] = 0
    # valid하다고 판단되지 않은 경우 False를 반환
    return False


def vaild(bo, num, pos):

    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check 3*3 cube
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_x*3+3):
        for j in range(box_x * 3, box_y * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True # everythings fine


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col
    return None

# print_board(board)
res = solve(board)
# print(res)
while res == True:
    board = [i[:] for i in board]
    for line in board:
        print(' '.join(list(map(str, line))))
    break

# def print_board(bo):
#     for i in range(len(bo)):
#         if i % 3 == 0 and i != 0:
#             print(" - - - - - - - - ")
#         for j in range(len(bo[0])):
#             if j % 3 == 0 and j != 0:
#                 print(" | ", end="")
#             if j == 8:
#                 print(bo[i][j])
#             else:
#                 print(str(bo[i][j]) + " ", end="")
#
# essential = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# total = 45
#
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
#
#
# # 하나가 미싱할때 체크하는 곳
# for _ in range(9):
#
#     #가로에서 확인
#     stack = []
#     x = 0
#     for idx in range(9):
#         cnt = 0
#         temp = []
#         for j in board[idx]:
#             x += 1
#             if j == 0:
#                 cnt += 1
#                 temp.extend(board[idx])
#
#         if cnt == 1:
#             if sum(board[idx]) != 45:
#                 x = board[idx].index(0)
#                 missing = 45 - sum(board[idx])
#                 stack.append((missing, idx, x))
#                 # [(1, 0, 0), (5, 3, 3), (7, 5, 5), (1, 8, 8)]
#     if len(stack) > 0:
#         for _ in range(len(stack)):
#             missing, y, x = stack.pop()
#             board[y][x] += missing
#
#     # 추가하고, 그 보드에서 세로로 재시작
#     # 세로
#     col_board = []
#     for iy in range(9):
#         new_sdo = []
#         for ix in range(9):
#             new_sdo.append(board[ix][iy])
#         col_board.append(new_sdo)
#
#     x = 0
#     for idx in range(9):
#         cnt = 0
#         temp = []
#         for j in col_board[idx]:
#             x += 1
#             if j == 0:
#                 cnt += 1
#                 temp.extend(col_board[idx])
#
#         if cnt == 1:
#             if sum(col_board[idx]) != 45:
#                 x = col_board[idx].index(0)
#                 missing = 45 - sum(col_board[idx])
#                 stack.append((missing, x, idx))
#                 # [(4, 0, 2), (9, 2, 2), (3, 6, 6), (4, 8, 6)]
#     if len(stack) > 0:
#         for _ in range(len(stack)):
#             missing, y, x = stack.pop()
#             board[y][x] += missing
#
#     # 재사용
#     stack = []
#     x = 0
#     for idx in range(9):
#         cnt = 0
#         temp = []
#         for j in board[idx]:
#             x += 1
#             if j == 0:
#                 cnt += 1
#                 temp.extend(board[idx])
#
#         if cnt == 1:
#             if sum(board[idx]) != 45:
#                 x = board[idx].index(0)
#                 missing = 45 - sum(board[idx])
#                 stack.append((missing, idx, x))
#                 # [(1, 0, 0), (5, 3, 3), (7, 5, 5), (1, 8, 8)]
#     if len(stack) > 0:
#         for _ in range(len(stack)):
#             missing, y, x = stack.pop()
#             board[y][x] += missing
#
#     col_board = []
#     for iy in range(9):
#         new_sdo = []
#         for ix in range(9):
#             new_sdo.append(board[ix][iy])
#         col_board.append(new_sdo)
#
#     # 재사용
#     x = 0
#     for idx in range(9):
#         cnt = 0
#         temp = []
#         for j in col_board[idx]:
#             x += 1
#             if j == 0:
#                 cnt += 1
#                 temp.extend(col_board[idx])
#
#         if cnt == 1:
#             if sum(col_board[idx]) != 45:
#                 x = col_board[idx].index(0)
#                 missing = 45 - sum(col_board[idx])
#                 stack.append((missing, x, idx))
#                 # [(4, 0, 2), (9, 2, 2), (3, 6, 6), (4, 8, 6)]
#     if len(stack) > 0:
#         for _ in range(len(stack)):
#             missing, y, x = stack.pop()
#             board[y][x] += missing
#
#
# # 추가하고, 그 보드에서 3*3으로 재시작
#
# queue = []
# missing_list = []
# for iy in range(0, 9, 3):
#     for ix in range(0, 9, 3):
#         total = 0
#         for y in range(3):
#             for x in range(3):
#                 total += board[iy + y][ix + x]
#                 if board[iy + y][ix + x] == 0:
#                     queue.append((iy + y, ix + x))
#         if total != 45:
#             missing = 45 - total
#             missing_list.append(missing)
#
# if len(queue) > 0:
#     for _ in range(len(queue)):
#         y, x = queue.pop(0)
#         board[y][x] += missing_list.pop(0)
#
# ### 모든 보드가 0으로만 이뤄져있을때 체크하는 곳
#
# for line in board:
#     print(' '.join(map(str,line)))
#
#
# print('-----------')
#
#
# counting = []
# for i in range(1, 10):
#     counting.append(i)
#
# result = []
#
# sdo = board
#
# #가로
# for i in sdo:
#     if sum(i) != 45:
#         result.append(0)
# #세로
# col_sdo = []
# for iy in range(9):
#     new_sdo = []
#     for ix in range(9):
#         new_sdo.append(sdo[ix][iy])
#     col_sdo.append(new_sdo)
#
# for i in col_sdo:
#     if sum(i) != 45:
#         result.append(0)
#
# #3*3
# for iy in range(0, 9, 3):
#     for ix in range(0, 9, 3):
#         total = 0
#         for y in range(3):
#             for x in range(3):
#                 total += sdo[iy+y][ix+x]
#
#         if total != 45:
#             result.append(0)
# # 0이 들어있으면 틀린 것
# print(result)
# if len(result) != 0:
#     print(0)
# else:
#     print(1)