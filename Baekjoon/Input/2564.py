'''

10 5
3
1 4
3 2
2 8
2 3


23
'''

import sys
sys.stdin = open('2564.txt', 'r')

X, Y = map(int, input().split()) # 10 5
board = [[0]*X for _ in range(Y)]
N_stores = int(input()) # 3

# 시작점이 1일때의 시계방향, 반시계방
first_rotation = [[0,1], [-1,0], [0,-1], [-1, 0]]
first_reverse_rotation = [[0, -1], [1,0], [0,1], [-1,0]]



# 만든 배열에 보드 색칠
# Store를 표시할 리스트
N_stores_list = [for _ in range(0, N_stores+1, 1)]


for _ in range(N_stores):
    D, P = map(int, input().split()) # Direction, Position
    mark = N_stores[_]
    if D == 1: # 위에서 내려간다
        # mark
        pass

    if D == 3:
        # mark
        pass

    if D == 2:
        # mark
        pass

    if D == 4: # 왼쪽에서 내려간다.
        # mark
        pass

# 'G' 로 표시
for _ in range(1):
    D, Goal = map(int, input().split())
    # 위와 동일
    if D == 1: # 위에서 내려간다
        # 'G'
        pass

    if D == 3:
        # 'G'
        pass

    if D == 2:
        # 'G'
        pass

    if D == 4: # 왼쪽에서 내려간다.
        # 'G'
        pass

for _ in range(N_stores*2):
    cnt = 0
    for iy in range(Y):
        for ix in range(X):
            cnt += 1
            # 시계방향, 반시계방향으로 나누기
            if board[iy][ix] == 'G':
                pass
            if board[iy][ix] == 'G':
                pass




