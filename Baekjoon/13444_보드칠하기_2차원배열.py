import sys
sys.stdin = open('13444.txt', 'r')
import copy
# 하 지우는 함수
def down(arr, iy, ix):
    for y in range(iy, N):
        if arr[y][ix] == '#':
            arr[y][ix] = 'B'
        if arr[y][ix] == '.':
            return

# 오른쪽 지우는 함수
def right(arr, iy, ix):
    for x in range(ix, M):
        if arr[iy][x] == '#':
            arr[iy][x] = 'B'
        if arr[iy][x] == '.':
            return

def colouring(y, x, arr):

    for idx in range(2):
        tempy = y + dy[idx]
        tempx = x + dx[idx]
        if 0 <= tempy < N and 0 <= tempx < M:
            if arr[tempy][tempx] == "#":
                right(arr, y, x)
                return
                # 하로 갈 애
            elif arr[tempy][tempx] == "#":
                down(arr, y, x)
                return

dy = [1, 0]
dx = [0, 1]
N, M = map(int, sys.stdin.readline().split())
board = [ list(sys.stdin.readline()) for _ in range(N)]
temp_board = copy.deepcopy(board)

compare_list = []

cnt = 0
for iy in range(N):
    for ix in range(M):
        if board[iy][ix] == '#':
            #시작점
            colouring(iy, ix, board)
            cnt += 1
compare_list.append(cnt)

second_board = [ list(temp_board[ix][iy]) for iy in range(N) for ix in range(M)]
for iy in range(M):
    for ix in range(N):
        if board[iy][ix] == '#':
            #시작점
            colouring(iy, ix, second_board)
            cnt += 1
compare_list.append(cnt)
print(min(compare_list))