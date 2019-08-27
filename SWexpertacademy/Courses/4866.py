import sys
sys.stdin = open('4866.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    string = list(input())

    temp = []
    for ix in string:
        if ix in ['{', '}', '(', ')']:
            temp.append(ix)
    print(temp) # 문장내의 {, }, (, ) 만 뽑아오기

    stack = []
    for i in range(len(temp)):
        if '(' == temp[i] or '{' == temp[i]:
            stack.append(temp[i])
        elif ')' == temp[i] or '}' == temp[i]:
            if len(stack) == 0:
                stack.append(temp[i])
                break
            elif (')' == temp[i] and '(' != stack[-1]) or ('}' == temp[i] and '{' != stack[-1]):
                stack.append(temp[i])
                break
            else:
                n = stack.pop()
                print(stack)

    if not len(stack): # 짝을 이뤘으면, []이므로, 0이 결과라서 1 출력
        print(f'#{tc} 1')
    elif len(stack): # 짝을 이루지못해서, 남아있으므로, 0 출력
        print(f'#{tc} 0')


