
'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''




N, K = map(int, input().split())
data = []
for _ in range(N):
    data += [int(input())]

i = 0
if K != 0:
    for idx in range(len(data)-1, -1, -1):
        coin = data[idx]
        t = K//coin # 각 코인별로 ki를 나눈 값
        i += t
        K = K - (coin*t)
        if K == 0:
            break
print(i)
