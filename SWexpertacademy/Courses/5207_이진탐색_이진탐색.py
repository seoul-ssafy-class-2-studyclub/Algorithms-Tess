import sys
sys.stdin = open('5207.txt', 'r')

def binary(arr, goal, status=0):
    global res
    low = 0
    high = len(arr)-1 # 마지막 인덱스 숫자
    while low <= high:
        mid = (low+high)//2
        guess = arr[mid]
        if guess == goal:
            res += 1
            return
        if guess > goal and (status == 0 or status == 1): # mid로 추측된 값이 더 크다면,
            high = mid - 1
            status = 2
        elif guess < goal and (status == 0 or status == 2): # 작다면,
            low = mid + 1
            status = 1
        else:
            return


for tc in range(int(input())):
    N, M = map(int, input().split())
    find = list(map(int, input().split()))
    mylist = list(map(int, input().split()))
    find.sort()
    res = 0
    for one in mylist:
        binary(find, one)
    print(f'#{tc+1}', res)

#
# def bi_search(l, r, num, di=0):
#     global cnt
#     m = (l + r) // 2
#     mid = A[m] # 가운데 값을 잡고,
#     if mid == num:
#         cnt += 1
#         return True
#     # 순서를 번갈아가면서 찾도록한다.
#     # 번갈아가면서 재귀호출이 이뤄진다.
#     if num < mid and (di == 'r' or not di):
#         bi_search(l, m-1, num, 'l') # 그리고 재귀호출
#     elif num > mid and (di == 'l' or not di):
#         bi_search(m+1, r, num, 'r') # 그리고 재귀호출
#
# for case in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     A.sort()
#     B = list(map(int, input().split()))
#     cnt = 0
#     for n in B:
#         bi_search(0, N-1, n)
#
#     print(f'#{case} {cnt}')