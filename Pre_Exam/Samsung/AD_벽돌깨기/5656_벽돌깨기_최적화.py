import sys
sys.stdin = open('5656.txt', 'r')
from pprint import pprint

import collections

def solve(t):
    global mymin, origin
    arr = [i[:] for i in origin]
    tt = t[:]
    while tt:
        idx = tt.pop()
        vis = [[False]*W for _ in range(H)]
        q = collections.deque([])
        for y in range(H):
            if arr[y][idx] != 0:
                q.append((y, idx))
                vis[y][idx] = True
                break
        while q:
            y, x = q.popleft()
            if arr[y][x] == 1:
                arr[y][x] = 0
                continue
            else:
                for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ory = y
                    orx = x
                    for i in range(0, arr[y][x] - 1):
                        iy = ory + dy
                        ix = orx + dx
                        if 0 <= iy < H and 0 <= ix < W and vis[iy][ix] == False and arr[iy][ix] != 0:
                            vis[iy][ix] = True
                            q.append((iy, ix))
                        ory = iy
                        orx = ix
        cnt = 0
        for x in range(W - 1, -1, -1):
            stack = collections.deque([])
            for y in range(H - 1, -1, -1):
                if vis[y][x] == True:
                    arr[y][x] = 0
                elif arr[y][x] != 0:
                    stack.append(arr[y][x])
                    arr[y][x] = 0
            cnt += len(stack)
            for y in range(H - 1, -1, -1):
                if len(stack) != 0:
                    data = stack.popleft()
                    arr[y][x] = data
    if cnt < mymin:
        mymin = cnt
    return mymin

def permut(k):
    global candis
    if k == N:
        # 복사가 아니라 참조인 상태로 append되기때문에 항상 현상태를 복사해서 append해줘야한다.
        candis.append(t[:])
        return
    else:
        for i in range(0, W):
            t[k] = wIndexes[i]
            permut(k+1)

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    origin = [list(map(int, input().split())) for _ in range(H)]
    mymin = 1e9
    candis = []
    wIndexes = [i for i in range(W)]
    t = [0]*N
    permut(0)
    for t in candis:
        ans = solve(t)
        if ans == 0:
            break
    print(f'#{tc} {mymin}')


'''
from collections import deque
 
delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def demolish(board, y, x, brick):
    q = deque()
    q.append((y, x, brick))
    board[y][x] = 0
    while q:
        y, x, size = q.popleft()
        for i in range(size):
            for a, b in delta:
                xi = x + (a * i)
                yi = y + (b * i)
                if 0 <= xi < W and 0 <= yi < H:
                    bomb = board[yi][xi]
                    if bomb:
                        if bomb > 1:
                            q.append((yi, xi, bomb))
                        board[yi][xi] = 0
 
 
def fall(board, w, h):
    cnt = 0
    for c in range(w):
        stack = deque()
        for r in range(h):
            brick = board[r][c]
            if brick:
                stack.append(brick)
                cnt += 1
        idx = h - 1
        while stack:
            board[idx][c] = stack.pop()
            idx -= 1
        while idx >= 0:
            board[idx][c] = 0
            idx -= 1
    return cnt
 
 
def cycle(board, k=0, cnt=0):
    global min_cnt
    if k == N:
        if min_cnt > cnt:
            min_cnt = cnt
        return True
     
    flag = True
    for i in range(W):
        is_clear = True
        for j in range(H):
            if board[j][i]:
                is_clear = False
                temp = [row[:] for row in board]
                demolish(temp, j, i, temp[j][i])
                break
        if is_clear:
            continue
        flag = False
        cnt = fall(temp, W, H)
        cycle(temp, k+1, cnt)
     
    if flag:
        min_cnt = 0
        return True
 
 
for case in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    game = [list(map(int, input().split())) for _ in range(H)]
    min_cnt = 999999
    cycle(game)
    print('#{0} {1}'.format(case, min_cnt))
'''