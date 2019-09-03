from itertools import combinations

def building_wall(candids, arr):
    for candid in candids:
        y, x = candid
        arr[y][x] = 1
    return arr

def start_virus(arr):
    stack = []
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 2:
                stack.append((y, x))
    while stack:
        iy, ix = stack.pop()
        if arr[iy][ix] == 0:
            arr[iy][ix] = 2

        for dy, dx in d:
            iiy = iy + dy
            iix = ix + dx

            if 0 <= iiy < N and 0 <= iix < M:
                if arr[iiy][iix] == 0:
                    stack.append((iiy, iix))
    return arr

def counting_zero(arr):
    cnt = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 0:
                cnt += 1
    return cnt

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
myyx = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            myyx.append((y, x))

candidates = list(combinations(myyx, 3))
max_candidate = []
for candidate in candidates:
    new_board = [i[:] for i in board]
    new_board = building_wall(candidate, new_board)
    new_board2 = start_virus(new_board)
    mymax = counting_zero(new_board2)
    max_candidate.append(mymax)
print(max(max_candidate))