################## 확인
# 받은 정보의 dir은 내 주위에 있는 애들이 change할 애라면, 방향을 나랑 반대로 해서 움직이고,
# 만약 걔가 움직이면 또, 영향 받는 애가 있지만,
# 움직이지 않는다면 그 애의 옆에가 change해야할것이여도, 영향받지 않는다.
# 돌릴애랑 인접한 애들을 구한다.

'''
0이면 1
1이면 0, 2
2이면 1, 3
3이면 2
'''
# [12 1.5 3 4.5 6 7.5 9 10.5]
# [0, 1, 2, 3, 4, 5, 6, 7]
# [, 3, 6, 9]
# 1이면 시계방향, -1이면 반시계방향

import sys
# sys.stdin = open('14891_톱니바퀴.txt', 'r')

input = sys.stdin.readline
import collections
data = [ collections.deque(list(map(str, input().strip()))) for _ in range(4)]
N = int(input())
directions = {1: -1, -1: 1}

q = collections.deque([])
visit = [False] * 4
for i in range(N):
    name, di = map(int, input().split())
    q.append((name-1, di, visit))

adj_list = [[(1,6,2)], [(0,2,6), (2,6,2)], [(1, 2, 6),(3, 6, 2)], [(2,2,6)]]
while q: # 담긴 수 만큼 돌텐데요 :-)

    start, dir, visit = q.popleft()
    visited = visit[:]

    # 바꿀 방향을 다 저장해 두고 그다음에 기어를 돌린다.
    result = [0]*4
    if visited[start] == False:
        visited[start] = True
        result[start] = dir

    myq = collections.deque([])
    myq.append((start, dir))

    while myq:
        start, dir = myq.popleft()
        for child, childidx, meidx in adj_list[start]:
            # 1, 3의 인접리스트를 도는데,
            if visited[child] == False:
                visited[child] = True
                if data[child][childidx] != data[start][meidx]:
                    result[child] = directions[dir]
                    myq.append((child, directions[dir]))

    for i in range(4):
        if result[i] == 1:
            back = data[i].pop()
            data[i].appendleft(back)
        elif result[i] == -1:
            front = data[i].popleft()
            data[i].append(front)

scores = [1, 2, 4, 8]
myres = 0
for i in range(4):
    if data[i][0] == '1':
        myres += scores[i]
print(myres)