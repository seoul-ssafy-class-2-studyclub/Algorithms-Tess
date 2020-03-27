import sys
input = sys.stdin.readline
# 가장 짧은 시간만 걸리는 걸 빼와야 하기때문에 힙큐를 사용한다.
import heapq

def solve(n):
    dictcheck = dict()
    q = []
    heapq.heappush(q,(0,n))
    while q:

        # time을 달고 다닐 필요가 없다.
        for _ in range(len(q)):
            t, n = heapq.heappop(q)

            if n == K:
                return t

            dictcheck[n] = n # 현재 상태는 동생이 없다고 판단이 된 상태이므로 다음으로 간다.

            next = [(n-1, 1), (n+1, 1), (n*2, 0)]  # 뒤로 걷기, 앞으로 걷기, 순간이동
            for nxt, ti in next:
                # 다음이 확인되지 않은 상태이므로 q에 들어간다.
                if 0 <= nxt <= 100000 and dictcheck.get(nxt) == None:
                    heapq.heappush(q, (t+ti, nxt))

N, K = map(int, input().split())
mymin = 1e9
path = 0
ansT = solve(N)
print(ansT)

