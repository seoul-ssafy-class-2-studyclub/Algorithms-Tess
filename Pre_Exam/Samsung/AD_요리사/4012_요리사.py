import sys
sys.stdin = open('4012.txt', 'r')

def solve(k, s):
    global ans
    if k == R:
        start = link = 0
        x = list(set([x for x in range(N)]) - set(t))
        print(t)
        for i in range(R-1):
            for j in range(i + 1, R):
                print(i, j)
                start += (mat[t[i]][t[j]] + mat[t[j]][t[i]])
        for i in range(R-1):
            for j in range(i + 1, R):
                link += (mat[x[i]][x[j]] + mat[x[j]][x[i]])
        ans = min(ans, abs(start - link))
    else:
        # N이 6일때 N//2개의 조합을 구한다.
        # 확실히 이해하기
        for i in range(s, N+(k-R)+1):
            t[k] = i
            solve(k + 1, i + 1)

T = int(input())
for tc in range(0, 1):
    N = int(input())
    R = N//2
    t = [0] * R
    mat = [list(map(int, input().split())) for _ in range(N)]
    ans = 1e9
    solve(0, 0)
    print(f'#{tc} {ans}')