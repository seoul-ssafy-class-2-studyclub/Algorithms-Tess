import sys
sys.stdin = open('14503.txt', 'r')

import collections
N, M = map(int, input().split())
r, c, d = map(int, input().split())

dirts = [ list(map(int, input().split())) for _ in range(N) ]
visit = [ [False]*M for _ in range(N) ]

'''
1.현재 위치를 청소한다.
2.현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
'''

'''
d
0 북 북에서 왼쪽은 서 0,-1 를 본다.
1 동 동에서 왼쪽은 북 -1,0
2 남 남에서 왼쪽은 동 0, 1
3 서 서에서 왼쪽은 남 1, 0

dirts[현재위치]가 1이 아니라면 청소하고 visit[현재위치]를 True처리
분기는 네개로 나뉜다

dirts[현재위치]가 1이라면, 현재 방향을 기준으로 왼쪽을 보는데,
1. 왼쪽이 visit한적도없고, 0이라면, 거기로 움직이고, 방향을 바꾼후 청소한다.
2. 왼쪽이 청소할 공간이 없다면, 방향으로 회전만하고 2번으로 돌아가 다시 탐색을 진행한다.
3. 네방향을 모두 보는데 이미 청소되어있거나 벽인경우에는 바라보는 방향을 유지하고 한칸 후진 후 2번으로 돌아간다.
4. 위와 동일하지만 뒤쪽이 벽인경우 작동을 멈춘다.
** 로봇청소기는 항상 빈칸에 처음 놓아진다.
'''
numofclean = 0
visit[r][c] = True
dirts[r][c] = 1
numofclean += 1
firstseeing = {0:(0,-1, 3), 1:(-1,0, 0), 2:(0,1, 1), 3:(1,0, 2)}

for y in range(N):
    for x in range(M):
        if dirts[y][x] == 1:
            visit[y][x] = True


q = collections.deque([])
q.append((r, c, d))
flag = 0

while q:
    status = 0
    r, c, d = q.popleft()

    if status == 0:
    #1번의 경우, 실패하면 그냥 빌 것
        fy, fx, tempd = firstseeing[d]
        iy = fy + r
        ix = fx + c
        if 0 <= iy < N and 0 <= ix < M:
            if dirts[iy][ix] == 0 and visit[iy][ix] == False:
            # 1. 왼쪽이 visit한적도없고, 0이라면, 거기로 움직이고, 방향을 바꾼후 청소한다.
                dirts[iy][ix] = 1
                visit[iy][ix] = True
                numofclean += 1
                q.append((iy, ix, tempd))
            else:
                status = 1
                print('-----')
                q.append((r, c, tempd))

    if status == 1:
        check = 0
        for dy, dx in [(0,1), (1,0), (-1,0), (0,-1)]:
            iy = dy + r
            ix = dx + c
            if 0 <= iy < N and 0 <= ix < M and visit[iy][ix] == True and dirts[iy][ix] == 1:
                check += 1
            print(check)
        if check == 4:
            while True:
                if d == 0:
                    r = r+1
                    break
                if d == 1:
                    c = c-1
                    break
                if d == 2:
                    r = r-1
                    break
                if d == 3:
                    c = c+1
                    break
            visit[r][c] = True
            q.append((r, c, d))

        if check == 3:
            while True:
                if d == 0:
                    r = r+1
                    break
                if d == 1:
                    c = c-1
                    break
                if d == 2:
                    r = r-1
                    break
                if d == 3:
                    c = c+1
                    break
            if dirts[r][c] == 1:
                flag = 1

    if flag == 1:
        break

print(numofclean)



# import sys
#
# N = M = 0
# arr = []
# ## 북 동 남 서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# def countClean():
#     count = 0
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] > 1:
#                 count += 1
#     return count
#
#
# def leftTurn(d):
#     if d == 0:
#         return 3
#     else:
#         return d - 1
#
#
# def clean(x, y, d, turnCount):
#     while True:
#         ## 4방향 모두 탐색했으면
#         if turnCount == 4:
#             backX = x - dx[d]
#             backY = y - dy[d]
#
#             if arr[backX][backY] == 1:
#                 print(countClean())
#                 return
#             else:
#                 x, y, d, turnCount = backX, backY, d, 0
#
#         ## 1. 현재 위치를 청소한다.
#         if arr[x][y] == 0:
#             arr[x][y] = 2
#
#         ## 2. 왼쪽 방향부터 탐색
#         ld = leftTurn(d)
#         nx = x + dx[ld]
#         ny = y + dy[ld]
#
#         ## 왼쪽 방향에 청소 안함 (1) 1번부터 다시 시작
#         if arr[nx][ny] == 0:
#             x, y, d, turnCount = nx, ny, ld, 0
#         else:
#             ## 왼쪽 방향에 청소함 (2) 2번부터 시작
#             ## 벽이면 왼쪽 탐색
#             x, y, d, turnCount = x, y, ld, turnCount + 1
#
#
# if __name__ == '__main__':
#     N, M = map(int, sys.stdin.readline().split())
#     r, c, d = map(int, sys.stdin.readline().split())
#     visited = [[False] * M for i in range(N)]
#
#     for i in range(N):
#         arr.append(list(map(int, sys.stdin.readline().split())))
#
#     clean(r, c, d, 0)
