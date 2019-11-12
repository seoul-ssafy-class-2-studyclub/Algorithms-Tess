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
def solve(cand, nums):
    # 앞에 연산결과를 계속 가진채로 다음껄 한다.
    global mymin, mymax
    res = nums.pop(0)
    while cand:
        op = cand.popleft()
        after = nums.pop(0)
        if op == '+':
            res = res + after

        if op == '-':
            res = res - after

        if op == 'x':
            res = res * after

        if op == '/':
            try:
                res = int(res / after)
            except ZeroDivisionError:
                res = 0

    if res < mymin:
        mymin = res
    if res > mymax:
        mymax = res

for tc in range(1, T+1):
    N = int(input())
    numofOperators = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    # 중복순열 product
    ableOperators = []
    for idx in range(len(numofOperators)):
        for i in range(numofOperators[idx]):
            ableOperators.append(operators[idx])

    # 순열로 뽑음
    candidates = list(itertools.permutations(ableOperators, N-1))
    print(candidates)
    mymin = 100000001
    mymax = -100000001
    for candidate in candidates:
        solve(collections.deque(list(candidate)), numbers[:])
    result = abs(mymin-mymax)
    print(f'#{tc} {int(result)}')
