import sys
sys.stdin = open('4869.txt', 'r')


def combination(M, N):
    mother = 1
    son = 1
    for n in range(N):
        son *= (M - n)
        mother *= (N - n)
    return int(son / mother)


for tc in range(int(input())):
    N = int(input()) // 10
    quotient = N // 2

    result = 0
    for a in range(1, quotient):
        result += combination(N - a, a) * (2 ** a)

    if N % 2 == 1:
        result += (quotient + 1) * (2 ** quotient) + 1
    else:
        result += 1 + (2 ** quotient)

    print('#{} {}'.format(tc + 1, result))


