import sys
sys.stdin = open('1222.txt', 'r')


for tc in range(1, 11):
    N = int(input())
    text = list(map(str, input()))

    number_stack = []
    operator_stack = []

    cnt = 0
    res = 0
    for idx in range(0, N):

        if text[idx] == "+":
            operator_stack.append(text[idx])

        else:
            number_stack.append(text[idx])

    res = sum(list(map(int, number_stack)))
    print(f'#{tc}', res)
