import sys
sys.stdin = open('1204.txt', 'r')

for tc in range(int(input())):
    tc = int(input())
    counting_sort = [0]*101
    data = list(map(int, input().split()))
    for d in data:
        counting_sort[d] += 1
    temp = 0
    res = 0
    for idx in range(len(counting_sort)):
        if counting_sort[idx] >= temp:
            temp = counting_sort[idx]
            res = idx
    print(f'#{tc}', res)