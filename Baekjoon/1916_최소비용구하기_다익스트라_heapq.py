import sys
input = sys.stdin.readline
import heapq
'''
4
'''

# 도시의 개수
N = int(input())
# 버스의 개수
M = int(input())

# N개의 도시를 가는 부모와 이웃(자식, 가중치)을 그리는 그래프
graph = {i: [] for i in range(1, N + 1)}

# M개의
# 버스의 출발 도시의 번호 busN, 도착지의 도시 번호 goalN, 버스 비용 busCost
for _ in range(M):
    busN, goalN, busCost = map(int, input().split())
    graph[busN].append((goalN, busCost))

start, goal = map(int, input().split())

infinity = float('inf')
# print(start, goal)
# print(graph)

check = {i: infinity for i in range(1, N + 1)}
check[start] = 0


pq = []
heapq.heappush(pq, (0, start))
# 우선순위 큐를 활용
while pq:
    w, now = heapq.heappop(pq)
    # 만약 지금까지 합해진 길이보다 기록된 길이가 짧으면 스킵
    if check[now] < w:
        continue

    for i, w in graph[now]:
        # 지금까지 기록된거 + 앞으로 진행할것이 이미 기록되어있는것보다 적으면
        nc = w + check[now]
        if nc < check[i]:
            check[i] = nc
            # 새로이 큐에 추가
            heapq.heappush(pq, (nc, i))

print(check[goal])