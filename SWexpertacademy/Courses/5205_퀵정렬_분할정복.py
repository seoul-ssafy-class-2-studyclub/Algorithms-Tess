import sys
sys.stdin = open('5204.txt', 'r')

'''
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, , N/2번 원소를 출력한다.
'''
#
# def qsort(arr):
#     if len(arr) <= 1: # 원소개수가 0이나 1이면 이미 정렬이 된 상태이므로 가지치기한다.
#         return arr
#
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr[-1:0] = [num]
#         elif num > pivot:
#             greater_arr[-1:0] = [num]
#         else:
#             equal_arr[-1:0] = [num]
#     return qsort(lesser_arr) + equal_arr + qsort(greater_arr)
#
#
# for tc in range(int(input())):
#     N = int(input())//2
#     myarr = list(map(int, input().split()))
#
#     myarr = qsort(myarr)
#     print(f'#{tc+1}', myarr[N])

#
# def qsort(arr):
#     if len(arr) <= 1: # 원소개수가 0이나 1이면 이미 정렬이 된 상태이므로 가지치기한다.
#         return arr
#
#     else:
#         pivot = arr[0] # pivot은 아무 값이나 가능하므로 가장 처음에 있는 인덱스를 기준점을 삼는다.
#         # less 와 more 둘다 기준점을 제외한 모든 리스트에있는 원소들을 순회하면서,
#         # pivot 이하인경우 less에 추가하고, 이상인경우 more에 추가하는데,
#         # 이를 재귀적으로 호출한다.
#         less = [i for i in arr[1:] if i <= pivot]
#         more = [i for i in arr[1:] if i > pivot]
#         return qsort(less) + [pivot] + qsort(more)
#
# for tc in range(int(input())):
#     N = int(input())//2
#     myarr = list(map(int, input().split()))
#     myarr = qsort(myarr)
#     # print(myarr)
#     print(f'#{tc+1}', myarr[N])


def q_sort(l, r): # 왼쪽, 오른쪽
    if l < r: # 왼쪽보다 오른쪽이 더 클때 아래를 시작, 0 < 4
        pivot = partition(l, r)
        if idx > pivot:
            q_sort(pivot + 1, r)
        else:
            q_sort(l, pivot - 1)

def partition(l, r):
    pivot = arr[r] # 맨끝을 기준점으로 잡고,
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

for case in range(1, int(input()) + 1):
    N = int(input())
    idx = N // 2
    arr = list(map(int, input().split()))
    q_sort(0, N - 1)
    print(f'#{case} {arr[N // 2]}')