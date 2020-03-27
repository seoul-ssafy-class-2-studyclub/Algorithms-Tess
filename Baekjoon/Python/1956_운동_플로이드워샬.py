import sys
sys.stdin = open('1956.txt', 'r')
from pprint import pprint

# 플로이드 워샬
'''
3
'''

import sys
input = sys.stdin.readline
V, E = map(int, input().split())
INF = 1e9
flo_arr = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    flo_arr[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if (flo_arr[i][k]+flo_arr[k][j]) < flo_arr[i][j]:
                flo_arr[i][j] = flo_arr[i][k]+flo_arr[k][j]
mymin = 1e9
for i in range(1, V+1):
    if mymin > flo_arr[i][i]:
        mymin = flo_arr[i][i]

if mymin == 1e9:
    print(-1)
else:
    print(mymin) # 이 부분