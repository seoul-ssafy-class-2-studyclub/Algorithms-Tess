import sys
sys.stdin = open('4873.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#     characters = list(input())
#     stack = []
#
#     for i in range(len(characters)):
#         # stack = [] 거나, stack의 마지막 값이 characters[i]과 다르다면,
#         if not stack or stack[-1] != characters[i]:
#             stack.append(characters[i])
#
#         # if가 실행안되는 경우, 다음을 실행
#         # stack = [data] 거나, stack의 마지막 값이 characters[i]와 같다면,
#         elif stack and stack[-1] == characters[i]:
#             stack.pop()
#
#         '''
#         []
#         ['A']
#         ['A', 'B']
#         ['A']
#         '''
#
#     print(f'#{tc}', len(stack))
#


for tc in range(1, int(input())+1):
    letters = list(input())

    stack = []

    for i in range(len(letters)):
        if not stack or stack[-1] != letters[i]:
            stack.append(letters[i])

        elif stack or stack[-1] == letters[i]:
            stack.pop()

    print(stack)






































