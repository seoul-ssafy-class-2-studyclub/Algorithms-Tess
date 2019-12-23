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
print(board)

D = int(input()) # 계속가다가 맞춰서 방향 전환을 한다.
D_info = []
for _ in range(D):
    data = input().split()
    heapq.heappush(D_info,(int(data[0]), data[1]))
print(D_info)

direction = [(0,1), (1, 0), (-1,0), (0, -1)]
# nxt[(0,1)][0] -> (0,1)일때 L이 들어온 경
nxt = {(0,1): [2, 1], (1, 0):[0, 3], (-1,0): [3, 0], (0, -1):[1, 2]}

flag = True
i = 0
board[0][0] = 1

q = collections.deque([(0,0)]) # 앞이 빠져서 움직이는 것
current_dir = (0,1)
while flag:
    i += 1

    fin, nxt_dir = heapq.heappop(D_info) # D_info에 저장된 숫자를 만날때까지
    if i == fin:
        # 같으면, current_dir이 바뀐다
        if nxt_dir == 'L':
            current_dir = direction[nxt[current_dir][0]]
        if nxt_dir == 'D':
            current_dir = direction[nxt[current_dir][1]]

    else: # fin하고 i가 다르다면, 다시 넣어준다.
        heapq.heappush(D_info, (fin, nxt_dir))

    y, x = q.pop() # 새로운 애들은 뒤에 적재되니까.
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

        if board[iy][ix] == 1:
            # 자기 몸을 만나면 끝
            flag = False
            break

        if board[iy][ix] == 0:
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

    if len(q) == 0:
        print(len(q))
        flag = False

    print(i)





