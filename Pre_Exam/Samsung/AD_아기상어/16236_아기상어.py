import sys
sys.stdin = open('16236.txt', 'r')

# heapq 사용하여 풀기
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

N = int(input())
underWater = []
for _ in range(N):
    data = list(map(int, input().split()))
    underWater.append(data)
print(underWater)

# 돌면서 데이터를 리스트에 받을건데,
# 힙큐를 사용할것
# size, [distance], y, x 순으로 저장해서 우선순위에 따른 데이터 정렬을 할 예정
shark = []
foods = []
for y in range(N):
    for x in range(N):
        if 1 <= underWater[y][x] <= 6:
            foods.append([underWater[y][x], y, x])
        elif underWater[y][x] == 9:
            shark.append([2, y, x])

# 계속 갱신될 정보
foods = sorted(foods)
# 먹으면 shark의 칸은 food의 칸과 바꿔진다.
print(foods)

# 계속 갱신될 정보 => 딕셔너리로 바꿀까?
print(shark)
for i in range(len(foods)):
    disy = abs(shark[0][1]-foods[i][1])
    disx = abs(shark[0][2]-foods[i][2])
    # 계속 갱신될 정보
    distance = disx + disy
    foods[i].insert(1, distance)
    print(distance)
print(foods)

# 모든 물고기들이 가진 거리를 shark를 기준으로 계산한다.

