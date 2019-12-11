'''짝홀 배열 만들어서 저장할 것'''
import collections
N, K = map(int, input().split())
import sys
input = sys.stdin.readline
def solve(n, k):
    # -1로 채워서 시작은 0으로, 해서 분간해준다.
    save = [[-1] * 500001 for _ in range(2)]
    save[0][n] = 0
    q = collections.deque([n])
    cnt = 0
    while q:
        if save[cnt%2][k] >= 0: #
            print(cnt)
            return

        cnt += 1 #  n과 k의 시간대를 맞춰줘서 움직이도록 한다.
        for _ in range(len(q)):
            n = q.popleft()
            idx = cnt % 2
            for fin in [(n + 1), (n - 1), (n * 2)]:
                if 0 <= fin <= 500000 and save[idx][fin] == -1:
                    save[idx][fin] = cnt + 1
                    q.append(fin)

        k += cnt
        if k > 500000: #
            print(-1)
            return

solve(N, K)


