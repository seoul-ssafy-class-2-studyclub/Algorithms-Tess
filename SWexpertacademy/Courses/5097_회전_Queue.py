import sys
sys.stdin = open('5097.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    for idx in range(M):
        rotation = queue.pop(0)
        queue.append(rotation)
    print(f'#{tc}', queue[0])
