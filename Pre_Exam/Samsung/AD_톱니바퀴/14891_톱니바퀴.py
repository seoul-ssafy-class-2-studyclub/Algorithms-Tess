import sys
sys.stdin = open('14891.txt', 'r')


import collections
data = [list(map(int, input().split())) for _ in range(4)]
N = int(input())

# 1이면 시계방향, -1이면 반시계방향
q = collections.deque([])
for i in range(N):
    name, di = map(int, input().split())
    q.append((name, di))
