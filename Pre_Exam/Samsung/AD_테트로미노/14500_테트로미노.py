# import sys
# sys.stdin = open('14500.txt', 'r')

# DFS로 깊이 4까지 탐색
# 도형 방향은 바뀐다.
# ㅣ ㅡ ㅣ ㅡ
# ㅁ ㅁ ㅁ ㅁ 
# ㄴ ㄱ . .
# ㄹ . . .
# ㅗ ㅓ ㅏ ㅜ 모양은 dfs 탐색이 불가능하므로 예외 처리 필요  -> 이유
'''
1) 맵의 꼭지점일 때
2) 맵의 테두리일때
3) 일반적일 때
'''



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxVal = 0


## 최대 4개짜리 dfs로 전부 탐색하면됨
def dfs(x, y, visited, count, sumVal):
    global maxVal

    if count == 4:
        if maxVal < sumVal:
            maxVal = sumVal
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < N and 0 <= ny and ny < M:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny, visited, count + 1, sumVal + arr[nx][ny])
                visited[nx][ny] = False


## ㅗ 모양은 dfs로 탐색이 안돼서 따로 처리해줌
## 가운데일 때를 기준으로 네방향 탐색
def fuck(x, y):
    global maxVal
    sumVal = arr[x][y]

    ## x, y가 모서리면 ㅗ 모양은 아예 불가능
    if x == 0:
        if y == 0 or y == M - 1:
            return
    elif x == N - 1:
        if y == 0 or y == M - 1:
            return

    ## x나 y가 가장자리에 있으면 ㅗ 모양은 하나밖에 안나옴
    if x == 0:
        sumVal += arr[x + 1][y] + arr[x][y - 1] + arr[x][y + 1]
    elif x == N - 1:
        sumVal += arr[x - 1][y] + arr[x][y - 1] + arr[x][y + 1]
    elif y == 0:
        sumVal += arr[x][y + 1] + arr[x - 1][y] + arr[x + 1][y]
    elif y == M - 1:
        sumVal += arr[x][y - 1] + arr[x - 1][y] + arr[x + 1][y]
    else:
        sumlist = []
        sumlist.append(sumVal + arr[x + 1][y] + arr[x][y - 1] + arr[x][y + 1])
        sumlist.append(sumVal + arr[x - 1][y] + arr[x][y - 1] + arr[x][y + 1])
        sumlist.append(sumVal + arr[x][y + 1] + arr[x - 1][y] + arr[x + 1][y])
        sumlist.append(sumVal + arr[x][y - 1] + arr[x - 1][y] + arr[x + 1][y])
        sumVal = max(sumlist)

    if maxVal < sumVal:
        maxVal = sumVal


def solve(): # 처음 시작하는 함수
    visited = [[False] * M for _ in range(N)] # 여기서 visit을 한다. 열에 해당하는 만큼 visitied를 생성
    for i in range(N): # 전체 보드를 돈다.
        for j in range(M):
            fuck(i, j) # ㅗ ㅏ ㅓ ㅜ 으로 도는 도형
            visited[i][j] = True
            dfs(i, j, visited, 1, arr[i][j]) # 다른 도형들을 찾는 재귀함수
            visited[i][j] = False



N, M = map(int, input().split())
print(N, M)

arr = [list(map(int, input().split())) for _ in range(N)]

solve()
print(maxVal) # result