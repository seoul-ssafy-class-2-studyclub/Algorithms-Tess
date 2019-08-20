import sys
sys.stdin = open('4866.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    string = list(input())

    temp = []
    for ix in string:
        if ix in ['{', '}', '(', ')']:
            temp.append(ix)

    stack = []
    for i in range(len(temp)):
        if '(' == temp[i] or '{' == temp[i]:
            stack.append(temp[i])
        elif ')' == temp[i] or '}' == temp[i]:
            if len(stack) == 0:
                stack.append(temp[i])
                break
            elif ('}' == temp[i] and '{' != stack[-1]) or (')' == temp[i] and '(' != stack[-1]):
                stack.append(temp[i])
                break
            else:
                stack.pop()

    if not len(stack):
        print(f'#{tc} 1')
    elif len(stack):
        print(f'#{tc} 0')


