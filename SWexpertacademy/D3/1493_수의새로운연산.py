import sys
sys.stdin = open('1493.txt', 'r')


'''
#1 33003
#2 6598
#3 19070
'''
T = int(input())
for tc in range(1, T+1):
    x, y = 3, 3# map(int, input().split())

    n = x + y

    re = (((n -2) * (n -1)) // 2) + x
    print(f'#{tc}', re)