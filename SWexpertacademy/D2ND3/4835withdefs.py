def result(arr):
    max_temp = arr[0]
    for i2 in range(1, len(arr)):
        if max_temp < arr[i2]:
            max_temp = arr[i2]
    cal_list.append(max_temp)

    min_temp = arr[0]
    for i3 in range(1, len(arr)):
        if min_temp > arr[i3]:
            min_temp = arr[i3]
    cal_list.append(min_temp)

    result = cal_list[0] - cal_list[1]
    return result

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    aj = list(map(int, input().split()))
    temp_sum_list = []
    sum_list = []
    cal_list = []

    for i in range(0, N-M+1):
        for i1 in range(0, M):
            temp_sum_list.append(aj[i+i1])
            if i1 == M-1:
                temp_sum = sum(temp_sum_list)
                sum_list.append(temp_sum)
                temp_sum_list = []
                continue

    A = result(sum_list)

    print('#{} {}'.format(tc, A))
