import sys
sys.stdin = open('1949.txt', 'r')

def dfs(y, x, cnt, k, n):
    global res
    if res < cnt + 1: # 값을 계속 저장하면서, 재귀내에서 res를 잃어버리지 않는다.
        res = cnt + 1
    visited[y][x] = True # 재귀의 시작이 있을때마다 True로 표시
    for dy, dx in d:
        iy = dy + y
        ix = dx + x
        if 0 <= iy < n and 0 <= ix < n:
            if visited[iy][ix] == 0: # 0이 아닌 재귀는 사라져서 없어진다.
                if arr[iy][ix] < arr[y][x]: # if가 가장 먼저 실행된다.
                    dfs(iy, ix, cnt+1, k, n)
                elif arr[iy][ix] - k < arr[y][x]: # 현재 위치의 숫자보다 계산된 숫자가 작아질 수 있으면,
                    pre = arr[iy][ix] # 값 저장
                    arr[iy][ix] = arr[y][x] - 1 # 바뀐 값을 저장해준다.
                    dfs(iy, ix, cnt+1, 0, n) # k는 사용되었으므로 0으로 없애준다.
                    # 해당 부분을 넘긴 상태가 지난 후에 재귀가 나올때 복귀될 부분
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

    # 준비된 후보군들을 하나씩 넣는다.
    for i in range(len(v)):
        dfs(v[i][0], v[i][1], 0, k, n)

    print("#{} {}".format(tc + 1, res))