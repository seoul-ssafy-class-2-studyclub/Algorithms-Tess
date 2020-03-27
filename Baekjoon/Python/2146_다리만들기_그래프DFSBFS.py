'''
섬과 섬 사이에 다리를 놓고, 가장 짧은 다리의 길이를 구하는 문제다. 땅을 DFS를 통해 하나의 섬으로 묶고, 각 섬과 섬 사이의 거리를 BFS를 통해 구하면 된다.

먼저 입력받은 맵에서 붙어있는 육지(1)를 찾아서 섬으로 묶어야 한다.
육지를 섬으로 그룹화하는 과정은 DFS를 통해 진행한다. 인접한 육지를 이동하면서 방문 체크를 하고, 카운트를 매긴다. 예를 들어, 첫 번째 섬은 1, 두 번째 섬은 2, ‥, N 번째 섬은 N으로 맵에 마킹한다.
섬을 체크했다면, 섬과 섬 사이를 BFS를 통해 이동한다.
바다(0)를 이동하다가, 출발한 섬과 다른 섬을 만나면, 이동거리를 최솟값으로 업데이트한다.
'''


import sys
# sys.stdin = open('2146.txt', 'r')
import collections
# from pprint import pprint

'''
3
'''

def DFS(chk_visit, clr, sy, sx):
    stack = collections.deque([])
    stack.append((sy, sx))
    while stack:
        y, x = stack.pop()
        chk_visit[y][x] = True
        earth[y][x] = clr

        for dy, dx in [(0,1), (0,-1), (1,0), (-1, 0)]:
            iy = dy + y
            ix = dx + x

            if 0 <= iy < N and 0 <= ix < N and chk_visit[iy][ix] == False:
                if earth[iy][ix] == 1:
                    stack.append((iy, ix))
    return chk_visit, clr

def BFS(sy, sx, nm, tm):
    global my_min

    q = collections.deque([])
    q.append((sy, sx))
    check2 = [[False] * N for _ in range(N)]
    check2[sy][sx] = True

    while q:
        tm += 1
        for _ in range(len(q)):
            y, x = q.popleft()

            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                iy = dy + y
                ix = dx + x
                if 0 <= iy < N and 0 <= ix < N and check2[iy][ix] == False:
                    if earth[iy][ix] == 0:
                        q.append((iy, ix))
                        check2[iy][ix] = True

                    elif earth[iy][ix] != 0 and earth[iy][ix] != nm:
                        if my_min > tm:
                            my_min = tm

N = int(input())
earth = [list(map(int, input().split())) for _ in range(N)]
# print(earth)

# 1. DFS로 만나는 땅에 숫자로 네임을 붙여준다.
check_visited = [[False]*N for _ in range(N)]
color = 0
for y in range(N):
    for x in range(N):
        if check_visited[y][x] == False and earth[y][x] == 1:
            color += 1
            check_visited, color = DFS(check_visited, color, y, x)

# print(check_visited, color)
# pprint(earth)


# 2. 섬을 체크해서 더이상 체크할 섬이 남아있지 않다면, color만큼의 섬이 있다는 것을 확인 할 수 있다.
names = [ x for x in range(1, color+1) ]
# print(names)

# 3. BFS를 이용해서 이동한다. 이동하면서 다른 섬을 만나면 최소값으로 업데이트 한다.

my_min = 9999999
for name in names:
    temp = 0
    check = [[False] * N for _ in range(N)] #visit를 어떤식으로 확인하느냐에 따라서 시간초과 해결
    for y in range(N):
        for x in range(N):
            if check[y][x] == False and earth[y][x] == name:
                check[y][x] == True
                BFS(y, x, name, temp)

print(my_min-1)