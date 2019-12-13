import sys
sys.stdin = open('2252.txt', 'r')
import collections

N, M = map(int, input().split())
inDegree = [0]*(N+1)
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    inDegree[e] += 1
    adj_list[s].append(e)

q = collections.deque([])
for idx in range(1, N+1):
    if inDegree[idx] == 0:
        q.append(idx)

res = []
while q:
    for _ in range(len(q)):
        p = q.popleft()
        res.append(p)
        for c in adj_list[p]:
            inDegree[c] -= 1
            if inDegree[c] == 0:
                q.append(c)

print(' '.join(map(str,res)))
