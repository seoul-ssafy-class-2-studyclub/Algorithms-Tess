# import sys
# sys.stdin = open('17822.txt', 'r')
# import collections
#
#
# N, M, T = map(int, input().split())
# print(N, M, T)
# # N: y의 수
# # M: 원소의 수
# # T: 회전
#
# board = []
# for _ in range(N):
#     data = collections.deque(list(map(int, input().split())))
#     print(data)
#     board.append(data)
# xi, di, ki = map(int, input().split())
# print(xi, di, ki)
# # xi의 배수인 원판을 di방향으로 ki칸 회전
# # xi:
# # di: 회전방법(0 시계 방향, 1 반시계 방향)
# # ki:
#
# # 인접하면서 수가 같은 것을 모두 찾는다.
# # 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
# # 없는 경우에는
# # 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
# # 원판을 T번 회전시킨 후 원판에 적힌 수의 합을 구해보자.
#
# # 네방향이 인접하다.
# # 리스트의 양끝은 양끌과 인접하다.
# # 아래는 위와 인접하다.
#
# # 만약 j가 0이거나 -1인경우, 0이면 -1을 이웃하고, -1이면 0을 이웃한다.
#
#
# # 이만큼 돌린다.
#
# for _ in range(ki):
#     # xi에 해당하는 애들만
#     for par in range(0, N, xi):
#         # 0, 2 => 2의 배수
#         cnt = 0
#         if di == 0:
#         # 시계방향
#             while cnt != ki:
#                 temp = board[par].pop()
#                 board[par].appendleft(temp)
#                 cnt += 1
#         if di == 1:
#         # 반시계방향
#             while cnt != ki:
#                 temp = board[par].popleft()
#                 board[par].append(temp)
#                 cnt += 1
# print(board)
# def checkBFS():
#     global board
#     fordelete = [[False]*M for _ in range(N)]
#     for y in range(N):
#         for x in range(M):
#             for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
#                 iy = y + dy
#                 ix = x + dx
#                 if 0 <= iy < N and 0 <= ix < M:
#                     # print(ix, M)
#                     # x가 0일때, ix는 M-1이여야 한다.
#                     # print(board[1][3], board[0][3])
#                     if x != 0:
#                         if board[y][x] == board[iy][ix]:
#                             fordelete[y][x] = True
#                             fordelete[iy][ix] = True
#
#                     elif x == 0:
#                         ix = M-1
#                         if board[y][x] == board[iy][ix]:
#                             fordelete[y][x] = True
#                             fordelete[iy][ix] = True
#                     # x가 3일때, ix는 0이여야 한다.
#                     elif x == M-1:
#                         ix = 0
#                         if board[y][x] == board[iy][ix]:
#                             fordelete[y][x] = True
#                             fordelete[iy][ix] = True
#
#     # 각각의 y, x의 네방향이 가진 똑같은 숫자에 대한 check를 한다.
#     # check 후 같은 것들은 0으로 처리 한다.
#     res = 0
#     for y in range(N):
#         for x in range(M):
#             if fordelete[y][x] == False:
#                 res += board[y][x]
#     return res
#
# # 다 돌리고 삭제한다. (삭제할때 양옆 인덱스 확인 필요)
# result = checkBFS()
# print(result)

#
# import sys
# # sys.stdin = open('17822.txt', 'r')
# sys.setrecursionlimit(1000000000)
# import collections
#
#
# def checkBFS():
#     global board
#     tempcnt = 0
#     q = []
#     for y in range(1, N+1):
#         for x in range(M):
#             for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
#                 iy = y + dy
#                 ix = x + dx
#                 if 1 <= iy < N+1 and board[y][x] != 0:
#                     if ix == -1:
#                         ix = M-1
#                         if board[y][x] == board[iy][ix]:
#                             q.append((y, x))
#                             q.append((iy, ix))
#                             tempcnt = 1
#
#                     elif ix == M:
#                         ix = 0
#                         if board[y][x] == board[iy][ix]:
#                             q.append((y, x))
#                             q.append((iy, ix))
#                             tempcnt = 1
#
#                     elif board[y][x] == board[iy][ix]:
#                         q.append((y, x))
#                         q.append((iy, ix))
#                         tempcnt = 1
#     while q:
#         y, x = q.pop()
#         board[y][x] = 0
#
#     return tempcnt
#
# N, M, T = map(int, input().split())
# board = []
# temp = collections.deque([0]*M)
# board.append(temp)
#
# for _ in range(N):
#     data = collections.deque(list(map(int, input().split())))
#     board.append(data)
#
# for _ in range(T):
#     xi, di, ki = map(int, input().split())
#     for par in range(xi, N+1, xi):
#         cnt = 0
#         if di == 0:
#             while cnt != ki:
#                 temp = board[par].pop()
#                 board[par].appendleft(temp)
#                 cnt += 1
#
#         if di == 1:
#             while cnt != ki:
#                 temp = board[par].popleft()
#                 board[par].append(temp)
#                 cnt += 1
#     fin = checkBFS()
#     if fin == 0:
#         # 인접한게 없을때만 작동
#         res = 0
#         num = 0
#         for y in range(N+1):
#             for x in range(M):
#                 if board[y][x] != 0:
#                     res += board[y][x]
#                     num += 1
#         res = res/num
#         for y in range(N+1):
#             for x in range(M):
#                 # 순서가 존재하는 if로 해야한다.
#                 if float(board[y][x]) > res and board[y][x] != 0:
#                     # res가 더 작다.
#                     # 평균보다 큰 수이다.
#                     board[y][x] = board[y][x]-1
#                 elif float(board[y][x]) < res and board[y][x] != 0:
#                     board[y][x] = board[y][x]+1
#
# res = 0
# for y in range(1, N+1):
#     for x in range(M):
#         res += board[y][x]
# print(res)






'''
def checkBFS():
    global board
    tempcnt = 0
    for y in range(1, N+1):
        for x in range(M):
            if board[y][x]:
                number = board[y][x]
                queue = deque()
                queue.append((y, x))
                while queue:
                    r, c = queue.popleft()
                    for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                        iy = r + dy
                        ix = c + dx
                        if ix == -1:
                            ix = M - 1
                        elif ix == M:
                            ix = 0
                        if 1 <= iy < N+1 and board[iy][ix] == number:
                            board[y][x] = 0
                            board[iy][ix] = 0
                            queue.append((iy, ix))
                            tempcnt = 1
    return tempcnt

'''



import sys
# sys.stdin = open('17822.txt', 'r')
sys.setrecursionlimit(1000000000)
import collections


# def checkBFS():
#     global board
#     tempcnt = 0
#     for y in range(1, N+1):
#         for x in range(M):
#             if board[y][x]:
#                 number = board[y][x]
#                 queue = collections.deque([])
#                 queue.append((y, x))
#                 while queue:
#                     r, c = queue.popleft()
#                     for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
#                         iy = r + dy
#                         ix = c + dx
#                         if ix == -1:
#                             ix = M - 1
#                         elif ix == M:
#                             ix = 0
#                         if 1 <= iy < N+1 and board[iy][ix] == number:
#                             board[y][x] = 0
#                             board[iy][ix] = 0
#                             queue.append((iy, ix))
#                             tempcnt = 1
#     return tempcnt

def checkBFS():
    global board
    tempcnt = 0
    q = []
    for y in range(1, N+1):
        for x in range(M):
            for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                iy = y + dy
                ix = x + dx
                if 1 <= iy < N+1 and board[y][x] != 0:
                    if ix == -1: # ix가 -1인 경우,
                        ix = M-1
                        if board[y][x] == board[iy][ix]:
                            q.append((y, x))
                            q.append((iy, ix))
                            tempcnt = 1

                    elif ix == M: #ix가 M인 경우,
                        ix = 0
                        if board[y][x] == board[iy][ix]:
                            q.append((y, x))
                            q.append((iy, ix))
                            tempcnt = 1

                    # 모두 괜찮은 경우
                    elif board[y][x] == board[iy][ix]:
                        q.append((y, x))
                        q.append((iy, ix))
                        tempcnt = 1
    while q:
        y, x = q.pop()
        board[y][x] = 0

    return tempcnt

N, M, T = map(int, input().split())
board = []
temp = collections.deque([0]*M)
board.append(temp)

for _ in range(N):
    data = collections.deque(list(map(int, input().split())))
    board.append(data)

for _ in range(T):
    xi, di, ki = map(int, input().split())
    for par in range(xi, N+1, xi):
        cnt = 0
        if di == 0:
            while cnt != ki:
                temp = board[par].pop()
                board[par].appendleft(temp)
                cnt += 1

        if di == 1:
            while cnt != ki:
                temp = board[par].popleft()
                board[par].append(temp)
                cnt += 1
    fin = checkBFS()
    if fin == 0:
        # 인접한게 없을때만 작동
        res = 0
        num = 0
        for y in range(N+1):
            for x in range(M):
                if board[y][x] != 0:
                    res += board[y][x]
                    num += 1
        try:
            res = res/num
        except ZeroDivisionError:
            res = 0

        for y in range(N+1):
            for x in range(M):
                # 순서가 존재하는 if로 해야한다.
                if float(board[y][x]) > res and board[y][x] != 0:
                    # res가 더 작다.
                    # 평균보다 큰 수이다.
                    board[y][x] = board[y][x]-1
                elif float(board[y][x]) < res and board[y][x] != 0:
                    board[y][x] = board[y][x]+1

res = 0
for y in range(1, N+1):
    for x in range(M):
        res += board[y][x]
print(res)