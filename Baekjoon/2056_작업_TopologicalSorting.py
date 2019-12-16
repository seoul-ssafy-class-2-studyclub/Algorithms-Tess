''' 최대 힙(높은 값이 앞으로, 뒤로 갈수록 작게)
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1
'''
import sys
sys.stdin = open('2056.txt', 'r')
import heapq

N = int(input())
inDegree = [0] * (N+1)
times = dict()
adj_list = [[] for _ in range(N+1)]
counting = [0] * (N+1)
for idx in range(1, N+1):
    data = list(map(int, input().split()))
    times[idx] = data[0]
    inDegree[idx] += data[1]
    if data[1]:
        for p in data[2:]:
            adj_list[p].append(idx)
q = []
for idx in range(1, N+1):
    if inDegree[idx] == 0:
        heapq.heappush(q, (times[idx], idx))
        counting[1] = times[idx]

while q:
    for _ in range(len(q)):
        time, p = heapq.heappop(q)

        for c in adj_list[p]:
            inDegree[c] -= 1

            if inDegree[c] == 0:
                counting[c] = time
                counting[c] += times[c]
                heapq.heappush(q, (time+times[c], c))
print(counting)
print(max(counting))
