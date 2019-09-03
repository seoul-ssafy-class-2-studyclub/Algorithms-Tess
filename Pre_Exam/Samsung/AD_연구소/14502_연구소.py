import sys
sys.stdin = open('14502.txt', 'r')

from itertools import combinations
import copy


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

## 3개를 놓는 경우의 수가 뭘까 인지 생각


# 1. 벽을 3개 놓을 수 있는 경우의 수를 구한다. 즉,
# 2. 0인 곳의 좌표를 모두 구하고,
# 3. 해당하는 좌표의 경우의 수를 구한다.
# 4. 해당 좌표들을 각각 튜플형식으로 놓고 itertools를 사용하여 3개가 있는 조합을 구한다.

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

myyx = []

for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            myyx.append((y, x))


# 중복없는 카운트 만드는 코드
candidates = list(combinations(myyx, 3))

max_candidate = []

for candidate in candidates:
    new_board = copy.deepcopy(board)
    # 5. 스택에 해당 조합을 넣고,
    # 6. 벽을 세운다음에
    new_board = building_wall(candidate, new_board)
    #print(new_board)

    # 7. 2를 퍼트리고
    new_board2 = start_virus(new_board)
    #print(new_board)

    # 8. 퍼트린 보드에서 0을 구하고,
    # 9. 리스트에 추가한 후, 해당 리스트에 있는 값중에 최대값을 구한다.
    mymax = counting_zero(new_board2)

    max_candidate.append(mymax)
print(max(max_candidate))



