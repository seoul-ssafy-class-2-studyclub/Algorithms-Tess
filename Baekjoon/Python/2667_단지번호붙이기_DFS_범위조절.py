
'''
3
7
8
9
'''

import sys
sys.stdin = open('2667.txt', 'r')


def change(iy, ix):
    cnt = 0
    stack = []
    stack.append((iy, ix)) # 처음 1을 만난 iy, ix 부터 시작하기 위해 스택에 넣는다.

    while len(stack) > 0: # stack의 길이가 []가 될때까지, 아래를 실행
        iy, ix = stack.pop()

        if board[iy][ix] != 0: # 문제해결: 1면 pop한 iy, ix는 버려진다. (중복이기때문에)
            board[iy][ix] = 0
            cnt += 1

            for idx in range(4):
                tempy = iy + dy[idx]
                tempx = ix + dx[idx]
                # 범위조절 주의! 0보다 '같거나 크면' 그리고 N 미만이면!
                if 0 <= tempy < N and 0 <= tempx < N:
                    # 범위안에 있는 사방의 좌표에 해당하는 보드의 숫자가 1이라면
                    # 스택에 넣는다.
                    if board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))
    return cnt

def check():
    cnt = 0
    for iy in range(N):
        for ix in range(N):
            if board[iy][ix] == 0:
                cnt += 1
                if cnt == (N*N):
                    return False
            else:
                return True

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
# all_direction = [[-1,0], [0,-1], [1,0], [0,1]]
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

houses = 0
flag = True
number_of_houses = []

for iy in range(N):
    for ix in range(N):
        if board[iy][ix] == 1:
            res = change(iy, ix)
            number_of_houses.append(res)
            houses += 1
            flag = check()

print(houses)
for res in sorted(number_of_houses):
    print(res)


'''
범위를 한 번에 조절가능
adj = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]] 
def checkIsland(i,j):                   # i,j에 대해 그 주변을 조사하여 같은 섬인 땅을 같은 숫자로 표시해주는 함수
    base_list[i][j] = -(cnt+1)
    for [dx,dy] in adj:
        if 0 <= i+dx < N and 0 <= j+dy < N and base_list[i+dx][j+dy] > 0:
            base_list[i+dx][j+dy] = -(cnt+1)
            checkIsland(i+dx, j+dy)

###########
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

board[y][x] = -1
queue = [x, y]
while queue:
    x = queue.pop(0)
    y = queue.pop(0)
    for idx in range(8):
        xi = x + dx[idx]
        yi = y + dy[idx]
        if 0 <= xi < N and 0 <= yi < N and board[yi][xi] >= 1:
            board[yi][xi] = -1
            queue.append(xi)
            queue.append(yi)
return 1

'''