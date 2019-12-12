num = [8,2,0]
k = 3

# 시간복갑도 실패
N = len(num)
while k:
    idx = N - 1
    for jdx in range(N-2, -1, -1):
        # print(num[jdx], num[idx])
        num[idx], num[jdx] = num[jdx], num[idx]
        idx -= 1
    k -= 1
print(num)


# 그냥 원래 생각한 slicing 하자.
k %= len(num)
print(k%len(num)) # k를 len(num)으로 나눈 나머지 3%0 만큼을 잘라서 붙여준다.
num[k:], num[:k] = num[:-k], num[-k:]