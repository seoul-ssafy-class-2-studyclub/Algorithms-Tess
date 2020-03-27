'''
94
'''


import sys
sys.stdin = open('2812.txt', 'r')


# import sys
# input = sys.stdin.readline
N, K = map(int, input().split())
data = list(map(int, input()))
stack = []
stack.append(data[0])
data = data[1:]
for num in data:
    if stack[-1] >= num: # 1 > 9 stack의 가장 맨 뒤에 있는게 비교 대상인 것보다 크거나 같은 경우, 우리의 현재가 된다.
        stack.append(num)
        continue
    else: # 비교대상이 앞에있는 값보다 큰 경우,
        # 새로운 애가 current보다 클때는 current가 더 클때까지 while을 돌려야 한다
        # 그때까지 넣어야 한다.
        while len(stack) >= 1 and num > stack[-1] and K > 0:
            stack.pop()
            K -= 1
        stack.append(num)
if K: # K가 남아있다면, 그 뒤에꺼를 없애야 한다.
    idx = K*(-1)
    stack = stack[:idx]
print(''.join(map(str, stack)))






# import collections
#
# N, K = map(int, input().split())
# save = N-K
# data = list(map(int, input()))
# stack = collections.deque([])
# stack.append(data[0])
#
# data = data[1:]
# while K != 0:
#     current = stack[-1]
#     nxt = data.pop(0)
#
#     if current >= nxt: # 1 > 9
#         stack.append(nxt)
#
#     if nxt > current: # 새로운 애가 current보다 클때는 current가 더 클때까지 while을 돌려야 한다
#         # 그때까지 넣어야 한다.
#         while len(stack) >= 1 and nxt > stack[-1] and K != 0:
#             stack.pop()
#             K -= 1
#         stack.append(nxt)
#
#     if len(stack) > save:
#         break
#     # print(stack)
#
# # print(stack)
# if len(stack) > save:
#     print(''.join(map(str, stack[:save])))
# else:
#     print(''.join(map(str, stack)))


