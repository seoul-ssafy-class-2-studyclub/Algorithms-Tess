import sys
sys.stdin = open('6109.txt', 'r')
from pprint import pprint


######### queue를 사용

from collections import deque

def move_v(c):
    for i in range(N): #
        queue = deque()
        #print(queue) # deque([])

        for j in range(N):
            if board[j][i]: # 만약 board[j][i] 이 True라면, 즉, 0이 아니라면
                #print(board[j][i])
                queue.append(board[j][i])
                board[j][i] = 0
        # 큐에 원래 들어가있는 숫자를 넣고, 그 해당하는 열의 숫자를 0으로 초기화
        # 한 열이 0으로 되는게 끝나면,
        '''
        [[0, 8, 2, 4, 0],
         [0, 4, 2, 0, 8],
         [0, 0, 2, 4, 4],
         [0, 2, 2, 2, 8],
         [0, 2, 2, 0, 0]]
        '''
        #pprint(board)

        # 한 열을 다 비우고 규칙에 따라 구성

        if c == 'up': # 상인 경우
            idx = 0 # y를 0으로 두고,
            while queue:
                nxt = queue.popleft() # queue에서 좌측부터 pop하면서,
                print(nxt)
                if board[idx][i] == 0: # 0 0 이 0인 경우
                    board[idx][i] = nxt # 0을 nxt로 추가한다.
                elif board[idx][i] == nxt: # 0 0 이 추가되었던 nxt인경우,
                    board[idx][i] += nxt # 0 0 에 nxt를 추가 한다.
                    idx += 1 # 그리고 idx를 늘린다.
                else:
                    idx += 1 # 두 경우 모두 아닌경우, 즉 0이나 nxt가 아닌 다른 번호인 경우
                    board[idx][i] = nxt # 그다음 idx에 nxt를 추가한다.
        else: # 하인 경우
            idx = N - 1 # 마지막 인덱스부터 시작해서 같은 규칙을 진행하고, 하나씩 빼서 idx는 0까지 가까워진다.
            while queue:
                nxt = queue.pop()
                if board[idx][i] == 0:
                    board[idx][i] = nxt
                elif board[idx][i] == nxt:
                    board[idx][i] += nxt
                    idx -= 1
                else:
                    idx -= 1
                    board[idx][i] = nxt


def move_h(c):
    for j in range(N):
        queue = deque()
        for i in range(N):
            if board[j][i]:
                queue.append(board[j][i])
                board[j][i] = 0
        if c == 'left':
            idx = 0
            while queue:
                nxt = queue.popleft()
                if board[j][idx] == 0:
                    board[j][idx] = nxt
                elif board[j][idx] == nxt:
                    board[j][idx] += nxt
                    idx += 1
                else:
                    idx += 1
                    board[j][idx] = nxt
        else:
            idx = N - 1
            while queue:
                nxt = queue.pop()
                if board[j][idx] == 0:
                    board[j][idx] = nxt
                elif board[j][idx] == nxt:
                    board[j][idx] += nxt
                    idx -= 1
                else:
                    idx -= 1
                    board[j][idx] = nxt


for case in range(1, int(input()) + 1):
    N, C = input().split()
    N = int(N) # 5 라면,
    board = [list(map(int, input().split())) for _ in range(N)]
    if C == 'up' or C == 'down': # 상이거나 하면,
        move_v(C)
    else: # 좌나 우면,
        move_h(C)
    print('#{0}'.format(case))
    for i in range(N):
        print(' '.join(map(str, board[i])))




##########
#
# def daching(board_180):
#     board_180.reverse()
#     for i in range(N):
#         board_180[i].reverse()
#     return board_180
#
#
# def re90(board_90):
#     board_90 = list(map(list, zip(*board_90)))
#     for idx in range(len(board_90)):
#         board_90[idx].reverse()
#     return board_90
#
#
# def re270(board_270):
#     board_270 = re90(board_270)
#     board_270 = daching(board_270)
#     return board_270
#
#
# def no(board):
#     return board
#
#
# directions = {'up': [no, no], 'left': [re90, re270], 'right': [re270, re90], 'down': [daching, daching]}
#
#
# def play(di):
#     global board
#
#     board = directions[di][0](board)
#
#     for y in range(1, N):
#         for x in range(N):
#             if board[y][x]:
#                 dy = -1
#                 while 0 < y + dy < N and not board[y + dy][x]:
#                     dy -= 1
#                 if board[y + dy][x] == board[y][x] and not visited[y + dy][x]:
#                     temp = board[y][x]
#                     board[y][x] = 0
#                     board[y + dy][x] += temp
#                     visited[y + dy][x] = True
#
#                 elif board[y + dy][x] == 0:
#                     temp = board[y][x]
#                     board[y][x] = 0
#                     board[y + dy][x] += temp
#
#                 else:
#                     temp = board[y][x]
#                     board[y][x] = 0
#                     board[y + dy + 1][x] += temp
#
#     board = directions[di][1](board)
#
#     return board
#
#
# for ro in range(int(input())):
#     N, di = input().split()
#     N = int(N)
#     board = []
#     visited = [[False] * N for _ in range(N)]
#     for _ in range(N):
#         board.append(list(map(int, input().split())))
#
#     print('#%d' % (ro + 1))
#
#     board = play(di)
#     for line in board:
#         for val in line:
#             print(val, end=' ')
#         print()

#
# T = int(input())
# for tc in range(1, T+1):
#     N, D = map(str, input().split()) # N 행, 열 D 방
#     N = int(N)
#     temp_board = [list(map(int, input().split())) for _ in range(N)]
#     print(N, D)
#
#     if D == 'up':
#         my_board = []
#         for y in range(N):
#             row_board = []
#             for x in range(N):
#                 row_board.append(temp_board[x][y])
#             my_board.append(row_board)
#
#         pprint(my_board)
#
#         compa_board = [[] for _ in range(N)]
#         for y in range(N):
#             for x in range(N):
#                 if my_board[y][x] != 0:
#                     compa_board[y].append(my_board[y][x])
#         pprint(compa_board)
#         print('???', compa_board[2][4])
#
#         temp2_board = [[] for _ in range(N)]
#         dy = 0
#         dx = 1
#         startx = 0
#         confirm = []
#         stack = []
#         stack.append((0, 0))
#
#         while stack:
#             y, x = stack.pop()
#             iy = y + dy
#             ix = x + dx
#             print(iy, ix)
#             print('??', y, x, compa_board[y])
#             if 0 <= ix < N and 0 <= iy < N and compa_board[y][x] == compa_board[iy][ix]:
#                 print(y, x)
#
#                 temp2_board[y].append(compa_board[y][x]*2)
#                 ix = ix+1
#                 stack.append((iy, ix))
#
#             elif 0 <= ix < N and 0 <= iy < N and compa_board[y][x] != compa_board[iy][ix]:
#
#                 temp2_board[y].append(compa_board[y][x])
#                 temp2_board[y].append(compa_board[iy][ix])
#                 ix = ix + 1
#                 stack.append((iy, ix))
#
#
#             elif len(compa_board[y]) < ix and 0 <= iy < N: # 5 < 4
#                 iy = iy + 1
#                 ix = startx
#                 stack.append((iy, ix))
#         pprint(temp2_board)

#
# d = [(1, 0)]
# T = int(input())
# for tc in range(1, T+1):
#     N, D = map(str, input().split()) # N 행, 열 D 방
#     N = int(N)
#     temp_board = [list(map(int, input().split())) for _ in range(N)]
#     new_board = [[0]*N for _ in range(N)]
#
#     stack = []
#     starty, startx = 0, 0
#     temp = temp_board[startx][starty]
#     stack.append((starty, startx, temp))
#
#     while stack:
#         y, x, temp = stack.pop()
#         for dy, dx in d:
#             iy = y + dy
#             ix = x + dx
#             if 0 <= iy < N and 0 <= ix < N:
#                 if temp != 0 and temp_board[ix][iy] == temp:
#                     new_board[x][y] = temp*2
#                     temp = 0
#                     iy = iy + 1
#                     stack.append((iy, ix, temp))
#
#                 elif temp != 0 and temp_board[ix][iy] != temp:
#                     new_board[x][y] = temp
#                     temp = temp_board[ix][iy]
#                     stack.append((iy, ix, temp))
#
#                 elif temp == 0 and temp_board[ix][iy] == 0:
#                     temp = temp_board[ix][iy]
#                     stack.append((iy, ix, temp))
#
#                 elif temp == 0 and temp_board[ix][iy] != 0:
#                     temp = temp_board[x][y]
#                     stack.append((iy, ix, temp))
#             # if N <= iy:
#             #     ix = startx + 1
#             #     iy = starty
#             #     temp = temp_board[ix][iy]
#             #     stack.append((iy, ix, temp))
#     print(temp_board)
#     print(new_board)
#
#





