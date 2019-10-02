import sys
sys.stdin = open('1952.txt', 'r')

# 1d 1m 3m 1y 각각의 값에 따라 dp에 적용시키면서 가장 min값을 가져오는 로직 구성
# 최종적으로 끌어온 값과 1y 값을 비교후 가장 작은 값 출력

# DP
def find(i):
    global mymin, dp
    if i == 12:
        return

    else:
        onedaypay = (plans[i] * oneday) # 0
        onemonthpay = onemonth # 40
        threemonthpay = threemonth

        temp = []
        if dp[i-1] >= onedaypay or onedaypay <= onemonthpay:
            ix = i + 1
            onedaypay = dp[i-1] + onedaypay
            temp.append((onedaypay, ix))

        if dp[i-1] >= onemonthpay or onedaypay > onemonthpay:
            ix = i + 1
            onemonthpay = dp[i - 1] + onemonthpay
            temp.append((onemonthpay, ix))

        # 앞이 0, 0, 0 인 경우를 고려해서 if조건 더 필요했음.
        if dp[i-3]+ dp[i-2]+ dp[i-1] >= threemonthpay or (onedaypay > threemonthpay or onemonthpay > threemonthpay):
            ix = i + 1
            threemonthpay = dp[i-3] + threemonthpay
            temp.append((threemonthpay, ix))

        temp = list(sorted(temp))
        dp[i] = temp[0][0]
        find(temp[0][1])

for tc in range(int(input())):
    oneday, onemonth, threemonth, mymin = map(int, input().split())
    plans = list(map(int,input().split()))
    dp = [0]*12 # dp를 위한 기본 리스트 준비
    res = find(0)
    print(f'#{tc+1}', min(dp[11], mymin))



