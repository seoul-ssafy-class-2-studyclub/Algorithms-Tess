import sys
from pprint import pprint

import itertools
sys.stdin = open('15683.txt', 'r')

def colouring(arr, permut, yx):
    global status
    # 3. status에 따라 방향이 달라진다.
    # 4. 방향에 맞춰서 '#' 로채운다.

    ############## 여기서 한번 쭉 가고 끝나버리는 문제 해결하면된다.
    for idx in range(len(permut)):
        status = permut[idx]
        y, x = yx[idx]
        visited = [[0]*M for _ in range(N)]
        if status == 0:
            if arr[y][x] == 1:
                stack = []
                stack.append((y, x))
                while stack:
                    y, x = stack.pop()
                    if arr[y][x] == 0:
                        arr[y][x] = -1
                    dy, dx = case1[0]
                    iy = y + dy
                    ix = x + dx
                    if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                        if -1 <= arr[iy][ix] <= 5:
                            stack.append((iy, ix))
                            visited[iy][ix] = 1
                        elif arr[iy][ix] == 6:
                            break
            if arr[y][x] == 2:
                for i in range(len(case1[1])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case1[1][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
            if arr[y][x] == 3:
                for i in range(len(case1[2])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case1[2][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
            if arr[y][x] == 4:
                for i in range(len(case1[3])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case1[3][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break

            if arr[y][x] == 5:
                for i in range(len(case1[4])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case1[4][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
        if status == 1:
            if arr[y][x] == 1:

                stack = []
                stack.append((y, x))
                while stack:
                    y, x = stack.pop()
                    if arr[y][x] == 0:
                        arr[y][x] = -1
                    dy, dx = case2[0]
                    iy = y + dy
                    ix = x + dx
                    if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                        if -1 <= arr[iy][ix] <= 5:
                            stack.append((iy, ix))
                            visited[iy][ix] = 1
                        elif arr[iy][ix] == 6:
                            break
            if arr[y][x] == 2:
                for i in range(len(case2[1])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case2[1][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
            if arr[y][x] == 3:
                for i in range(len(case2[2])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case2[2][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break

            if arr[y][x] == 4:
                for i in range(len(case2[3])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case2[3][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
            if arr[y][x] == 5:
                for i in range(len(case2[4])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case2[4][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break

        if status == 2:
            if arr[y][x] == 1:

                stack = []
                stack.append((y, x))
                while stack:

                    y, x = stack.pop()
                    if arr[y][x] == 0:
                        arr[y][x] = -1
                    dy, dx = case3[0]
                    iy = y + dy
                    ix = x + dx
                    if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                        if -1 <= arr[iy][ix] <= 5:
                            stack.append((iy, ix))
                            visited[iy][ix] = 1
                        elif arr[iy][ix] == 6:
                            break

            if arr[y][x] == 2:
                for i in range(len(case3[1])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case3[1][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
            if arr[y][x] == 3:
                for i in range(len(case3[2])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case3[2][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break

            if arr[y][x] == 4:
                for i in range(len(case3[3])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case3[3][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
            if arr[y][x] == 5:
                for i in range(len(case3[4])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case3[4][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
        if status == 3:
            if arr[y][x] == 1:
                stack = []
                stack.append((y, x))
                while stack:
                    y, x = stack.pop()
                    if arr[y][x] == 0:
                        arr[y][x] = -1
                    dy, dx = case4[0]
                    iy = y + dy
                    ix = x + dx
                    if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                        if -1 <= arr[iy][ix] <= 5:
                            stack.append((iy, ix))
                            visited[iy][ix] = 1
                        elif arr[iy][ix] == 6:
                            break
            if arr[y][x] == 2:
                for i in range(len(case4[1])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case4[1][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break

            if arr[y][x] == 3:
                for i in range(len(case4[2])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case4[2][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
            if arr[y][x] == 4:
                for i in range(len(case4[3])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case4[3][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
            if arr[y][x] == 5:
                for i in range(len(case4[4])):
                    y, x = yx[idx]
                    stack = []
                    stack.append((y, x))
                    while stack:
                        y, x = stack.pop()
                        if arr[y][x] == 0:
                            arr[y][x] = -1
                        dy, dx = case4[4][i]
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == 0:
                            if -1 <= arr[iy][ix] <= 5:
                                stack.append((iy, ix))
                                visited[iy][ix] = 1
                            elif arr[iy][ix] == 6:
                                break
    return arr


def chk(arr2):
    my_num = 0
    for y in range(N):
        for x in range(M):
            if arr2[y][x] == 0:
                my_num += 1
    return my_num

# 총 한번의 테케에 4번의 경우의 수가 있고,
# 4번 중에 하나의 최소값을 구하면 된다.

        # 상 하 우 좌
        # 0 1 2 3

delta = [(-1,0), (1,0), (0, 1), (0, -1)]

# 인덱스 0부터 4까지 1부터 5 CCTV가 각 상황에따라 취할 방향을 적는다.
case1 = [(delta[2]),
         (delta[2], delta[3]),
         (delta[0], delta[2]),
         (delta[0], delta[2], delta[3]),
         (delta),
         ] # 0도 회전
case2 = [(delta[1]),
         (delta[0], delta[1]),
         (delta[1], delta[2]),
         (delta[0], delta[1], delta[2]),
         (delta),
         ]  # 90도 회전
case3 = [(delta[3]),
         (delta[2], delta[3]),
         (delta[3], delta[1]),
         (delta[1], delta[2], delta[3]),
         (delta),
         ] # 180도 회전
case4 = [(delta[0]),
         (delta[0], delta[1]),
         (delta[0], delta[3]),
         (delta[0], delta[1], delta[3]),
         (delta),
         ]  # 270도 회전

# def mypermutations(k=0):
#     global status
#     global result_1
#     global my_num
#     if k == my_num:
#         result2 = A[:]
#         result_1.append(result2)
#         return True
#     for i in range(4):
#         A[k] = status[i]
#         mypermutations(k+1)
#         A[k] = 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 처음 status

my_yx = []
for iiy in range(N):
    for iix in range(M):
        if 1 <= board[iiy][iix] <= 5:
            my_yx.append((iiy, iix))
my_num = len(my_yx)
status = [0, 1, 2, 3]
'''
함수쓰기
'''
candidate_status = list(itertools.product(status, repeat=my_num))
'''
직접만들기
'''
# A = [0]*8
# result_1 = []
# mypermutations()
# print(result_1)
# 중복 순열으로 빼온 케이스를 토대로
# 순열 후보를 하나씩 함수안에서 돌면서,
# 순열과 myxy의 인덱스를 맞추고,
# 맞춘 것에 맞게 계산하여
# 모든 순열을 돈다.

# 1. 총 for문은 4번돈다.
result_list = []
for candidate in candidate_status:
# 2. status를 한번 돌때마다 1씩 더해준다.
# 2-1. deepcopy해준다.
    temp_board = [i[:] for i in board]
    temp_board = colouring(temp_board,  candidate, my_yx)
    res = chk(temp_board)
    result_list.append(res)
    # 5. 채운 걸 토대로 0을 센다
    # pprint(temp_board)

# 6. 반환한다.
# 7. 리스트에 추가한다.
print(min(result_list))
############## CCTV 각자 어떤 방향으로 돌건지 경우의 수 존재
# http://blog.naver.com/PostView.nhn?blogId=godori91&logNo=221254315307&parentCategoryNo=&categoryNo=45&viewDate=&isShowPopularPosts=true&from=search

