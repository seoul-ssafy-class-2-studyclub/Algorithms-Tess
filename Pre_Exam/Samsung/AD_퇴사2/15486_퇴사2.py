import sys
# sys.stdin = open('15486.txt', 'r')
input = sys.stdin.readline

# 데이터가 크다
# 상담을 할지 안 할지를 보면서 연산 진행여부가 결정되기 때문에 효율적이다.
def DP():
    # N+1 될때까지 일을 할 수 있다.
    for idx in range(N-1, -1, -1): # 뒤로 가면서한다.
        xchildren = Ti[idx] + idx
        if xchildren > N:
            dp[idx] = dp[idx+1]
            continue # 앞의 if문 무시
        # 상담을 했을 때 수익 : Pi[idx] + dp[xchildren]
        # 상담을 안 했을 때 수익 : dp[idx+1]
        else:
            pivot = Pi[idx] + dp[xchildren]
            if pivot > dp[idx+1]: # 상담한다.
                dp[idx] = pivot
            elif pivot <= dp[idx+1]: # 상담 안 한다.
                dp[idx] = dp[idx+1]

N = int(input())
Ti = [0] * (N + 1)
Pi = [0] * (N + 1)
dp = [0] * (N + 1)
for i in range(N):
    ti, pi = map(int, input().split())
    Ti[i] = ti # 하루가 소요되므로 처음부터 데이터 전처리
    Pi[i] = pi
DP()
print(dp[0]) # 구한 값들 중의 최대 이익이므로 가장 큰 값을 출력해야한다.