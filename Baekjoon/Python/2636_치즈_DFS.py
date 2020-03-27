import sys
sys.stdin = open('2636.txt', 'r')


#1. 녹이기 전에 1이 칸에 몇개있는지 저장한다.
def howmanycheeses():
    cnt = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                cnt += 1
    return cnt

#1. 0, 0을 기준으로 움직이면서 상하좌우로 1을 만나면 3로 바꾼다. -> 1은 바꾸고 0은 stack에 넣는다.
def find(iy, ix):
    global board
    stack = []
    stack.append((iy, ix))
    visited = [[False]*M for _ in range(N)]
    while stack:
        iy, ix = stack.pop()
        visited[iy][ix] = True
        for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
            iiy = iy + dy
            iix = ix + dx
            if 0 <= iiy < N and 0 <= iix < M and visited[iiy][iix] == False:
                if board[iiy][iix] == 0:
                    stack.append((iiy, iix))
                elif board[iiy][iix] == 1:
                    board[iiy][iix] = 3
    return

# 2. 녹인다.
def melt(y, x):
    global board
    stack = []
    stack.append((y, x))
    visited2 = [[False]*M for _ in range(N)]
    while stack:
        iy, ix = stack.pop()
        visited2[iy][ix] = True

        for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
            iiy = iy + dy
            iix = ix + dx
            if 0 <= iiy < N and 0 <= iix < M and visited2[iiy][iix] == False:
                if board[iiy][iix] == 3:
                    board[iiy][iix] = 0

                elif board[iiy][iix] == 0:
                    stack.append((iiy, iix))
    return

#2. 치즈가 다 녹으면 멈추는 함수를 만든다.
def melt_chk():
    global board
    fin_cnt = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                fin_cnt += 1
                if fin_cnt == N*M:
                    return 1

    if fin_cnt < N*M:
        return 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

time = 0
numofcheese = []

fin = 0
while fin == 0:
    nums = howmanycheeses()
    numofcheese.append(nums)
    time += 1
    find(0, 0)
    melt(0, 0)
    fin = melt_chk()
    if fin == 1:
        break

print(time)
print(numofcheese[-1])
