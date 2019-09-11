import sys
sys.stdin = open('2573.txt', 'r')



# 1. 붙어있는 0만큼 -1 된다.
# 1. 빙산이 두 덩어리 이상으로 분리되 결과값을 출력한다.















# import copy
#
# # 16
#
# def change(x, y):
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#
#     queue = [x, y]
#     vis[y][x] = True
#
#     while queue:
#         x = queue.pop(0)
#         y = queue.pop(0)
#         for i in range(4):
#             xi = x + dx[i]
#             yi = y + dy[i]
#             if 0 <= xi < M and 0 <= yi < N and not vis[yi][xi]: # 범위지정과 비지트
#                 if board[yi][xi] == 0 and board[y][x] > 0:
#                     board[y][x] -= 1
#                 elif board[yi][xi] >= 1:
#                     vis[yi][xi] = True
#                     queue.append(xi)
#                     queue.append(yi)
#     return 1
#
# # board를 아예 슬라이싱으로 따로 복사해본후
# # 0보다 큰수의 덩어리를 아예 0으로 만들어서 없애면서
# #체크
# def check_in(iy, ix):
#
#     #board를 new_board로 만들어서 체크
#     visit_board = copy.deepcopy(board)
#     stack = []
#     stack.append((iy, ix))
#     while len(stack) > 0: # stack의 길이가 []가 될때까지, 아래를 실행
#         iy, ix = stack.pop()
#
#         if visit_board[iy][ix] != 0:  # 문제해결: 1면 pop한 iy, ix는 버려진다. (중복이기때문에)
#             visit_board[iy][ix] = 0
#             for dy, dx in directions:
#                 tempy, tempx = iy + dy, ix + dx
#                 if 0 <= tempy < N and 0 <= tempx < M:
#                     if visit_board[tempy][tempx] == 0:
#                         stack.append((tempy, tempx))
#     return 1
#
#
# def check(arr):
#
#     flag2 = True
#     cnt = 0
#
#     while flag2 == True:
#
#         for iy in range(N):
#             if iy == (N - 1) and ix == (M - 1):
#                 flag2 = False
#                 break
#
#             for ix in range(M):
#                 if arr[iy][ix] > 0:
#                     cnt += check_in(iy, ix)
#                     if iy == (N-1) and ix == (M-1):
#                         flag2 = False
#                         break
#     return cnt
#
#
#
# # 행, 열
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
#
# directions = [[0,-1],[-1,0],[1,0],[0,1]]
#
# flag = True
# year = 0
#
# while flag == True:
#     vis = [[False] * M for i in range(N)]
#     is_fin = True
#     for iy in range(N):
#         if flag == False:
#             break
#
#         for ix in range(M):
#             # 0보다 큰 양수를 기준으로 좌표를 넣는다.
#             if board[iy][ix] > 0 and not vis[iy][ix]:
#                 is_fin = False
#                 year += change(iy, ix)
#                 #한 번 보드를 싹 돌면서 바꿔줄 함수
#                 year += 1 # change함수가 시작되면 year이 늘어난다.
#
#
#     print(year)
#     if is_fin:
#         year = 0
#         break





