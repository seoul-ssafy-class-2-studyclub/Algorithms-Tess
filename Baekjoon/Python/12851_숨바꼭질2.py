from collections import deque
import sys
input = sys.stdin.readline

def solve(n):
    dictcheck = dict()
    q = deque([])
    q.append(n)
    t = -1
    time = 1e9
    path = 0
    flag = False
    while q:

        t += 1 # time을 달고 다닐 필요가 없다.
        for _ in range(len(q)):
            n = q.popleft()

            if t > time:
                continue

            if n == K and flag == False:
                time = t
                flag = True

            if n == K and flag == True:
                path += 1

            dictcheck[n] = n # 현재 상태는 동생이 없다고 판단이 된 상태이므로 다음으로 간다.

            next = [n-1, n+1, n*2]  # 뒤로 걷기, 앞으로 걷기, 순간이동
            for nxt in next:
                # 다음이 확인되지 않은 상태이므로 q에 들어간다.
                if 0 <= nxt <= 100000 and dictcheck.get(nxt) == None:
                    q.append(nxt)

    return time, path
    # t를 활용 해서 찾는데, t로 나한테 오는 경우의 수

N, K = map(int, input().split())
mymin = 1e9
path = 0
ansT, ansP = solve(N)
print(ansT)
print(ansP)
