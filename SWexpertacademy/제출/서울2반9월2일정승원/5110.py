T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    n = N
    for _ in range(M - 1):
        new_numbers = list(map(int, input().split()))
        first_num = new_numbers[0]

        for i in range(n):
            if first_num < numbers[i]:
                numbers[i:0] = new_numbers
                break
        else:
            numbers += new_numbers
        n += N
    numbers = numbers[-10:]
    result = ' '.join(list(map(str, reversed(numbers))))
    print('#{} {}'.format(tc, result))
