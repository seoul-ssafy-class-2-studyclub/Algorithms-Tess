import sys
sys.stdin = open('4615.txt', 'r')
from pprint import pprint

def start_color_decision():
    if color == 1:
        another = 2
    else:
        another = 1
    return color, another

def start_newboard():
    c = N // 2
    board = [[0] * N for _ in range(N)]
    board[c - 1][c - 1] = 2
    board[c][c] = 2
    board[c - 1][c] = 1
    board[c][c - 1] = 1
    return board

def result():
    black = 0
    white = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                black += 1
            elif board[y][x] == 2:
                white += 1
    return black, white

d = [(-1, 0),(-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1),(-1,-1)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = start_newboard()
    for _ in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        color, another = start_color_decision()
        board[y][x] = color
        for dy, dx in d:
            xi = x + dx
            yi = y + dy
            if 0 <= xi < N and 0 <= yi < N:
                cnt = 0
                while board[yi][xi] == another:
                    cnt += 1
                    xi += dx
                    yi += dy
                    if xi < 0 or yi < 0 or xi >= N or yi >= N or board[yi][xi] == 0:
                        break
                    elif board[yi][xi] == color:
                        xi = x + dx
                        yi = y + dy
                        while cnt != 0:
                            cnt -= 1
                            board[yi][xi] = color
                            xi += dx
                            yi += dy
    black, white = result()
    print(f'#{tc} {black} {white}')






#
# far_dy = [-2, -2, -2, 0, 2, 2, 2,  0]
# far_dx = [-2, 0,   2, 2, 2, 0, -2, -2]
#
# near_dy = [-1, -1, -1, 0, 1, 1, 1,  0]
# near_dx = [-1, 0,   1, 1, 1, 0, -1, -1]
#
#
# # def check(arr):
# #
# #     res = []
# #     for y in range(N):
# #         for x in range(N):
# #             if arr[y][x] != 0:
# #                 res.append(0)
# #     if len(res) == N*N:
# #         return 0
# # 빈 곳이 없는가?  위 함수는 빈곳 없을때 확인 가능
#
#
#
# # 양 플레이어 모두 놓을 곳이 없는가?
#
#
# def change(y, x):
#     global C
#     global C2
#     global board
#     print(y, x)
#     # queue = []
#     # queue2 = []
#     if board[y][x] == 0:
#         for idx in range(8):
#             tempx = x + near_dx[idx]
#             tempy = y + near_dy[idx]
#
#             tempx2 = x + far_dx[idx]
#             tempy2 = y + far_dy[idx]
#
#             #print(_, C, y, x)
#             if 0 <= tempx < N and 0 <= tempy < N and 0 <= tempx2 < N and 0 <= tempy2 < N:
#                 #print(C)
#                 # print(_, C, y, x)
#                 # pprint(board)
#                 if board[tempy][tempx] == C2 and board[tempy2][tempx2] == C:
#                     #print(_, C, y, x)
#                     #print('--',  board)
#                     board[y][x] = C
#                     board[tempy][tempx] = C
#                     #print('~~~', board)
#                     #print(_)
#
#
#                 elif board[tempy][tempx] == C2 and board[tempy2][tempx2] == C2:
#                     print(_, C, y, x)
#                     #print(x, y)
#                     #print(_)
#                     print('--',  board)
#                     pprint(board)
#                     board[y][x] = C2
#                     # board[tempy][tempx] = C2
#                     print('~~~', board)
#
#                 elif board[tempy][tempx] == C:
#                     board[y][x] = C
#
#
#                 elif board[tempy][tempx] == 0:
#                     board[y][x] = C
#                     # print(_, C, y, x)
#                     # queue.append((tempy, tempx))
#                     # queue2.append((tempy, tempx))
#
#
#
#
# # 사방을 검사해서 바꾼다.
# # 룰에 따르는 경우
# # 그것도 아니면 가까운 네 방향이 0인 경우
#
# ## 어차피 입력은 놓을 수 없는 곳을 주진 않으므로 상관 없음
# # 둘다아니면 상대편 플레이어가 다시 돌을 놓는다.
# # 즉, 상대편 플레이어가 돌을 놓아야 한다! 2이였을 경우 1의 턴이 되어야 한다.
#
# T = int(input())
# N, M = map(int, input().split())
# board = [[0]*N for _ in range(N)]
#
# board[N//2-1][N//2-1] = 'W'
# board[N//2-1][(N//2)] = 'B'
# board[(N//2)][(N//2)] = 'W'
# board[(N//2)][N//2-1] = 'B'
# pprint(board)
# res = 1
#
# # 4//2 -> 2
#
#
#
# for _ in range(1, M+1): # 12번 놓는다.
#     X, Y, C = map(int, input().split())
#     X = X-1
#     Y = Y-1
#     print(X, Y)
#     if C == 1:
#         C = 'B'
#         C2 = 'W'
#         # res = check(board)
#         change(Y, X)
#         if res == 0:
#             break
#
#     elif C == 2:
#         C = 'W'
#         C2 = 'B'
#         # res = check(board)
#         change(Y, X)
#         if res == 0:
#             break
#
# pprint(board)