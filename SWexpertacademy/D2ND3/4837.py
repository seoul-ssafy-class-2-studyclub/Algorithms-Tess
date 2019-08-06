import sys
sys.stdin = open('4837.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    #print(tc, N, K)

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    Al = len(A)
    final_list = []
    count = 0
    for i in range(1<<Al):
        su = []
        for j in range(Al):
            if i&(1<<j):
                su.append(A[j])
        final_list.append(su)

    for temp in final_list:
        if len(temp) == N:
            if sum(temp) == K:
                count += 1
    print(f'#{tc} {count}')




