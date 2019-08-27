'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX


#1 1
#2 4
#3 11
'''

import sys
sys.stdin = open('4873input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    text = list(input())

    stack = []

    for idx in range(len(text)):
        # 스택이 비어있거나 스택 마지막 값이 현재 처리할 값과 다르면 저장
        # 값이 없으면 거짓
        if not stack or stack[-1] != text[idx]:
            stack.append(text[idx])

        elif stack and stack[-1] == text[idx]:
            stack.pop()

    print(f'#{tc}', len(stack))
