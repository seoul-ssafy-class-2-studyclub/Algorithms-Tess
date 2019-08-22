import sys
sys.stdin = open('2636.txt', 'r')
from pprint import pprint
# 5


def start_board(arr):
    for x in range(B):
        arr[0][x] = 'A'
        arr[-1][x] = 'A'
    for y in range(A):
        arr[y][0] = 'A'
        arr[y][-1] = 'A'
    return arr

def check_final(arr):
    cnt = 0
    for iy in range(A):
        for ix in range(B):
            if arr[iy][ix] == 'A':
                cnt += 1
                if cnt == (A*B):
                    cnt = 1
    return cnt


up = [-1, 0]
down = [1, 0]
left = [0, -1]
right = [0, 1]


A, B = map(int, input().split())
# col = A, row = B

mat = [list(map(int, input().split())) for _ in range(A)]
board = start_board(mat)

res = 0
turns = []
leftover = []

while res == 0:
    for iy in range(A):
        for ix in range(B):

            # iy가 0, ix가 0~마지막이면, 아래만 확인
            if 0 <= ix <= B-1 and iy == 0:
                if board[iy][ix] == 'A':
                    for y, x in [down]:
                        if board[iy+y][ix+x] == 0:
                            board[iy+y][ix+x] = 'A'
                        if board[iy+y][ix+x] == 1:
                            board[iy + y][ix + x] = 'C'

            # ix가 0이고, iy가 0~마지막이면, 오른쪽만 확인
            if ix == 0 and 0 <= iy <= A-1:
                if board[iy][ix] == 'A':
                    for y, x in [right]:
                        if board[iy+y][ix+x] == 0:
                            board[iy+y][ix+x] = 'A'
                        if board[iy+y][ix+x] == 1:
                            board[iy + y][ix + x] = 'C'

            # iy가 마지막이고, ix가 0~마지막이면, 위만 확인
            if 0 <= ix < B-2 and iy == (A-1):
                if board[iy][ix] == 'A':
                    for y, x in [up]:
                        if board[iy + y][ix + x] == 0:
                            board[iy + y][ix + x] = 'A'
                        if board[iy + y][ix + x] == 1:
                            board[iy + y][ix + x] = 'C'

            # ix가 마지막이고, iy가 0~마지막이면, 왼쪽만 확인
            if ix == (B - 1) and 0 <= iy <= A-1:
                if board[iy][ix] == 'A':
                    for y, x in [left]:
                        if board[iy + y][ix + x] == 0:
                            board[iy + y][ix + x] = 'A'
                        if board[iy + y][ix + x] == 1:
                            board[iy + y][ix + x] = 'C'

            # ix가 0보다 크고, 마지막보다 작으며, iy가 0보다 크고, 마지막보다 작으면,
            if 0 < ix < B-1 and 0 < iy < A-1:
                if board[iy][ix] == 'A':
                    for y, x in [up, down, left, right]:
                        if board[iy + y][ix + x] == 0:
                            board[iy + y][ix + x] = 'A'
                        if board[iy + y][ix + x] == 1:
                            board[iy + y][ix + x] = 'C'

    for iy in range(A, -1, -1):
        for ix in range(B, -1, -1):
            if 0 < ix < B-1 and 0 < iy < A-1:

                # iy가 0, ix가 0~마지막이면, 아래만 확인
                if 0 <= ix <= B - 1 and iy == 0:
                    if board[iy][ix] == 'A':
                        for y, x in [down]:
                            if board[iy + y][ix + x] == 0:
                                board[iy + y][ix + x] = 'A'
                            if board[iy + y][ix + x] == 1:
                                board[iy + y][ix + x] = 'C'

                # ix가 0이고, iy가 0~마지막이면, 오른쪽만 확인
                if ix == 0 and 0 <= iy <= A - 1:
                    if board[iy][ix] == 'A':
                        for y, x in [right]:
                            if board[iy + y][ix + x] == 0:
                                board[iy + y][ix + x] = 'A'
                            if board[iy + y][ix + x] == 1:
                                board[iy + y][ix + x] = 'C'

                # iy가 마지막이고, ix가 0~마지막이면, 위만 확인
                if 0 <= ix < B - 2 and iy == (A - 1):
                    if board[iy][ix] == 'A':
                        for y, x in [up]:
                            if board[iy + y][ix + x] == 0:
                                board[iy + y][ix + x] = 'A'
                            if board[iy + y][ix + x] == 1:
                                board[iy + y][ix + x] = 'C'

                # ix가 마지막이고, iy가 0~마지막이면, 왼쪽만 확인
                if ix == (B - 1) and 0 <= iy <= A - 1:
                    if board[iy][ix] == 'A':
                        for y, x in [left]:
                            if board[iy + y][ix + x] == 0:
                                board[iy + y][ix + x] = 'A'
                            if board[iy + y][ix + x] == 1:
                                board[iy + y][ix + x] = 'C'

                # ix가 0보다 크고, 마지막보다 작으며, iy가 0보다 크고, 마지막보다 작으면,
                if 0 < ix < B - 1 and 0 < iy < A - 1:
                    if board[iy][ix] == 'A':
                        for y, x in [up, down, left, right]:
                            if board[iy + y][ix + x] == 0:
                                board[iy + y][ix + x] = 'A'
                            if board[iy + y][ix + x] == 1:
                                board[iy + y][ix + x] = 'C'

    hr = 0
    left_cheese = 0
    for iy in range(A):
        for ix in range(B):
            if board[iy][ix] == 'C':
                board[iy][ix] = 'A'
                left_cheese += 1
                hr = 1
    turns.append(hr)
    leftover.append(left_cheese)
    result = check_final(board)

    if result == 1:
        res = sum(turns)
    else:
        res = 0

print(res)
print(leftover[-1])











# start point를 잡아서
#check함수를 만드는데 2이상히면 가능해지는거..? 예외가 너무 많다.


# 나를 기준으로
# 내 위 아래든지, 양옆이든지, 1이면 내가 c가 될 수 있다.
# 그 기준을 반복하면서 1이있는 옆으로 타고타고

## 탐색하면서 c로 바꾸면서 가는게 제일 괜찮은거같은데..
#
# flag = True
# col_startpoint = None
# row_startpoint = None
# cnt = 0
# while flag == True:
#     for iy in range(A):
#         if col_startpoint != None:
#             flag = False
#             break
#         for ix in range(B):
#             if mat[iy][ix] == 1:
#                 flag = False
#                 col_startpoint = iy
#                 row_startpoint = ix
#                 break
# print(col_startpoint, row_startpoint)
# pprint(mat)
#
#
#
#
# #############
#
#
# def is_air():
#     for i in range(1, x-1):
#         for j in range(1, y-1):
#             if plate[i][j] == 0:
#                 if plate[i - 1][j] == 2:
#                     plate[i][j] = 2
#                     continue
#                 if plate[i][j - 1] == 2:
#                     plate[i][j] = 2
#                     continue
#                 if plate[i + 1][j] == 2:
#                     plate[i][j] = 2
#                     continue
#                 if plate[i][j + 1] == 2:
#                     plate[i][j] = 2
#                     continue
#             else:
#                 pass
#     for i in range(x-2, 0, -1):
#         for j in range(y-2, 0, -1):
#             if plate[i][j] == 0:
#                 if plate[i - 1][j] == 2:
#                     plate[i][j] = 2
#                     continue
#                 if plate[i][j - 1] == 2:
#                     plate[i][j] = 2
#                     continue
#                 if plate[i + 1][j] == 2:
#                     plate[i][j] = 2
#                     continue
#                 if plate[i][j + 1] == 2:
#                     plate[i][j] = 2
#                     continue
#             else:
#                 pass
#
#     # for i in range(1, y-1):
#     #     for j in range(1, x-1):
#     #         if plate[j][i] == 0:
#     #             if plate[j][i - 1] == 2:
#     #                 plate[j][i] = 2
#     #                 continue
#     #             if plate[j - 1][i] == 2:
#     #                 plate[j][i] = 2
#     #                 continue
#     #             if plate[j][i + 1] == 2:
#     #                 plate[j][i] = 2
#     #                 continue
#     #             if plate[j + 1][i] == 2:
#     #                 plate[j][i] = 2
#     #                 continue
#     #         else:
#     #             pass
#     #
#     # for i in range(y-2, 0, -1):
#     #     for j in range(x-2, 0, -1):
#     #         if plate[j][i] == 0:
#     #             if plate[j][i - 1] == 2:
#     #                 plate[j][i] = 2
#     #                 continue
#     #             if plate[j - 1][i] == 2:
#     #                 plate[j][i] = 2
#     #                 continue
#     #             if plate[j][i + 1] == 2:
#     #                 plate[j][i] = 2
#     #                 continue
#     #             if plate[j + 1][i] == 2:
#     #                 plate[j][i] = 2
#     #                 continue
#     #         else:
#     #             pass
#
#
# def air_cheese():
#     global count_cheese
#     for i in range(1, x-1):
#         for j in range(1, y-1):
#             if plate[i][j] == 1:
#                 if plate[i - 1][j] == 2:
#                     plate[i][j] = 3
#                     count_cheese -= 1
#                     continue
#                 if plate[i][j - 1] == 2:
#                     plate[i][j] = 3
#                     count_cheese -= 1
#                     continue
#                 if plate[i + 1][j] == 2:
#                     plate[i][j] = 3
#                     count_cheese -= 1
#                     continue
#                 if plate[i][j + 1] == 2:
#                     plate[i][j] = 3
#                     count_cheese -= 1
#                     continue
#             else:
#                 pass
#
#
# def melt_cheese():
#     for i in range(1, x-1):
#         for j in range(1, y-1):
#             if plate[i][j] == 3:
#                 plate[i][j] = 0
#
#
# x, y = map(int, input().split())
# count_cheese = 0
# plate = [list(map(int, input().split())) for _ in range(x)]
# for row in plate:
#     count_cheese += sum(row)
# for i in range(x):
#     plate[i][0] = 2
#     plate[i][y-1] = 2
# for j in range(y):
#     plate[0][j] = 2
#     plate[x-1][j] = 2
#
# step = 0
# last_count = 0
# while count_cheese > 0:
#     is_air()
#     step += 1
#     last_count = count_cheese
#     air_cheese()
#     if count_cheese == 0:
#         break
#     melt_cheese()
#
# print(step)
# print(last_count)
#
#
#
# ############
#
#
# # 0을 이어주는 함수
# def outline(board):
#     stack = [(0, 0)]
#     checked = []
#     zeros = []
#
#     while len(stack) != 0:
#         i, j = stack.pop()
#         print()
#         print(i, j)
#         zeros.append((i, j))
#
#         if i - 1 != -1 and (i - 1, j) not in checked:
#             checked.append((i - 1, j))
#             if board[i - 1][j] == 0:
#                 stack.append((i - 1, j))
#                 zeros.append((i - 1, j))
#         if i + 1 != row and (i + 1, j) not in checked:
#             checked.append((i + 1, j))
#             if board[i + 1][j] == 0:
#                 stack.append((i + 1, j))
#                 zeros.append((i + 1, j))
#         if j - 1 != -1 and (i, j - 1) not in checked:
#             checked.append((i, j - 1))
#             if board[i][j - 1] == 0:
#                 stack.append((i, j - 1))
#                 zeros.append((i, j - 1))
#         if j + 1 != col and (i, j + 1) not in checked:
#             checked.append((i, j + 1))
#             if board[i][j + 1] == 0:
#                 stack.append((i, j + 1))
#                 zeros.append((i, j + 1))
#     print(len(zeros))
#
#
# # arounds = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌 index
#
# row, col = map(int, input().split())
# board = [list(map(int, input().split())) for i in range(row)]
#
# outline(board)





