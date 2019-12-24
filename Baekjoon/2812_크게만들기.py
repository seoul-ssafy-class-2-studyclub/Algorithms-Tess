'''
94
'''


import sys
sys.stdin = open('2812.txt', 'r')


'''분할정복'''


N, K = map(int, input().split())
save = N-K
data = list(input())
data = list(map(int, data))
stack = []
stack.append(data[0])

data = data[1:]
while K != 0:
    current = stack[-1]
    nxt = data.pop(0)

    if current >= nxt: # 1 > 9
        stack.append(nxt)

    if nxt > current: # 새로운 애가 current보다 클때는 current가 더 클때까지 while을 돌려야 한다
        # 그때까지 넣어야 한다.
        while len(stack) >= 1 and nxt > stack[-1] and K != 0:
            stack.pop()
            K -= 1
        stack.append(nxt)

    if len(stack) > save:
        break
    # print(stack)

# print(stack)
if len(stack) > save:
    print(''.join(map(str, stack[:save+1])))
else:
    print(''.join(map(str, stack)))


