operators = ['*', '/', '+', '-', '(', ')']
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

for tc in range(1,11):
    N = int(input())
    equation = list(map(str, input()))

    stack_A = []
    stack_A.append(equation[0])
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
                        stack_A.append(equation[idx])

                    elif equation[idx] == ')':
                        while True:
                            temp = stack_A.pop()
                            if temp == '(':
                                break
                            else:
                                result_B.append(temp)

                    elif icp[equation[idx]] >= isp[stack_A[-1]]:
                        stack_A.append(equation[idx])

                    elif icp[equation[idx]] < isp[stack_A[-1]]:
                        while icp[equation[idx]] < isp[stack_A[-1]]:
                            temp = stack_A.pop()
                            result_B.append(temp)
                        stack_A.append(equation[idx])
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

        elif result_B[idx] == "*":
            if len(number_stack) >= 2:
                num2 = int(number_stack.pop())
                num1 = int(number_stack.pop())
                cnt = num1 * num2
                number_stack.append(cnt)

        else:
            number_stack.append(result_B[idx])

    print(f'#{tc}', number_stack[-1])

