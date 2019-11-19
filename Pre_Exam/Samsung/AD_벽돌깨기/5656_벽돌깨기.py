import sys
sys.stdin = open('5656.txt', 'r')
from pprint import pprint
# 1.
def hitAndSpread(ar, vi, id):
    q = []
    # 앞에서 부터
    for y in range(H):
        if ar[y][id] != 0:
            q.append((y, id))
            vi[y][id] = True
            break
    # vi에 퍼진애만 체크한다.
    # 퍼질애는 다 퍼졌는가?
    # ar은 그냥 참고용
    while q:
        y, x = q.pop(0)
        ########### 처리 확인해야 한다.
        if ar[y][x] == 1:
            # 1이라면 아래 할 필요없이 다른걸 꺼낸다.
            vi[y][x] = True
            continue
        else:
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # 하나 돌때마다 증가되어야하니까
                # 원본을 복사해두고 시작
                ory = y
                orx = x
                # 9
                for i in range(0, ar[y][x] - 1):
                    iy = ory + dy
                    ix = orx + dx
                    if 0 <= iy < H and 0 <= ix < W and vi[iy][ix] == False and ar[iy][ix] != 0:
                        vi[iy][ix] = True
                        q.append((iy, ix))
                    ory = iy
                    orx = ix
    return ar, vi


# 2.
def popping(ar, vi):
    for y in range(H):
        for x in range(W):
            if vi[y][x] == True:
                ar[y][x] = 0
    return ar


# 3.
def gravity(ar):

    # 위로 올라가면서 0으로 바꿔가며 쌓고,
    # 위로 올라가면서 다시 놓는다

    for x in range(W-1, -1, -1):
        stack = []
        for y in range(H-1, -1, -1):
            if ar[y][x] != 0:
                stack.append(ar[y][x])
                ar[y][x] = 0

        for y in range(H-1, -1, -1):
            if len(stack) != 0:
                data = stack.pop(0)
                ar[y][x] = data
    return ar


# 4.
def check(ar):
    cnt = 0
    for y in range(H):
        for x in range(W):
            if ar[y][x] != 0:
                cnt += 1
    return cnt

def solve(t):
    global mymin, origin
    arr = [i[:] for i in origin]
    # 작업 시작하는 함수
    tt = t[:]
    while tt:
        # 순열생성시 조심좀
        idx = tt.pop()

        vis = [[False]*W for _ in range(H)]
        arr, vis = hitAndSpread(arr, vis, idx)
        arr = popping(arr, vis)
        arr = gravity(arr)

    mymin = min(mymin, check(arr))
    return mymin


def permut(k):
    global candis
    if k == N:
        # 복사가 아니라 참조인 상태로 append되기때문에 항상 현상태를 복사해서 append해줘야한다.
        candis.append(t[:])
        return
    else:
        for i in range(0, W):
            t[k] = wIndexes[i]
            permut(k+1)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    origin = [list(map(int, input().split())) for _ in range(H)]
    mymin = 1e9
    candis = []
    wIndexes = [i for i in range(W)]
    t = [0]*N
    permut(0)
    for t in candis:
        ans = solve(t)
        if ans == 0:
            break

    print(f'#{tc} {mymin}')

    ### test
    # arr = [i[:] for i in origin]
    # vis = [[False] * W for _ in range(H)]
    # hitAndSpread(arr, vis, 2)