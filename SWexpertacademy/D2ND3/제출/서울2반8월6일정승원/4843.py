def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

    return a


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    new_list = [0] * N
    #bigger_list, equal_list, smaller_list = QuickSort(num_list)
    #print(bigger_list, equal_list, smaller_list)

    result = selectionSort(num_list)
    #print(result)

    cnt0 = 0
    cnt1 = 0
    for n in range(N): # 0 1 2 3 4 5 6 7 8 9 10
        if cnt0 < int(N/2) or cnt1 < int(N/2):
            if n%2 == 0: #0 2 4
                new_list[n] = result[-cnt0-1] # 1 2 3 4
                cnt0 += 1
            elif n%2 == 1: # 1 3 5
                new_list[n] = result[cnt1]
                cnt1 += 1

    print(f'#{tc} ', end='')
    for char in new_list[:10]:
        print(f'{char}', end=' ')
    print()
