import sys
sys.stdin = open('17070.txt', 'r')
input = sys.stdin.readline
import collections
'''
1
'''

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
G = N-1
path = 0
status = 0
stack = collections.deque([])
stack.append((0, 1, status))
while stack:
    y, x, status = stack.pop()
    if y == G and x == G:
        path += 1
    # 0 가로 1 세로 2 대각선
    if status == 0:  # 가로로 놓여있을때 : 가로, 대각선 가능
        iy = 0 + y
        ix = 1 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0:
                status2 = 0
                stack.append((iy, ix, status2))
        iy = 1 + y
        ix = 1 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0 and board[iy][ix-1] == 0 and board[iy-1][ix] == 0:
                status2 = 2
                stack.append((iy, ix, status2))
    elif status == 1:  # 세로일때: 세로, 대각선 가능
        iy = 1 + y
        ix = 0 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0:
                status2 = 1
                stack.append((iy, ix, status2))
        iy = 1 + y
        ix = 1 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0 and board[iy][ix-1] == 0 and board[iy-1][ix] == 0:
                status2 = 2
                stack.append((iy, ix, status2))

    elif status == 2:  # 대각선일때, 가로, 세로 대각선 가능
        # for dy, dx in [(1, 1)]:
        iy = 1 + y
        ix = 1 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0 and board[iy][ix-1] == 0 and board[iy-1][ix] == 0:
                status2 = 2
                stack.append((iy, ix, status2))
        iy = 0 + y
        ix = 1 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0:
                status2 = 0
                stack.append((iy, ix, status2))
        iy = 1 + y
        ix = 0 + x
        if 0 <= iy < N and 0 <= ix < N:
            if board[iy][ix] == 0:
                status2 = 1
                stack.append((iy, ix, status2))
print(path)
