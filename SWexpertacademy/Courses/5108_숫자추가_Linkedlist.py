import sys
sys.stdin = open('5108.txt', 'r')

'''
#1 4
#2 32402
#3 13398
'''

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    original_list = list(map(int, input().split()))

    for _ in range(M):
        new_idx, new_num = list(map(int, input().split()))
        original_list.insert(new_idx, new_num)
    print(f'#{tc} {original_list[L]}')