import sys
sys.stdin = open('4843.txt', 'r')

#quick sort 사용하려다가 이 문제에 맞지 않음을 깨우침 ㅠ
def QuickSort(arr):
    if len(arr) <= 1:
        return arr

    bigger_list = []
    smaller_list = []
    equal_list = []

    for n in range(1, N):
        middle = arr[0]

        if arr[n] > middle:
            bigger_list.append(arr[n])
            #print(bigger_list)
        elif arr[n] < middle:
            smaller_list.append(arr[n])
            #print(smaller_list)
        else:
            equal_list.append(arr[n])
    equal_list.append(middle)

    return bigger_list, equal_list, smaller_list


## min으로 sort 해준다.

def selectionSort(a): # [10,9,8,7,6,5,4,3,2,1]  길이10
    for i in range(0, len(a)-1): # 0을 기준으로 잡는다. (가장 작은 인덱스)
        min = i
        for j in range(i+1, len(a)): # 0+1, 10  1~9
            if a[min] > a[j]: # a[0] > a[1]이면, 10 > 9
                min = j #  1 = 1
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

    ## 10개까지!!!만 출력
    print(f'#{tc} ', end='')
    for char in new_list[:10]:
        print(f'{char}', end=' ')
    print()


