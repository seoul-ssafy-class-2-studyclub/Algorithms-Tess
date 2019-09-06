def dfs(y, x, cnt, k, n):
    global res
    if res < cnt + 1:
        res = cnt + 1
    visited[y][x] = True
    for dy, dx in d:
        iy = dy + y
        ix = dx + x
        if 0 <= iy < n and 0 <= ix < n:
            if visited[iy][ix] == 0:
                if arr[iy][ix] < arr[y][x]:
                    dfs(iy, ix, cnt+1, k, n)
                elif arr[iy][ix] - k < arr[y][x]:
                    pre = arr[iy][ix]
                    arr[iy][ix] = arr[y][x] - 1
                    dfs(iy, ix, cnt+1, 0, n)
                    arr[iy][ix] = pre
    visited[y][x] = False

d = [(0,1),(0,-1),(1,0),(-1,0)]
T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    res = 0
    maxV = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maxV < arr[i][j]:
                maxV = max(maxV, arr[i][j])
    v = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == maxV:
                v.append([i, j])

    for i in range(len(v)):
        dfs(v[i][0], v[i][1], 0, k, n)

    print("#{} {}".format(tc + 1, res))