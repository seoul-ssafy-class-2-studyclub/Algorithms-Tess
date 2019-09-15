import sys
# sys.stdin = open('1707.txt', 'r')
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(now, groupName, a, visit):
    visit[now] = groupName
    for i in a[now]:
        if visit[i] == 0:
            if dfs(i, -groupName, a, visit) == False: # 아래에서 False를 리턴받아 다음을 리턴한다.
                return False # 이분 그래프가 아니므로 False를 리턴,
        elif visit[i] == visit[now]: # 만약 0이 아니라면, 즉 방문한 노드가 아니라면, 현재노드의 groupName과 다음노드의 groupName을 비교
            return False # 번호가 같으면 인접노드가 같은 그룹이므로 False 리턴
    return True # DFS 탐색이 끝날때까지 False를 리턴하지 않았을 경우, 모든 노드를 이분화하는 것을 성공, 1로 바뀐채로 다음 노드를 찾으러 True를 리턴하며 함수 종료

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    
    for _ in range(E):
        v, u = map(int, input().split())
        # 이분그래프는 무방향그래프에서 확인 가능하다.
        adj_list[v].append(u)
        adj_list[u].append(v)

    visited = [0]*(V+1)
    res = True
    for idx in range(1, V+1):
        if visited[idx] == 0:
            if dfs(idx, 1, adj_list, visited) == False: # return을 False 로 받으면,
                res = False
                break # False를 한 번이라도 받으면 더이상 순회할 필요가 없다.

    if res == True: # False인적이 없으므로,
        print('YES')
    elif res == False:
        print('NO')
