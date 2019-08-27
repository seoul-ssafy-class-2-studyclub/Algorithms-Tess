'''
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())


#1 1
#2 1
#3 0
'''



import sys
sys.stdin = open('stack.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    text = input() # 문장 읽기
    stack = []

    for i in range(len(text)): # 길이만큼 반복한다.
        # 짝이 맞는 지만 검사
        if text[i] == "(" or text[i] == "{":
            stack.append(text[i])

        elif text[i] == ")" or text[i] == "}":
            if len(stack) == 0: # 닫는 괄호가 제일 처음나오는 예외 처리
                # stack.append(text[i])
                break # 잘못된 경우 발견시 종료
            elif (text[i] == ")" and stack[-1] != "(") or (text[i] == "}" and stack[-1] != "{"):
                # stack.append(text[i]) # 잘못된 경우 발견시 종료
                break
            else:
                stack.pop() # 짝이 발견되면 빼낸다.
    # 문장검사 종료
    if len(stack) == 0: # 비어있으므로 모든게 짝을 찾아 나갔다.
        print(f'#{tc}', 1)
    elif len(stack) > 0:
        print(f'#{tc}', 0)


