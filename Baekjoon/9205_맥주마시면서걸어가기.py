import sys
sys.stdin = open('9205.txt', 'r')
'''
happy
sad
'''
from pprint import pprint

import sys
input = sys.stdin.readline
def solve():
    for idx1 in range(0, len(data) - 1):
        for idx2 in range(idx1 + 1, len(data)):
            if abs(data[idx1][0] - data[idx2][0]) + abs(data[idx1][1] - data[idx2][1]) <= 1000:  # 1000보다 크면 못간다.
                avaliable[idx1][idx2] = 1
                avaliable[idx2][idx1] = 1
            elif avaliable[0][n - 1] == 1:
                return 'happy'

    for j in range(n):
        for s in range(n):
            for e in range(n):
                if avaliable[s][j] == 0 or avaliable[j][e] == 0 or avaliable[s][e] == 1:
                    continue
                else: # avaliable[s][e] == 0 인데 avaliable[s][j] == 1이고 avaliable[j][e] == 1이라면,
                    avaliable[s][e] = 1
                    avaliable[e][s] = 1

    if avaliable[0][n - 1] == 1:
        return 'happy'
    else:
        return 'sad'

ans = []
t = int(input())
for _ in range(t):
    n = int(input()) + 2
    data = []
    for _ in range(n):
        x, y = map(int, input().split())
        data.append((x, y))
    avaliable = [[0]*(n) for _ in range(n)]
    ans += [solve()]
print('\n'.join(ans))