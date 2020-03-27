import sys
# sys.stdin = open('input/16947.txt', 'r')

'''
2개의 지선: 철도·수로 따위의 본선에서 갈려 나간 선.
1개의 순환
'''

# 순환선 구하기
import collections
input = sys.stdin.readline
# maximum recursion은 **으로 설정해야 한다.
sys.setrecursionlimit(10**8)

def find(start, depth, vis, point):
    global fin, count
    if start == point and depth:
        if depth > 3:  # 2이상일때
            count[point] = 1
            for i in range(N):
                if vis[i] and count[i] != 1:
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
        q = collections.deque([])
        q.append((i, 1))
        while q:
            p, dis = q.popleft()
            for child in adj_list[p]:
                if finalvisit[child] == False and count[child] == 0:
                    finalvisit[child] = True
                    q.append((child, dis + 1))
                    result[child] = dis

print(' '.join(map(str, result)))
