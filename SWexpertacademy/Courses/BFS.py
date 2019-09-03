def BFS(G, v): # 그래프 G, 탐색시작점 v
    visited = [0]*n # 정점의 개수
    queue = []
    queue.append(v)

    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
        for i in G[t]: # t와 연결된 모든 선에대해
            if not visited[i]: # 방문되지 않은 곳이라면,
                queue.append(i)