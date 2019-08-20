import sys
sys.stdin = open('1285.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    throw = list(map(int, input().split()))

    plus_throw = []

    for one_throw in throw:
        if one_throw < 0:
            plus_throw.append(abs(one_throw))
        else:
            plus_throw.append(one_throw)

    min_throw = min(plus_throw)

    min_throw_count = plus_throw.count(min_throw)

    print(f'#{tc}', min_throw, min_throw_count)