'''
9
'''

import sys
sys.stdin = open('3190.txt', 'r')

import heapq
import collections

N = int(input())
board = [[0]*(N) for _ in range(N)]
K = int(input())
for i in range(1, K+1):
    Y, X = map(int, input().split())
    board[Y-1][X-1] = 2 # -1씩 해줘야 한다.

D = int(input()) # 계속가다가 맞춰서 방향 전환을 한다.
D_info = dict()
for _ in range(D):
    data = input().split()
    D_info[int(data[0])] = data[1]
direction = [(0,1), (1, 0), (-1,0), (0, -1)]
# nxt[(0,1)][0] -> (0,1)일때 L이 들어온 경
# 문제가 있는듯, 잘 움직이긴하는데..
nxt = {(0,1): [2, 1], (1, 0):[0, 3], (-1,0): [3, 0], (0, -1):[1, 2]}


flag = True
i = 0
board[0][0] = 1

q = collections.deque([(0,0)]) # 앞이 빠져서 움직이는 것
current_dir = (0,1)
while flag:

    i += 1

    y, x = q.popleft() # 새로운 애들은 뒤에 적재되니까.

    dy, dx = current_dir
    iy, ix = dy+y, dx+x
    if 0 <= iy < N and 0 <= ix < N:

        if board[iy][ix] == 2:
            # 만약 이동한 칸에 사과가 있다면,
            # 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
            # -> 사과가 없어진곳을 1로 만들고 q 에 넣어준다.
            board[iy][ix] = 1
            q.appendleft((iy, ix))
            continue

        elif board[iy][ix] == 1 or (iy, ix) in q:
            # 자기 몸을 만나면 끝
            flag = False
            break

        elif board[iy][ix] == 0:
            # 만약 이동한 칸에 사과가 없다면,
            # 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
            # 만약 몸이 긴 상태였다면, 앞에서 움직인것 말고 맨 뒤에있는 애가 사라지고,
            # 앞에 움직인애 즉 새로운 애는 넣어져야 할텐데
            board[iy][ix] = 1
            q.appendleft((y, x))
            q.appendleft((iy, ix))
            ny, nx = q.pop() # 꼬리는 뒤에있으니까.
            board[ny][nx] = 0

    else: # 벽이라면, 끝
        flag = False
        break

    if i in D_info: # i가 있다면, 빼준다. # 밑으로 옮기니까 답이 나왔다.
        nxt_dir = D_info[i] # D_info에 저장된 숫자를 만날때까지
        # 같으면, current_dir이 바뀐다
        if nxt_dir == 'L':
            current_dir = direction[nxt[current_dir][0]]
        if nxt_dir == 'D':
            current_dir = direction[nxt[current_dir][1]]
print(i)


'''
from collections import deque
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
L, D = (3, 2, 0, 1), (2, 3, 1, 0)

def solve():
    x, y, z, d, ans = 0, 0, 0, 0, 0
    a[0][0] = 2
    q = deque()
    q.append((0, 0))
    while True:
        x, y = x+dx[d], y+dy[d]
        ans += 1
        if x < 0 or x >= n or y < 0 or y >= n or a[x][y] == 2:
            print(ans)
            return
        if not a[x][y]:
            nx, ny = q.popleft()
            a[nx][ny] = 0
        a[x][y] = 2
        q.append((x, y))
        t, c = b[z]
        if ans == int(t):
            if c == 'L':
                d = L[d]
            else:
                d = D[d]
            z = (z+1)%m

n = int(input())
a = [[0]*n for _ in range(n)]
for _ in range(int(input())):
    u, v = map(int, input().split())
    a[u-1][v-1] = 1
m = int(input())
b = [list(map(str, input().split())) for _ in range(m)]
solve()
'''
