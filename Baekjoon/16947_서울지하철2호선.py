import sys
# sys.stdin = open('16947.txt', 'r')

'''
2개의 지선: 철도·수로 따위의 본선에서 갈려 나간 선.
1개의 순환
'''

# 순환선 구하기
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10*7)

def find(start, depth, vis, point):
    global fin

    if start == point and depth:
        if depth >= 3:  # 2이상일때
            count[point] = 1
            for i in range(N):
                if vis[i]:
                    count[i] = 1
            fin = True
        return
    elif start != point:
        vis[start] = True
    for child in adj_list[start]:
        visit = vis[:]
        if visit[child] == False:
            find(child, depth + 1, visit, point)
    return


def getdistance(start):
    global finalvisit, result
    q = collections.deque([])
    q.append((start, 1))

    while q:
        p, dis = q.popleft()

        for child in adj_list[p]:
            if finalvisit[child] == False and count[child] == 0:
                finalvisit[child] = True
                result[child] = dis
                q.append((child, dis+1))


N = int(input())

count = [0]*N
adj_list = [[] for _ in range(N)]
for _ in range(N):
    s, e = map(int, input().split())
    e = e-1
    s = s-1
    adj_list[s].append(e)
    adj_list[e].append(s)

# 먼저 순환선이 뭔지 찾고,
for i in range(N):
    fin = False
    visit = [False] * N
    find(i, 0, visit, i)
    if fin == True:
        break

result = [0]*N
# 순환선이 아닌것들중 BFS를 해서 거리를 찾는다.
finalvisit = [False]*N
for i in range(N):
    if count[i] == 1:
        distance = getdistance(i)
print(' '.join(map(str, result)))
