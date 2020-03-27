import sys
sys.stdin = open('1516.txt', 'r')

import heapq

N = int(input())
res = [0]*(N+1)
times = dict()
adj_list = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for child in range(1, N+1):
    data = list(input().split())
    # 소요시간
    times[child] = int(data[0])
    data = list(map(int, data[1:-1]))

    # 진입차수 :: 길이는 곧 선행되어야 할 건물의 수를 의미한다.
    indegree[child] += len(data)

    # 인접리스트 :: data의 정보가 곧 부모를 의미하므로, 다음과 같이 생성해야 한다.
    for idx in data:
        adj_list[idx].append(child)
q = []
for s in range(1, N+1):
    if indegree[s] == 0:
        heapq.heappush(q, (times[s], s))

while q:
    for _ in range(len(q)):
        cnt, s = heapq.heappop(q)
        res[s] = cnt
        for c in adj_list[s]:
            indegree[c] -= 1
            if indegree[c] == 0:
                heapq.heappush(q, (cnt+times[c], c))

print('\n'.join(map(str,res[1:])))


