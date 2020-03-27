import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
# sys.stdin = open('17070.txt', 'r')

'''
1
'''

def recursion(y, x, status):
    global path
    if y == G and x == G:
        path += 1
        return True
    # 0 가로 1 세로 2 대각선
    if status == 0:  # 가로로 놓여있을때 : 가로, 대각선 가능
        iy = 0 + y
        ix = 1 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0:
                status2 = 0
                recursion(iy, ix, status2)
        iy = 1 + y
        ix = 1 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0 and board[iy][ix-1] == 0 and board[iy-1][ix] == 0:
                status2 = 2
                recursion(iy, ix, status2)

    elif status == 1:  # 세로일때: 세로, 대각선 가능
        iy = 1 + y
        ix = 0 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0:
                status2 = 1
                recursion(iy, ix, status2)
        iy = 1 + y
        ix = 1 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0 and board[iy][ix-1] == 0 and board[iy-1][ix] == 0:
                status2 = 2
                recursion(iy, ix, status2)

    elif status == 2:  # 대각선일때, 가로, 세로 대각선 가능
        # for dy, dx in [(1, 1)]:
        iy = 1 + y
        ix = 1 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0 and board[iy][ix-1] == 0 and board[iy-1][ix] == 0:
                status2 = 2
                recursion(iy, ix, status2)
        # for dy, dx in [(0, 1)]:  # 가로로
        iy = 0 + y
        ix = 1 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0:
                status2 = 0
                recursion(iy, ix, status2)
        # for dy, dx in [(1, 0)]:  # 세로로
        iy = 1 + y
        ix = 0 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0:
                status2 = 1
                recursion(iy, ix, status2)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
G = N-1
path = 0
status = 0
recursion(0, 1, status)
print(path)


# G = N-1
# path = 0
# q = []
# q.append((0, 1))
# while q:

#     y, x = q.pop(0)

#     if y == G and x == G:
#         path += 1
    
#     for dy, dx in [(0,1), (1,0), (1,1)]:
#         iy = dy + y
#         ix = dx + x
#         if 0 <= iy < N and 0 <= ix < N and board[iy][ix] == 0:
#             q.append((iy, ix))
# print(path)
