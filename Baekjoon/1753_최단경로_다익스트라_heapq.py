import sys
sys.stdin = open('1753.txt', 'r')
input = sys.stdin.readline
# import queue as Q
# n, m = map(int, input().split())
# start = int(input())
#
# adj = [[] for i in range(n + 1)]
# DIST = [1e9] * (n + 1)
#
#
# def dijkstra(src):
#     q = Q.PriorityQueue()
#     q.put((0, src))
#     DIST[src] = 0
#
#     while not q.empty():
#         pp = q.get()
#         here = pp[1]
#         dist = pp[0]
#
#         if DIST[here] < dist:
#             continue
#
#         for i in adj[here]:
#             cost = dist + i[1]
#             if DIST[i[0]] > cost:
#                 DIST[i[0]] = cost
#                 q.put((cost, i[0]))
#
#
# while m:
#     m -= 1
#     a, b, c = map(int, input().split())
#     adj[a].append((b, c))
#
# dijkstra(start)
#
# for i in range(1, n + 1):
#     if DIST[i] is 1e9:
#         print("INF")
#     else:
#         print(DIST[i])

'''
힙큐 = 우선순위큐
넣을때 우선순위에 맞춰서 정렬해서 넣음
뺄때 우선순위에 맞춰서 가장 높은애를 
우선순위-> [0, 1] *앞의 원소를 기준으로 함

최소힙
최대힙

파이썬은 최소힙을 기준으로 우선순위 큐가 생긴다.

정렬시 이진트리로 정렬되는데,
한 노드에서 다른노드로 가는 간선의 수가 0~2개인 트리
3개가 되는순간 그냥 트리가 된다는 말

heapq.heappush(큐, [들어갈원소])
heapq.heappop()

다익스트라 알고리즘
최소비용

[누비용, 현재번호]
누적비용이 낮은 것부터 보면서 교체
'''


import heapq
 
V, E = map(int, input().split(' '))
 
K = int(input())
 
graph = {i: [] for i in range(1, V + 1)}
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
print(graph)

# 무한대를 이렇게 구현해보았다.
# 무한대는 어차피 다른 모든 숫자와 교환된다.
check = {i: 'INF' for i in range(1, V + 1)}
check[K] = 0 # 시작점은 항상 결과가 0이다.


pq = []
heapq.heappush(pq, (0, K))
# 우선순위 큐를 활용
while pq:
    w, now = heapq.heappop(pq)

    # 만약 지금까지 합해진 길이보다 기록된 길이가 짧으면 스킵
    if check[now] is not 'INF' or check[now] < w:
        continue

    for i, w in graph[now]:
        # 지금까지 기록된거 + 앞으로 진행할것이 이미 기록되어있는것보다 적으면
        nc = w + check[now]
        if check[i] is 'INF' or nc < check[i]:
            check[i] = nc
            # 새로이 큐에 추가
            heapq.heappush(pq, (nc, i))

print(check)
for i in range(1, V + 1):
    print(check[i])


'''
https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%81%AC%EC%8A%A4%ED%8A%B8%EB%9D%BC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
'''