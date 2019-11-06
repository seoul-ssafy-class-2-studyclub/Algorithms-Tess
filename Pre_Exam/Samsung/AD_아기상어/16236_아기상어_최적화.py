import sys
input = sys.stdin.readline
N = int(input())
underWater = []
for y in range(N):
    data = list(map(int, input().split()))
    underWater.append(data)
    if 9 in data:
        x = data.index(9)
        shark = [2, y, x, 0]
        underWater[y][x] = 0
time = 0
while True:
    q = []
    q.append((shark[1], shark[2], 0, shark[3]))
    foods = []
    visited = [[False]*N for _ in range(N)]
    while q:
        y, x, dist, cnt = q.pop(0)
        visited[y][x] = True
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < N and visited[iy][ix] == False:
                if underWater[iy][ix] < shark[0] and underWater[iy][ix] != 0:
                    foods.append((dist + 1, iy, ix))
                    q.append((iy, ix, dist + 1, cnt))
                    visited[iy][ix] = True
                elif underWater[iy][ix] == shark[0] or underWater[iy][ix] == 0:
                    q.append((iy, ix, dist + 1, cnt))
                    visited[iy][ix] = True
    foods = sorted(foods)
    if len(foods) == 0:
        break
    if len(foods) != 0:
        foodsDistance, foodsy, foodsx = foods[0][0], foods[0][1], foods[0][2]
        shark[3] += 1
        underWater[foodsy][foodsx] = 0
        time += foodsDistance
        shark[1], shark[2] = foodsy, foodsx
        if shark[0] == shark[3]:
            shark[0] += 1
            shark[3] = 0
print(time)

