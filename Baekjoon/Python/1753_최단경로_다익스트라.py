import sys
sys.stdin = open('1753.txt', 'r')
# 우선순위큐
# 시간초과

input = sys.stdin.readline
'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''

# 정점, 간선 개수
V, E = map(int, input().split())

# 시작번호
K = int(input())

infinity = float('inf')
graph = {i: {} for i in range(1, V+1)}
costs = {}
processed = []
for idx in range(E):
    u, v, w = map(int, input().split()) # u에서 v로 가는 가중치 w인 간선이 존재

    if v not in graph[u]:
        graph[u][v] = w
    else:
        if graph[u][v] > w:
            graph[u][v] = w


    if v == K:
        costs[v] = 0
    else:
        costs[v] = infinity

def find_lowest_cost_node(costs):
   lowest_cost = float('inf')
   lowest_cost_node = None # None으로 초기화해주어야 return값이 None이 나옴
   for node in costs:
       cost = costs[node]
       if cost < lowest_cost and node not in processed:
           lowest_cost = cost
           lowest_cost_node = node
   return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
   cost = costs[node]
   neighbors = graph.get(node)
   if neighbors != None:
       for n in neighbors.keys():
           new_cost = cost + neighbors[n]
           if costs[n] > new_cost:
               costs[n] = new_cost # 최소 costs를 업데이트
   processed.append(node)
   node = find_lowest_cost_node(costs)

res = [x for x in range(1, V+1)]

for i in res:
    res = costs.get(i)
    if res == None:
        print('INF')
    else:
        print(res)