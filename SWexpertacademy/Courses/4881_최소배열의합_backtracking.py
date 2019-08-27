import sys
sys.stdin = open('4881.txt', 'r')

# backtracking으로 푼다
# stack을 쓰고, if조건이 완료되면 끝낸다.

'''
#1 8
#2 14
#3 9
'''



def permutation(sums, length):
    global result

    if length == N:

        if sums < result:
            result = sums

        return True

    for nxt in range(N):
        if visited[nxt]:
            continue
        temp = board[length][nxt]
        if sums + temp >= result:
            continue
        visited[nxt] = True
        permutation(sums + temp, length + 1)
        visited[nxt] = False

for ro in range(int(input())):
    N = int(input())
    board = []
    per_list = []
    visited = [False for _ in range(N + 1)]
    result = 9*N
    for _ in range(N):
        board.append(list(map(int, input().split())))

    for i in range(N):
        visited[i] = True
        permutation(board[0][i], 1)
        visited[i] = False

    print('#%d %d' % (ro + 1, result))
#
# def colouring(y, x):
#
#     for iy in range(N):  # 0, 1, 2
#         for ix in range(N):  # 0, 1, 2
#             Non_visit[y][ix] = True
#             Non_visit[iy][x] = True
#     return y, x

# def backtracking(x):
#     # 첫줄에서의 start 포인트
#     stack = []
#     stack.append((0, x))
#
#     counting = []
#     while stack:
#         yi, xi = stack.pop()
#         counting.append(board[yi][xi])
#         if yi == 0:
#             for iy in range(N): # 0, 1, 2
#                 for ix in range(N): # 0, 1, 2
#                     Non_visit[yi][ix] = True
#                     Non_visit[iy][xi] = True
#                     stack.append((iy, xi))
#         elif yi != 0:
#             for ix in range(N): # 0, 1, 2
#                 if Non_visit[yi][xi+ix] == False:
#                     iy, ix = colouring(iy, xi+ix)
#                     stack.append((iy, ix))
#                 elif Non_visit[yi][xi+ix] == True:
#                     break
#         elif counting == N:
#             check_vis = sum(Non_visit, [])
#             if False not in check_vis:
#                 return sum(counting)
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     board = [list(map(int, input().split())) for _ in range(N)]
#     print(board)
#
#     # while문 안에서 visit를 만들고,
#     # sum한 cnt를 특정 리스트에 추가하고,
#     # 그 리스트에서 min의 최종을 산출한다.
#
#     cnt = 0
#     result_list = []
#
#     for idx in range(N):
#         Non_visit = [[False] * N for _ in range(N)]
#         res = backtracking(idx)
#         result_list.append(res)
#     print(result_list)


