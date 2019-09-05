import sys
sys.stdin = open('16234.txt', 'r')
from collections import deque

def search_companions(y, x):
    global fin
    q = deque()
    q.append((y, x))
    my_friends = deque()
    while q:
        y, x = q.popleft()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < N and visited[iy][ix] == False:
                if L <= abs(earth[y][x] - earth[iy][ix]) <= R:
                    visited[iy][ix] = True
                    q.append((iy, ix))
                    my_friends.append((iy, ix))
    my_temp_sum = 0
    ML = len(my_friends)
    if ML > 1:
        fin += 1
        for y, x in my_friends:
            my_temp_sum += earth[y][x]
        my_temp_res = my_temp_sum // ML
        for y, x in my_friends:
            earth[y][x] = my_temp_res

N, L, R = map(int, sys.stdin.readline().split())
earth = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = -1
Com = N*N
while 1:
    res += 1
    visited = [[0] * N for _ in range(N)]
    fin = 0
    for Y in range(N):
        for X in range(N):
            if earth[Y][X] != 0 and visited[Y][X] == 0:
                search_companions(Y, X)
    if fin == 0:
        break
print(res)


import time
st = time.time()
print(time.time() - st)
