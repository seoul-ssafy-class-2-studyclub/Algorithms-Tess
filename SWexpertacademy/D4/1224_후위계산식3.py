'''
1. 열린 괄호 '(' 인 경우 stack에 추가
2. 숫자의 경우 바로 stack에 넣지않고 출력
3. + 의 경우, 연산 부호 이므로 stack에 추가
4. 닫힌 괄호 ')' 인 경우 열린 괄호가 나올때까지 pop하여 출력
5. * 의 경우 연산 부호 이므로 stack에 추가
6. 마찬가지로 열린 괄호가 나올때까지 pop한다.
7. 더이상 남아있지 않은 경우 모두 pop한다.

연산자 우선순위를 고려한다면 단순히 stack에 추가하는 것이 아니라
추가하기전에 자신의 우선순위보다 낮은 연산자일때까지 pop해주어야 한다.


1) 피연산자는 무조건 B배열로 이동시킨다.

2) 연산자는 스택에 저장한다. (괄호 또한 연산자로 취급한다.)
연산자를 스택에 저장하는 방식은 "괄호가 없는 중위 표기법"과 방식이 같다.
하지만, 다른 점은 여는 괄호가 어느 연산자보다도 우선순위가 낮다고 가정해야 한다.
만약, 닫는 괄호가 나타났다면 여는 괄호 이전까지의 모든 연산자들을 배열 B로 옮겨야 한다.
단, 여는 괄호와 닫는 괄호는 B 배열로 옮기지 않는다.

3. 피연산자를 B배열로 모두 옮겼다면, 스택에 저장된 연산자도 모두 B배열로 옮긴다.

이처럼
후위계산식을 만든 후,
만든 후위계산식을 토대로 계산한다.
'''

import sys
sys.stdin = open('1224.txt', 'r')

'''
#1 672676
#2 1974171
#3 12654
#4 38756
#5 4035
#6 155304
#7 6964
#8 2819
#9 24711
#10 208785
'''

# "34+56*+7+"
# '*', '/' # 이거 라면
# '+', '-'
operators = ['*', '/', '+', '-', '(', ')']
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

for tc in range(1,11):
    N = int(input())
    equation = list(map(str, input()))

    stack_A = []
    stack_A.append(equation[0])
    # result_B.append(equation[1])
    flag = True

    while stack_A:

        result_B = []

        for idx in range(1, N):
            if idx == N-1:
                for _ in range(len(stack_A)):
                    temp = stack_A.pop()
                    if temp != '(':
                        result_B.append(temp)

            if idx != N - 1:
                if equation[idx] not in operators:
                    result_B.append(equation[idx])

                elif equation[idx] in operators:
                    if equation[idx] == '(':
                        # '(' 나오면 무조건 들어간다.
                        stack_A.append(equation[idx])

                    elif equation[idx] == ')':
                        # '('가 나올때까지 pop
                        while True:
                            temp = stack_A.pop()
                            if temp == '(':
                                break
                            else:
                                result_B.append(temp)

                    # temp == '(': # 버림
                    # text들어올애 - icp를 보고 # stack - isp를 비교해서 크고 같냐를 비교
                    # icp가 더 크거나 같으면 쌓이면되고
                    # isp가 더 크면 stack의 -1을 icp보다 같거나 작아질때까지 pop
                    # 하고 append
                    # while해서 pop후 추가

                    elif icp[equation[idx]] >= isp[stack_A[-1]]:
                        stack_A.append(equation[idx])

                    elif icp[equation[idx]] < isp[stack_A[-1]]:
                        while icp[equation[idx]] < isp[stack_A[-1]]: # while안의 while 조건이 끝날때까지 진행
                            temp = stack_A.pop()
                            result_B.append(temp)
                        stack_A.append(equation[idx])


    ### 계산시작
    #print(result_B)

    number_stack = []

    number_stack.append(result_B[0])
    number_stack.append(result_B[1])

    cnt = 0
    res = 0
    for idx in range(2, len(result_B)):
        if result_B[idx] == "+":
            if len(number_stack) >= 2:
                num2 = int(number_stack.pop())
                num1 = int(number_stack.pop())
                cnt = num1 + num2
                number_stack.append(cnt)

        # elif result_B[idx] == "-":
        #     if len(number_stack) >= 2:
        #         num2 = int(number_stack.pop())
        #         num1 = int(number_stack.pop())
        #         cnt = num1 - num2
        #         number_stack.append(cnt)

        elif result_B[idx] == "*":
            if len(number_stack) >= 2:
                num2 = int(number_stack.pop())
                num1 = int(number_stack.pop())
                cnt = num1 * num2
                number_stack.append(cnt)

        # elif result_B[idx] == "/":
        #     if len(number_stack) >= 2:
        #         num2 = int(number_stack.pop())
        #         num1 = int(number_stack.pop())
        #         cnt = num1 / num2
        #         number_stack.append(cnt)

        else:
            number_stack.append(result_B[idx])

    print(f'#{tc}', number_stack[-1])




