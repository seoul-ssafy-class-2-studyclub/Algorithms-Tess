'''
136
'''

import sys
sys.stdin = open('16637.txt', 'r')

'''
수식 길이: N
0 <= N

0~9 정수 + 연산자(+,-,*)
1. 연산자 우선순위는 모두 동일하다.
2. 중첩괄호는 안된다. 괄호로 감싸는 것에 대한 제한은 없다. 그리고 괄호 안에는 연산자가 하나만 들어있어야한다.
3. 괄호로 감싸지 않아도 된다.
괄호로 안감쌀때의 결과

랜덤으로 괄호가 감싸질때의 여러 결과

그 결과중에 가장 최대값은?
'''

'''
문제의 조건에 따라서 괄호를 씌울 수 있는 모든 경우를 나열
1+2는 괄호를 씌우나 마나 결과가 같다. 가장 앞에 위치하기 때문이다.
다음과 같이 5가지 경우가 존재한다.

3 + 8 * 7 - 9 * 2
3 + 8 * 7 - (9 * 2)
3 + 8 * (7 - 9) * 2
3 + (8 * 7) - 9 * 2
3 + (8 * 7) - (9 * 2)

함수를 두 번 재귀호출 하여 구현
1. 이전 계산 결과와 오른쪽에 있는 피연산자를 피연산자로 하여
    현재 가리키는 연산자의 연산을 수행하는 함수 
    (왼쪽부터 순서대로 계산하게 됨)

2. 이전 계산 결과와 오른쪽에 있는 연산자의 연산 수행 결과를 피연산자로 하여
    현재 가리키는 연산자의 연산을 수행하는 함수 
    
[재귀 탈출 조건]
연산자의 인덱스를 초과하여 현재 가리키는 연산자가 없는 경우
계산된 결과를 비교하여 최대값으로 업데이트하는 작업을 수행한 뒤 종료
'''


import sys
sys.setrecursionlimit(100000)

def calculate(a, b, op):

    ret = 0

    if op == '+':
        ret = a + b


    if op == '-':
        ret = a - b

    if op == '*':
        ret = a * b

    return ret



def solve(res, opidx):
    global result, numbers, operators

    if opidx >= No:
        if result < res:
            result = res
        return

    nowresult = calculate(res, numbers[opidx+1], operators[opidx])
    solve(nowresult, opidx + 1)

    if opidx + 2 < Nn:
        nextresult = calculate(numbers[opidx+1], numbers[opidx+2], operators[opidx+1])
        nowresult = calculate(res, nextresult, operators[opidx])
        solve(nowresult, opidx+2)

N = int(input())
data = list(input())
numbers = []
operators = []

for i in range(0, N, 2):
    # print(i)
    if i <= N-2:
        numbers.append(int(data[i]))
        operators.append(data[i+1])

    elif i == N-1:
        numbers.append(int(data[i]))

Nn = len(numbers)
No = len(operators)

# print(numbers)
# print(operators)
result = -9999999999 # 답이 음수로 나오는 경우를 고려해야한다.
solve(numbers[0], 0)

print(result)
