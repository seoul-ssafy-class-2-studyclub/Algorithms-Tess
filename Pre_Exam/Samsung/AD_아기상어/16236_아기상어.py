'''
N x N 공간
물고기 M마리
아기상어 1마리 
한칸에는 물고기가 최대 1마리만 존재
아기상어와 물고기는 크기를 가지고 있고, 이 크기는 자연수
처음 아기상어의 크기는 2 -> 1초에 상하좌우로 한 칸씩이동

아기 상어는 자신의 크기보다 큰 물고기가있는 칸은 지날 수 없지만
1) 작거나 -> 먹는다. 빈칸으로 만든다. (이동과 동시에 먹는다)
    먹으면, 현재 크기에서 크기가 1이 증가한다.
2) 빈칸은
지나갈 수 있다.

이동 순서
1) 더이상 먹을 수 있는 물고기가 없다면 아기상어는 엄마 상어를 부른다.
    - 더이상 작은 물고기가 없다면,
    - 모든 물고기를 다 먹었다면
2) 먹을 수 있는 물고기가 1마리면 먹으러 간다. (작은크기) (같거나 큰건 먹을 수 없다)
3) 먹을 수 있는 물고기가 2마리 이상이면 거리가 가장 가까운걸 먹는다.
    - 거리: 먹으러 갈때 지나야하는 최소 칸의 개수
    - 거리가 똑같은 곳에 물고기가 있다면,1) 가장위 
                                2) 위에서 많으면 가장왼쪽

---입력---
첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.

0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
아기 상어는 공간에 한 마리 있다.

'''
import sys
# sys.stdin = open('16236.txt', 'r')
input = sys.stdin.readline
N = int(input())
underWater = []
for _ in range(N):
    data = list(map(int, input().split()))
    underWater.append(data)

shark = []
for y in range(N):
    for x in range(N):
        if underWater[y][x] == 9:
            shark.append([2, y, x, 0])
            underWater[y][x] = 0
# 먹으면 shark의 칸은 food의 칸과 바꿔진다.
# 크기가 크거나 같은 애들밖에 없는 경우

# 결과가 나올때까지 함수를 계속해서 돌려야 하므로, while문 안에 둔다

time = 0
while True:
    q = []
    q.append((shark[0][0], shark[0][1], shark[0][2], 0, shark[0][3]))

    foods = []
    visited = [[False]*N for _ in range(N)]

    while q:
        size, y, x, dist, cnt = q.pop(0)
        visited[y][x] = True
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < N and visited[iy][ix] == False:
                if underWater[iy][ix] < size and underWater[iy][ix] != 0:
                    foods.append((dist + 1, iy, ix, underWater[iy][ix]))
                    q.append((size, iy, ix, dist + 1, cnt))
                    visited[iy][ix] = True
                elif underWater[iy][ix] == size or underWater[iy][ix] == 0:
                    q.append((size, iy, ix, dist + 1, cnt))
                    visited[iy][ix] = True
    # 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
    # 예를 들어,
    # 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
    foods = sorted(foods)
    if len(foods) == 0:
        break

    if len(foods) != 0:
        foodsDistance, foodsy, foodsx, foodsSize = foods[0][0], foods[0][1], foods[0][2], foods[0][3]
        shark[0][3] += 1
        underWater[foodsy][foodsx] = 0
        time += foodsDistance
        shark[0][1], shark[0][2] = foodsy, foodsx
        if shark[0][0] == shark[0][3]:
            # 1이 크면 다시 탐색해서 다음 애들도 내 순위로 넣을 수 있다. 그러니까 다시 탐색하러 가자.
            shark[0][0] += 1
            shark[0][3] = 0

print(time)

