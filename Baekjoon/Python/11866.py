# 7 3
N, K = map(int, input().split())
stack = [i for i in range(1, N + 1)]
result = []
temp = K - 1
# 숫자를 담은 리스트(stack),
# 이를 지속적으로 도는 temp,
# 맞는 숫자를 pop하여 result에 넣는 식을 통해 간단하게 해결할 수 있다.
for i in range(N):
    if len(stack) > temp:
        result.append(stack.pop(temp))
        temp += K - 1
    elif len(stack) <= temp:
        temp = temp % len(stack)
        result.append(stack.pop(temp))
        temp += K - 1

print("<", end='')
for i in result:
    if i == result[-1]:
        print(i, end = '')
    else:
        print("%s, " %(i), end='')
print(">")