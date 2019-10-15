import sys
sys.stdin = open('5249.txt', 'r')

'''
# g: graph s: start node
def MST_Prim(g, s):
    key = ['INF'] * N # 가중치를 무한대로 초기화
    pi = [None] * N # 트리에서 연결될 부모 정점 초기화
    visited = [False] * N # 방문여부 초기화
    key[s] = 0 # 시작정점의 가중치를 0으로 설정

    for _ in range(N): # 정점의 개수만큼 반복
        minIndex = -1
        min = 'INF'
        for i in range(N): # 방문 안한 정점중 최소 가중치 정점 찾기
            if not visited[i] and key[i] < min:
                min = key[i]
                minIndex = i
        visited[minIndex] = True # 최소 가중치 정점 방문처리
        for v, val in g[minIndex]: # 선택 정점의 인접한 정점
            if not visited[v] and val < key[v]:
                key[v] = val # 가중치 갱신
                pi[v] = minIndex # 트리에서 연결될 부모 정점
'''


'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

#1 2
#2 13
#3 22
'''

# 최소신장트리: 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우

# 0번부터 V번까지의 노드와
# E개의 간선을 가진 그래프 정보가 주어질 때,
# 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램

# g: graph s: start node
# 프림알고리
def MST_Prim(g, s): # 인접그래프를 무향으로 받고, 0에서 시작한다.
    # INF = float('inf')
    key = [999999] * E # 가중치를 무한대로 초기화, pi에 저장된 간선의 가중치 저
    pi = [None] * E # 트리에서 연결될 부모 정점 초기화, 정점이 트리에 연결될때 사용된 간선정보 저장
    visited = [False] * E # 방문여부 초기화
    key[s] = 0 # 시작정점의 가중치를 0으로 설정

    # V의 수만큼해야하고, 인덱스는 -1까지니까 +1을 해준다.
    for _ in range(V+1): # 정점의 개수만큼 반복
        minIndex = -1
        min = 999999
        for i in range(V+1): # 방문 안한 정점중 최소 가중치 정점 찾기
            if not visited[i] and key[i] < min:
                min = key[i]
                minIndex = i
        visited[minIndex] = True # 최소 가중치 정점 방문처리
        for v, val in g[minIndex]: # 선택 정점의 인접한 정점
            if not visited[v] and val < key[v]:
                key[v] = val # 가중치 갱신
                pi[v] = minIndex # 트리에서 연결될 부모 정점
    return key, pi, visited


T = int(input())
for tc in range(1, T+1):
    # 마지막 노드번호 V와 간선의 개수 E
    V, E = map(int, input().split())

    # 간선의 개수만큼 저장한다.
    adj_list = [[] for _ in range(E)]
    # 간선의 양 끝 노드 n1, n2, 가중치 w
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        # 무향그래프
        # (노드, 가중치) 순으로 저장한다.
        adj_list[n1].append((n2, w))
        adj_list[n2].append((n1, w))

    resweight, resparents, resvisited = MST_Prim(adj_list, 0)
    # 간선의 수 -1 만큼을 가진 그래프
    # print(resweight)
    result = 0
    for i in resweight:
        if i != 999999:
            result += i
    print(f'#{tc}', result)

