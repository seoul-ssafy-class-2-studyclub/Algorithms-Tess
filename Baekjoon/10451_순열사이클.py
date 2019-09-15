import sys
# sys.stdin = open('10451.txt', 'r')
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(v):

    visited[v] = True

    for u in adj_list[v]:
        if visited[u] == False: # v에서 u를 확인할때, 방문하지 않았다면 dfs를 태운다.
            dfs(u)

for tc in range(int(input())):
    N = int(input()) # 순열 개수
    permutations = list(map(int, input().split())) # u가 될 permutations
    
    # 후에 1001로 수정
    adj_list = [[] for _ in range(1001)]

    # 양방향이라는 전제는 깔려있지않다.
    for idx in range(N): # v는 1부터 시작하므로
        adj_list[idx+1].append(permutations[idx])

    #print(adj_list)

    visited = [False]*(1001)
    cnt = 0
    for idx in range(1, 1001):
        if visited[idx] == False and adj_list[idx] != []: # []가 아닌경우에만 시작해서 cnt올린다.
            cnt += 1
            dfs(idx)

    print(cnt)