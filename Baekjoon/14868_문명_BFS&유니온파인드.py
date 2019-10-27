import sys
sys.stdin = open('14868.txt', 'r')
from pprint import pprint
import collections
# bfs union-find


'''
1. 받은 정보를 가지고 보드판을 만든다.
2. 보드판을 dfs를 돌려서 번호를 매긴다.
3. 이때 각 번호마다 속해있는 좌표번호를 해시맵에 저장한다.
4. 저장한 좌표에서 시작해서 상하좌우로 한번씩만 퍼져나간다.
5. 이때 자기자신의 번호를 퍼트리면서 퍼져나가는데, 
-> 퍼져나가는 정보를 범위에넘지않는거만 잘 정리한다.
-> 정보를 토대로 직접 그린다.
6. 다른 번호를 만나면 내 이웃이므로 나의 인접리스트에 자식으로 추가한다.
7. 일년을 지날때마 유니온파인드를 돌려서 
모든 유니온들이 1로 묶여질때 그만 반복한다.
'''


def numbering(y, x, num):
    global world
    q = collections.deque([])
    q.append((y, x))
    world[y][x] = num
    info[num] = [(y, x)]
    while q:
        y, x = q.popleft()
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < N and world[iy][ix] == -1:
                world[iy][ix] = num
                q.append((iy, ix))
                info[num].append((iy, ix))



N, K = map(int, input().split())
world = [[0]*N for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    y = y-1
    x = x-1
    world[y][x] = -1

pprint(world)

# while안에서 1로 묶일때까지 도는 함수들이 안에 작성될것
# while True:

info = {}
number = 1
for y in range(N):
    for x in range(N):
        if world[y][x] == -1:
            print(y, x)
            numbering(y, x, number)
            number += 1
pprint(world)
name = [i for i in range(1, number)]
print(name) # 섬들의 이름을 알 수 있다.
print(info)

# 아래와 같이 섬들은 전파되는데,
# 범위가 벗어나지 않는 가정하
# 1. 0을 만나면 정상적으로 전파
# 근데 이거는 모든게 다 정해졌을때 전파되는거다. 그러니까 전파시킬때는 -1을 적어야한다.
# 그리고 다시 번호를 매겨주는 식으로 해야한다.
# 문명은 한번에 퍼지기때문에. 시간차가 없다.
# 2. 다른 번호, 섬을 만나면 나의 이웃으로 추가
# (a+1,b), (a-1,b), (a,b+1), (a,b-1)





# res = 0
# # union-find
#
#
#
# if res == 1:
#     break


