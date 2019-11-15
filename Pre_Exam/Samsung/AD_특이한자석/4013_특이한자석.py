import sys
sys.stdin = open('4013.txt', 'r')

import collections

newdir = {1:-1, -1:1}
# 내 이웃, 나랑 비교되는 이웃의 idx, 나의 idx
myneighbour = {1:[(2, 6, 2)], 2:[(1, 2, 6),(3, 6, 2)], 3:[(2, 2, 6), (4, 6, 2)], 4:[(3,2,6)]}


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnet = {}
    for name in range(1, 5):
        magnet[name] = collections.deque(list(map(int, input().split())))

    q_info = collections.deque([])
    for _ in range(K):
        q_info.append(list(map(int, input().split())))

    while q_info:
        # 앞에서 하나씩 실행하는데,
        # 가장 먼저 움직일 자석, 그 자석의 방향을 말한다.
        # 1이면 시계방향이므로 뒤에껄 빼서 앞에 넣어야하고
        # -1이면 반대인데,
        # 그 과정을 거치기 전에 움직이는 자석과 맞닿아있는 이웃 자석에 대한 상태를 확인해서
        # 어떤식으로 다른 자석들의 상태가 변할건지를 먼저 확인한다.

        name, dir = q_info.popleft()
        status = [0] * 5
        vis = [False] * 5
        q = collections.deque([])
        q.append((name, dir))
        vis[name] = True
        status[name] = dir
        while q:
            name, dir = q.popleft()
            for neighbour, nextidx, myidx in myneighbour[name]:
                if magnet[neighbour][nextidx] != magnet[name][myidx] and vis[neighbour] == False:
                    vis[neighbour] = True
                    # 같지 않으면 다음과 같이 바뀌는데,
                    status[neighbour] = newdir[dir]
                    q.append((neighbour, newdir[dir]))

        # status에 따라 바꾼다
        for i in range(1, 5):
            if status[i] == 1:
                x = magnet[i].pop()
                magnet[i].appendleft(x)
            elif status[i] == -1:
                x = magnet[i].popleft()
                magnet[i].append(x)
    score = [0, 1, 2, 4, 8]
    res = 0
    for i in range(1, 5):
        if magnet[i][0] == 1:
            res += score[i]
    print(f'#{tc} {res}')






import collections
newdir = {1:-1, -1:1}
myneighbour = {1:[(2, 6, 2)], 2:[(1, 2, 6),(3, 6, 2)], 3:[(2, 2, 6), (4, 6, 2)], 4:[(3,2,6)]}
score = [0, 1, 2, 4, 8]
T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnet = {}
    for name in range(1, 5):
        magnet[name] = collections.deque(list(map(int, input().split())))
    q_info = collections.deque([])
    for _ in range(K):
        q_info.append(list(map(int, input().split())))
    while q_info:
        name, dir = q_info.popleft()
        status = [0] * 5
        vis = [False] * 5
        q = collections.deque([])
        q.append((name, dir))
        vis[name] = True
        status[name] = dir
        while q:
            name, dir = q.popleft()
            for neighbour, nextidx, myidx in myneighbour[name]:
                if magnet[neighbour][nextidx] != magnet[name][myidx] and vis[neighbour] == False:
                    vis[neighbour] = True
                    status[neighbour] = newdir[dir]
                    q.append((neighbour, newdir[dir]))
        for i in range(1, 5):
            if status[i] == 1:
                x = magnet[i].pop()
                magnet[i].appendleft(x)
            elif status[i] == -1:
                x = magnet[i].popleft()
                magnet[i].append(x)
    res = 0
    for i in range(1, 5):
        if magnet[i][0] == 1:
            res += score[i]
    print(f'#{tc} {res}')