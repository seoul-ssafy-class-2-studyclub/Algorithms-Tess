import sys
sys.stdin = open('4013.txt', 'r')

import collections
T = int(input())
for tc in range(1):
    N = int(input())
    magnet = {}
    for name in range(4):
        magnet[name] = list(map(int, input().split()))

    q_info = collections.deque([])
    for _ in range(N):
        q_info.append([map(int, input().split())])

    print(magnet)
    print(q_info)