#5 17

from collections import deque
import sys
input = sys.stdin.readline

def solve(n):
    dictcheck = dict()
    q = deque([])
    q.append(n)
    t = 0

    while q:

        t += 1 # time을 달고 다닐 필요가 없다.
        for _ in range(len(q)):
            n = q.popleft()

            if n == K:
                return t

            next = [n-1, n+1, n*2]  # 뒤로 걷기, 앞으로 걷기, 순간이동
            for nxt in next:
                if 0 <= nxt <= 100000 and dictcheck.get(nxt) == None:
                    dictcheck[nxt] = nxt
                    q.append(nxt)

N, K = map(int, input().split())
mymin = 1e9
print(solve(N)-1)

