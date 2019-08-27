'''
#1 84
#2 error
#3 168
'''

import sys
sys.stdin = open('4874.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    text = list(map(str, input().split()))

    number_stack = []
    # operator_stack = []

    number_stack.append(text[0])
    number_stack.append(text[1])

    cnt = 0
    res = 0
    for idx in range(2, len(text)):
        if text[idx] == ".":
            if len(number_stack) == 1:
                res = number_stack.pop()
                break
            if len(number_stack) >= 2:
                res = 'error'
                break

        elif text[idx] == "+":
            if len(number_stack) >= 2:
                num2 = int(number_stack.pop())
                num1 = int(number_stack.pop())
                cnt = num1 + num2
                number_stack.append(cnt)
            else:
                res = 'error'
                break

        elif text[idx] == "-":
            if len(number_stack) >= 2:
                num2 = int(number_stack.pop())
                num1 = int(number_stack.pop())
                cnt = num1 - num2
                number_stack.append(cnt)
            else:
                res = 'error'
                break

        elif text[idx] == "*":
            if len(number_stack) >= 2:
                num2 = int(number_stack.pop())
                num1 = int(number_stack.pop())
                cnt = num1 * num2
                number_stack.append(cnt)
            else:
                res = 'error'
                break

        elif text[idx] == "/":
            try:
                if len(number_stack) >= 2:
                    num2 = int(number_stack.pop())
                    num1 = int(number_stack.pop())
                    cnt = num1 // num2
                    number_stack.append(cnt)
                else:
                    res = 'error'
                    break
            except ZeroDivisionError:
                res = 'error'
                break

        else:
            number_stack.append(text[idx])
    print(f'#{tc}', res)







