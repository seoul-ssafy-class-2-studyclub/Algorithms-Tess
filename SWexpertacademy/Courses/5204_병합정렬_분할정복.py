import sys
sys.stdin = open('5204.txt', 'r')

'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

#1 2 0
#2 6 6
'''


# N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수
# merging하는 과정에서 left right를 pop해서 result에 넣기 전에
# left[-1], right[-1]을 비교해서
# left[-1]이 더 큰경우를 counting


# 분할 정복
def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

# 병합
def merge(left, right):
    global cnt
    result = []
    if left[-1] > right[-1]:
        cnt += 1
    l = h = 0
    while len(left) > l and len(right) > h:
        if left[l] <= right[h]:
            result.append(left[l])
            l+=1
            # print(l)
        else:
            result.append(right[h])
            h += 1
            # print(h)
    if len(left) > 0:
        result += left[l:]
    if len(right) > 0:
        result += right[h:]
    return result

for tc in range(int(input())):
    idx = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print(f'#{tc+1} {arr[idx//2]} {cnt}')
