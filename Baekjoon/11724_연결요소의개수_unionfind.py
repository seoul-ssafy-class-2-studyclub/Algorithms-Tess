import sys
sys.stdin = open('11724.txt', 'r')
'''
무방향그래프의 연결요소 개수 출력
연결요소란
원그래프 G 가운데 노드와 엣지가 서로 겹치지 않는 부그래프이되, 부그래프 내 모든 노드쌍에 대해 경로가 존재하는 걸 가리킵니다. 

'''


''' for문에 실행될 원소가 없는 경우 cnt도 더해지지 않는다.
visited = [False]*100
cnt = 0
a = []
for i in a:
    print('---', i)
    print('----for문 안에 있어요-----')
    cnt += 1
    if visited[a] == False:
        visited = True
print(visited)
print('---------')
print(cnt)
'''

### dfs-bfs 풀이
# DFS 나 BFS로 정말 빠르게 풀이 할 수 있을 것이라 생각했다. 방문표시하여 O(V+E)로 풀이할 수 있다.
# 모든 인접한 정점들을 세어주고, 이때 시작정점은 무향그래프이기에 상관이 없다. 대신 모든 정점이 방문표시가 되어야 한다.
# 정점을 한번 방문할 때마다 CC 개수를 +1 한다. 그리고 인접한 모든 정점을 방문하며, 방문하였다면 방문표시를 하며 누적한다.

def dfs(v): # 한 번 False로 정점이 시작되면,
    visited[v] = True

    for e in adj_list[v]:
        if visited[e] == False:
            dfs(e)

N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())

    adj_list[u].append(v)
    adj_list[v].append(u)

cnt = 0
visited = [False]*(N+1)
for idx in range(1, len(visited)): # 0을 건너뛴다. 연속적으로 1부터 6까지 검사를 진행하고, False인 경우에만 함수에 들어간다.
    if visited[idx] == False:
        cnt += 1
        dfs(idx)
print(cnt)

### union-find풀이
# 모든 연결되어 있는 정점들을 방문해주면서 한 Connected Component (이하 CC)을 모두 방문이 완료되면 해당 CC에 속한 정점들은 모두 방문했기에 나중에 다시 방문하지 않으며, 이때마다 CC 개수를 +1 하면서 풀 수 있다.