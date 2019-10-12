import sys
sys.stdin = open('16000.txt', 'r')
import collections
input = sys.stdin.readline

def find(y, x, named):
    global earth, landname, firstvisited
    q = collections.deque([])
    q.append((y, x))
    firstvisited[y][x] = True
    earth[y][x] = named
    while q:
        y, x = q.popleft()
        for dy, dx in [(0,1), (0,-1), (1, 0), (-1, 0)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < M and firstvisited[iy][ix] == False and earth[iy][ix] == '#':
                firstvisited[iy][ix] = True
                q.append((iy, ix))
                earth[iy][ix] = named

def secondfind(y, x, stop):
    global earth
    tempvisit = [ [False]*M for _ in range(N) ]
    q = collections.deque([])
    q.append((y, x))
    forreturn = []
    while q:
        y, x = q.popleft()
        for dy, dx in [(0,1), (0,-1), (1, 0), (-1, 0)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < M and tempvisit[iy][ix] == False:
                if earth[iy][ix] == '.':
                    tempvisit[iy][ix] = True
                    q.append((iy, ix))
                if earth[iy][ix] != stop and earth[iy][ix] != '.':
                    forreturn.append(earth[iy][ix])
    return forreturn

def getinfo(start):
    global earth
    mychildren = set()
    used = [ [False]*M for _ in range(N) ]
    for i in range(N):
        for j in range(M):
            if earth[i][j] == start and used[i][j] == False:
                used[i][j] = True
                info = secondfind(i, j, start)
                mychildren.update(info)
    return list(mychildren)

N, M = map(int, input().split())

# 최외곽을 -2로 바꾼다. -> 우리들의 도착점이다.
earth = [ list(input()) for _ in range(N) ]
final = [i[:] for i  in earth]

landname = [0]
firstvisited = [ [False]*M for _ in range(N) ]
name = 0
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0 or i == N-1 or j == M-1:
            earth[i][j] = 0

        if earth[i][j] == '#':
            name += 1
            landname.append(name)
            find(i, j, name)

adj_list = [ [] for i in range(name+1)]
for one in landname:
    children = getinfo(one)
    adj_list[one].extend(children)
# print(adj_list)
safe = [False] * (name+1)
for i in range(name+1):
    # print(i)
    if 0 in adj_list[i]:
        safe[i] = True
for i in range(name+1):
    if safe[i]:
        continue
    for j in range(name+1):
        if i == j:
            continue
        vis = [False] * (name+1)
        stack = collections.deque([])
        stack.extend(adj_list[i])
        flag = True
        while stack:
            node = stack.pop()
            if node == 0:
                flag = False
                break
            if not vis[node] and node != j:
                vis[node] = True
                stack.extend(adj_list[node])
        if flag:
            break
    if not flag:
        safe[i] = True
for r in range(N):
    for c in range(M):
        if earth[r][c] == '.':
            continue
        island = earth[r][c]
        if island == 0:
            earth[r][c] = '.'
        elif safe[island]:
            earth[r][c] = '0'
        else:
            earth[r][c] = 'X'

for r in range(N):
    print(''.join(earth[r]))