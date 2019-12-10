import sys
input = sys.stdin.readline
# 가장 짧은 시간만 걸리는 걸 빼와야 하기때문에 힙큐를 사용한다.
import heapq

# 바깥에 숫자를 cnt별로 저장해두면 어떨까?
'''
이동 경로를 저장할 path 배열을 만든다.
path[다음 좌표] = (현재 좌표) 방식으로 path 배열을 저장한다.
K에 도착하면, path 배열을 K부터 시작해서 N까지 역순으로 출력한다.
'''

def solve(n):
    global ans, pathcheck
    dictcheck = dict()
    pathcheck = dict()
    ans = [0] * 100001
    q = []
    heapq.heappush(q,(0, n))
    ans[0] = (n, 0)
    while q:
        # time을 달고 다닐 필요가 없다.
        for _ in range(len(q)):
            t, n = heapq.heappop(q)

            if n == K:
                ans = []
                while n != N: # 수빈의 위치가 아닐때까지
                    ans.append(n)
                    n = pathcheck[n] # n 부터 가면서 n이 가리키는 다음 값을 찾아가면된다. 17이 가르키는거..
                ans.append(N)
                ans.reverse()
                return t, ans

            dictcheck[n] = 1 # 현재 상태는 동생이 없다고 판단이 된 상태이므로 다음으로 간다.

            next = [(n-1), (n+1), (n*2)]  # 뒤로 걷기, 앞으로 걷기, 순간이동
            for nxt in next: # linkedlist형태
                # 다음이 확인되지 않은 상태이므로 q에 들어간다.
                if 0 <= nxt <= 100000 and dictcheck.get(nxt) == None:
                    pathcheck[nxt] = n # pathcheck에는 키값에는 nxt 그리고 값은 nxt를 가기 위해 다가온 것
                    dictcheck[nxt] = 1 # dictcheck에는 키값에는 nxt 그리고 값은 존재한다를 확인하기 위함
                    heapq.heappush(q, (t+1, nxt))

N, K = map(int, input().split())
mymin = 1e9

dist = [0]*100001
ansT, path = solve(N)
print(ansT)
print(' '.join(list(map(str, path))))