import sys
sys.stdin = open('14889.txt', 'r')

def solve(k, s):
    global ans
    if k == R:
        start = link = 0
        x = list(set([x for x in range(N)]) - set(t))
        # print(t, x)

        for i in range(R-1):
            for j in range(i + 1, R):
                start += (mat[t[i]][t[j]] + mat[t[j]][t[i]])
        for i in range(R-1):
            for j in range(i + 1, R):
                link += (mat[x[i]][x[j]] + mat[x[j]][x[i]])
        ans = min(ans, abs(start - link))
    else:
        # N이 6일때 N//2개의 조합을 구한다.
        # 확실히 이해하기
        # 0, 6+(0-3)+1
        # 0 부터 4까지 0, 1, 2, 3까지 돈다.
        for i in range(s, N+(k-R)+1):
            # t[0]에 0을 넣고 다음으로..
            t[k] = i
            solve(k + 1, i + 1)

N = int(input())
R = N//2
t = [0] * R
# N이 6일때 R은 3이므로 t는 [0,0,0]을 가진다.
mat = [list(map(int, input().split())) for _ in range(N)]
ans = 1e9
solve(0, 0)
print(ans)

#
# def solve(k, s):
#     global ans
#     if k == R:
#         start = link = 0
#
#         x = list(set([x for x in range(N)]) - set(t))
#
#         for i in range(R - 1):
#             for j in range(i + 1, R):
#                 start += (mat[t[i]][t[j]] + mat[t[j]][t[i]])
#         for i in range(R - 1):
#             for j in range(i + 1, R):
#                 link += (mat[x[i]][x[j]] + mat[x[j]][x[i]])
#
#         ans = min(ans, abs(start - link))
#
#     else:
#         for i in range(s, N + (k - R) + 1):
#             t[k] = i
#             solve(k + 1, i + 1)
#
#
# N = int(input())
# R = N // 2
# t = [0] * R
# mat = [list(map(int, input().split())) for _ in range(N)]
#
# ans = 1e9
# solve(0, 0)
#
# print(ans)
