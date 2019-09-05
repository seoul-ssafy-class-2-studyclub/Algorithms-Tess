
'''
1
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
'''


import sys
sys.stdin = open('1949.txt', 'r')

# dfs + 재귀
def dfs(y, x, cnt, k, n):
    global res
    if (res < cnt + 1):
        res = cnt + 1
    visited[y][x] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny >= 0 and ny < n and nx >= 0 and nx < n):
            if (visited[ny][nx] == 0): # 0이 아니라면
                # 안깎고 이동이 가능할 때
                if (arr[ny][nx] < arr[y][x]):
                    dfs(ny, nx, cnt + 1, k, n)
                # 깎고 이동할 때
                elif (arr[ny][nx] - k < arr[y][x]):
                    # 값 저장
                    pre = arr[ny][nx]
                    # 깎고
                    arr[ny][nx] = arr[y][x] - 1
                    dfs(ny, nx, cnt + 1, 0, n)
                    # 값 복귀
                    arr[ny][nx] = pre
    visited[y][x] = 0

T = int(input())
for tc in range(T):
    n, k = map(int, input().split())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    res = 0
    maxV = 0
    visited = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (maxV < arr[i][j]):
                maxV = max(maxV, arr[i][j])
    v = []
    for i in range(n):
        for j in range(n):
            if (arr[i][j] == maxV):
                v.append([i, j])
    for i in range(len(v)):
        dfs(v[i][0], v[i][1], 0, k, n)

    print("#{} {}".format(tc + 1, res))



# 무슨 K가 주어지던 1번만 깎는다.
# BFS로 가장 깊은 depth까지 도달하기


# def search(yx, arr, k):
#     cnt = 0
#     q = []
#     q.append(((yx[0], yx[1]), cnt))
#     res = []
#     while q:
#         myk = k
#         used = False
#         visit = [[False] * N for _ in range(N)] # 한번 쭉 갈때 비지트를 다시 만들어준다.
#         yx, cnt = q.pop()
#         cnt += 1
#         y = yx[0]
#         x = yx[1]
#         visit[y][x] = True
#         for dy, dx in d:
#             iy = dy + y
#             ix = dx + x
#             if 0 <= iy < N and 0 <= ix < N:
#                 if visit[iy][ix] == False:
#                     if arr[y][x] > arr[iy][ix]:
#                         q.append(((iy, ix), cnt))
#                     elif arr[y][x] <= arr[iy][ix]:
#                         if arr[y][x] > arr[iy][ix]-myk and used == False:
#                             used = True
#                             pre = arr[iy][ix]
#                             arr[iy][ix] = arr[y][x] - 1
#                             q.append(((iy, ix), cnt))
#                             arr[iy][ix] = pre
#                         else:
#                             res.append(cnt)


#
#
# d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#
#     mountains = [list(map(int, input().split())) for _ in range(N)]
#
#
#
#     # 1. 가장 높은 봉우리를 찾는다.
#     highest = 0
#     for y in range(N):
#         for x in range(N):
#             if mountains[y][x] > highest:
#                 highest = mountains[y][x]
#     #print(highest)
#
#     # 2. 시작점의 좌표를 구한다. 모든 시작점을 넣을 예정이다.
#     highest_yx = []
#     for y in range(N):
#         for x in range(N):
#             if mountains[y][x] == highest:
#                 highest_yx.append((y, x))
#     #print(highest_yx)
#
#
#     # 3. 받아온 시작점들을 하나하나 함수 안에서 실행하고 그중에서 맥스값을 리턴받아 특정 리스트에 넣은 후,
#     temp_maxes = []
#     res = 0
#     #print('-------------tc9', tc)
#     visit = [[False] * N for _ in range(N)]
#     for my_yx in highest_yx:
#         #print('-------------tc9', tc, highest_yx)
#         # temp_mountains = [i[:] for i in mountains]
#         temp_max = search(my_yx[0], my_yx[1], K, 0)
#         temp_maxes.append(temp_max)
#     # 4. 마지막에 리스트에서 맥스값을 찾아 낼 것임.
#     #print(temp_max)
#     #print(temp_maxes)
#     result = max(temp_maxes)
#     print(f'#{tc}', result)



''''''


    #
    # def dfs(y, x, cnt, k, n):
    #     global res
    #     if (res < cnt + 1):
    #         res = cnt + 1
    #     visited[y][x] = 1
    #     dx = [0, 1, 0, -1]
    #     dy = [1, 0, -1, 0]
    #     for i in range(4):
    #         ny = y + dy[i]
    #         nx = x + dx[i]
    #         if (ny >= 0 and ny < n and nx >= 0 and nx < n):
    #             if (visited[ny][nx] == 0):
    #                 # 안깎고 이동이 가능할 때
    #                 if (arr[ny][nx] < arr[y][x]):
    #                     dfs(ny, nx, cnt + 1, k, n)
    #                 # 깎고 이동할 때
    #                 elif (arr[ny][nx] - k < arr[y][x]):
    #                     # 값 저장
    #                     pre = arr[ny][nx]
    #                     # 깎고
    #                     arr[ny][nx] = arr[y][x] - 1
    #                     dfs(ny, nx, cnt + 1, 0, n)
    #                     # 값 복귀
    #                     arr[ny][nx] = pre
    #     visited[y][x] = 0
    #
    #
    # T = int(input())
    #
    # for tc in range(T):
    #     n, k = map(int, input().split())
    #
    #     arr = []
    #     for i in range(n):
    #         arr.append(list(map(int, input().split())))
    #
    #     res = 0
    #     maxV = 0
    #     visited = [[0] * n for i in range(n)]
    #     for i in range(n):
    #         for j in range(n):
    #             if (maxV < arr[i][j]):
    #                 maxV = max(maxV, arr[i][j])
    #     v = []
    #     for i in range(n):
    #         for j in range(n):
    #             if (arr[i][j] == maxV):
    #                 v.append([i, j])
    #     for i in range(len(v)):
    #         dfs(v[i][0], v[i][1], 0, k, n)
    #
    #     print("#{} {}".format(tc + 1, res))