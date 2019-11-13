'''
#1 24
#2 8
#3 144
#4 8
#5 91
#6 150
#7 198
#8 2160
#9 46652
#10 701696
'''

import sys

sys.stdin = open('4008.txt', 'r')
import itertools

operators = ['+', '-', 'x', '/']
import collections

# 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
# 가장 작은 값 - 가장 큰 값의 차이
# 숫자 -1 만큼의 연산자 카드가 사용될것이고, 모든 연산자 카드가 사용되어있어야 한다.

T = int(input())


def solve(cand, K):
    # 앞에 연산결과를 계속 가진채로 다음껄 한다.
    global mymin, mymax, operators

    if K == N-1:
        if cand < mymin:
            mymin = cand
        if cand > mymax:
            mymax = cand
        return


    for i in range(4):
        if numofOperators[i]: # 0이 아니라면
            numofOperators[i] -= 1
            if operators[i] == '+':
                solve(cand + numbers[K+1],K+1)

            elif operators[i] == '-':
                solve(cand - numbers[K+1],K+1)

            elif operators[i] == 'x':
                solve(int(cand * numbers[K+1]), K+1)

            elif operators[i] == '/':
                try:
                    solve(int(cand / numbers[K+1]),K+1)
                except ZeroDivisionError:
                    solve(0,K+1)
            numofOperators[i] += 1



for tc in range(1, T + 1):
    N = int(input())
    numofOperators = list(map(int, input().split()))
    # [2, 1, 0, 1]

    numbers = list(map(int, input().split()))
    N = len(numbers)

    mymin = 100000001
    mymax = -100000001
    # for idx in range(len(numbers)): # 불필요
    solve(numbers[0], 0)
    result = abs(mymin - mymax)
    print(f'#{tc} {int(result)}')

# '''
# #1 24
# #2 8
# #3 144
# #4 8
# #5 91
# #6 150
# #7 198
# #8 2160
# #9 46652
# #10 701696
# '''
#
# import sys
# sys.stdin = open('4008.txt', 'r')
# import itertools
# operators = ['+', '-', 'x', '/']
# import collections
# # 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
# # 가장 작은 값 - 가장 큰 값의 차이
# # 숫자 -1 만큼의 연산자 카드가 사용될것이고, 모든 연산자 카드가 사용되어있어야 한다.
#
# T = int(input())
# def solve(cand, nums):
#     # 앞에 연산결과를 계속 가진채로 다음껄 한다.
#     global mymin, mymax
#     res = nums.pop(0)
#     while cand:
#         op = cand.popleft()
#         after = nums.pop(0)
#         if op == '+':
#             res = res + after
#
#         if op == '-':
#             res = res - after
#
#         if op == 'x':
#             res = res * after
#
#         if op == '/':
#             try:
#                 res = int(res / after)
#             except ZeroDivisionError:
#                 res = 0
#
#     if res < mymin:
#         mymin = res
#     if res > mymax:
#         mymax = res
#
# for tc in range(1, T+1):
#     N = int(input())
#     numofOperators = list(map(int,input().split()))
#     # [2, 1, 0, 1]
#
#     numbers = list(map(int,input().split()))
#
#     ableOperators = []
#     for idx in range(len(numofOperators)):
#         for i in range(numofOperators[idx]):
#             ableOperators.append(operators[idx])
#
#     # 순열로 뽑음
#     # 다른식으로 하세요.
#
#     candidates = list(itertools.permutations(ableOperators, N-1))
#     print(candidates)
#     mymin = 100000001
#     mymax = -100000001
#     for candidate in candidates:
#         solve(collections.deque(list(candidate)), numbers[:])
#     result = abs(mymin-mymax)
#     print(f'#{tc} {int(result)}')
