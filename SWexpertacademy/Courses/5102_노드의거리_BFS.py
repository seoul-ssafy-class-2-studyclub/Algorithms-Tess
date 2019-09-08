import sys
sys.stdin = open('5102.txt', 'r')

# 몇개의 간선을 지나야 특정 노드에 도착할 수 있는지 결과출력
def search(s, g):
    visited = [False]*1001
    queue = []
    cnt = 0
    queue.append((s, cnt))
    while queue:
        si, cnt = queue.pop(0) # 부모노드와 카운트를 빼낸다.
        if visited[si] == False:
            visited[si] = True # 다시 방문하는 것을 막기위한 처리
            cnt += 1
            for sj in adj_list[si]: # 부모노드를 인덱스로 하여 자식을 빼낸다.
                queue.append((sj, cnt))
                if sj == g: # 도착지점에 왔다면, 반환한다.
                    return cnt, g
    # 끝까지 도달했음에도 불구하고 큐에 모든게 빠져나왔다면, 도착노드에 갈 수 없다는 뜻이므로 여태까지의 카운트는 의미가 없다.
    # 때문에 0으로 바꿔 반환한다.
    cnt = 0
    return cnt, g

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(1001)]

    # 인접리스트 생성
    for e in range(E):
        s, g = map(int, input().split())
        # 무방향 그래프에서 확인해줘야한다. 무방향이므로 자식과 부모 부모와 자식이 모두 양방향 접근 가능하다.
        adj_list[s].append(g)
        adj_list[g].append(s)
    print(adj_list)
    S, G = map(int, input().split())
    result = search(S, G)
    print(f'#{tc}', result[0])


