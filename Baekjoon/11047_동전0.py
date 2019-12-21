
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
Ki = K
data = []
for _ in range(N):
    data += [int(input())]

temp = [1e9]*10
i = 0
while Ki != 0:
    i = 0

    for idx in range(len(data)):

        t = Ki//data[-idx]
        if t == 0:
            continue

        elif 1 <= t and t < temp[i]:
            temp[i] = t

        if idx == len(data)-1:
            Ki = data[i]
            i += 1
print(temp)
