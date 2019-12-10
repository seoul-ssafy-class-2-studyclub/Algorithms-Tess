##### 고쳐야한다.
import heapq

N, K = map(int, input().split())


def solve(N):
    dictcheck = dict()
    q = []
    heapq.heappush(q, (0, N))
    while q:
        for _ in range(len(q)):

            cnt, n = heapq.heappop(q)

            if n == -1:
                continue

            if n == K:
                return cnt
            dictcheck[n] = 1

            # 수빈
            count = [(n + 1), (n - 1), (n * 2)]
            for fin in count:
                if 0 <= fin  <= 500000 and dictcheck.get(fin ) == None:
                    dictcheck[fin ] = 1
                    heapq.heappush(q, (cnt + 1, fin))
                if fin > 500000:
                    dictcheck[fin ] = 1
                    heapq.heappush(q, (cnt+1, -1))

        for _ in range(len(q)):

            cnt, n = heapq.heappop(q)

            if n == -1:
                continue

            if n == K:
                return cnt
            dictcheck[n] = 1

            # 동생: 가속도가 붙는다
            count = [(n + 1, cnt), (n - 1, cnt), (n * 2, cnt)]
            for fin, time in count:
                if 0 <= fin + time <= 500000 and dictcheck.get(fin + time) == None:
                    dictcheck[fin + time] = 1
                    heapq.heappush(q, (cnt + 1, fin + time))
                if fin + time > 500000:
                    dictcheck[fin + time] = 1
                    heapq.heappush(q, (cnt+1, -1))
    return -1

print(solve(N))
