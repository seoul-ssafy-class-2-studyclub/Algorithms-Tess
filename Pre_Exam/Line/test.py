# 코니가 (2,1) 위치로 도망을 갔다. 문이 (0,0) 위치에서 출발
def find(y, x, v, t):
    if y == CY and x == CX:
        mymintime.append(t)
        return True

    for dy, dx in [(0, 1), (1, 0)]:
        iy = dy + y
        ix = dx + x
        if 0 <= iy < M and 0 <= ix < N and v[iy][ix] == False:
            v[iy][ix] = True
            t += 1
            find(iy, ix, v, t)
            t -= 1
            v[iy][ix] = False


# 가로, 세로
N, M = map(int, input().split())
mymap = [[0] * N for _ in range(M)]
CX, CY = map(int, input().split())
vis = [[False] * N for _ in range(M)]
mymintime = []
vis[0][0] = True
find(0, 0, vis, 0)
myminres = min(mymintime)
resnum = mymintime.count(myminres)
print(myminres)
print(resnum)