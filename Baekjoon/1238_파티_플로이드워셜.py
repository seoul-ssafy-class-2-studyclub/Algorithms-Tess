import sys
sys.stdin = open('1238.txt', 'r')
input = sys.stdin.readline
import heapq


# pathscount = [[0,2], [0,1]]
# print(pathscount[0][1]) # 1 부모노드에서 2 자식노드로가는데 사용되는 가중치를 뽑을 수 있다.

# N: 마을수 M: 간선수 Goal: 도착지
N, M, Goal = map(int, input().split())
infinity = float('inf')

# 2차원 배열 준비
pathscount = [[infinity]*N for i in range(N)]
# print(pathscount)

for i in range(N):
    pathscount[i][i] = 0

# 0은 노드1이다 라고 생각하면서 풀어야한다.
graph = {i: [] for i in range(N)}
for i in range(M):
    #S: 시작 E: 끝 T: 소요시간
    S, E, T = map(int, input().split())
    S -= 1
    E -= 1
    graph[S].append((E, T))
    pathscount[S][E] = T # 2차원 배열 가중치 추가
print(graph)
print(pathscount)

# 자기부터 시작해서 Goal에 도착하면 while문이 끝나도록 하면서 최소비용 갱신

hq = []
for i in range(N):
    # print(i)
    heapq.heappush(hq, (0, i)) # 자기자신의 가중치는 0으로 시작한다.

    while hq:
        Ti, now = heapq.heappop(hq)

        if pathscount[i][now] < Ti:
            continue

        for child, time in graph[now]:
            print('==', graph[now])
            candi = time + pathscount[i][now]

            # 여기에 안들어간다.
            if candi < pathscount[i][child]:
                print('---')
                pathscount[i][child] = candi
                heapq.heappush(hq, (candi, child))

print(pathscount)


