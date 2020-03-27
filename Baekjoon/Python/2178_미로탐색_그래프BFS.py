import sys
sys.stdin = open('2178.txt', 'r')
import collections

# 최단거리를 구하는 문제
# (0,0)에서 출발해서
# (N-1, M-1)에 도착
N, M = map(int, input().split())
GN, GM = N-1, M-1

maze = [list(map(int, input())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]

q = collections.deque([])
q.append((0,0))
visited[0][0] = True
res = 0
my_min = 9999999
while q:

    res += 1
    for _ in range(len(q)):
        y, x = q.popleft()
        if y == GN and x == GM:
            if my_min > res: # 비교하면서 결과를 출력하는게 더 빠르다. 시간초과 및 메모리 해결
                my_min = res

        else:
            for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                iy = dy + y
                ix = dx + x

                if 0 <= iy < N and 0 <= ix < M and visited[iy][ix] == False:

                    if maze[iy][ix] == 1:
                        q.append((iy, ix))
                        visited[iy][ix] = True
print(my_min)