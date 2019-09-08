import sys
sys.stdin = open('14501.txt', 'r')

# 최대값을 도출하는 문제
# 모든 경우를 조사하라고 하면 어떤 경우를 조사하라는 거지? 라는 생각으로 해야한다.
# 경우의 수가 부분 집합임을 알아야 한다.



def solve(k):
    global ans
    if k == N:
        for i in range(N):
            if Si[i]:
                for j in range(i + 1, i + Ti[i]):
                    if j >= N or Si[j] : return

        tsum = 0
        for i in range(N):
            if Si[i]:
                tsum += Pi[i]
        if tsum > ans : ans = tsum

    else:
        Si[k] = 1
        solve(k + 1)
        Si[k] = 0
        solve(k + 1)

N = int(input())

Ti = [0] * N
Pi = [0] * N
Si = [0] * N

for i in range(N):
    Ti[i], Pi[i] = map(int, input().split())


ans = 0
solve(0)

print(ans)







# def solve(k, s):
#     global ans
#     if k == N:
#         ans = max(ans, s)
#         return
#
#     if(k + Ti[k] <= N):
#         solve(k + Ti[k], s + Pi[k])
#
#     solve(k + 1, s)
#
# N = int(input())
#
# Ti = [0] * N
# Pi = [0] * N
#
# for i in range(N):
#     Ti[i], Pi[i] = map(int, input().split())
#
# ans = 0
# solve(0, 0)
#
# print(ans)
