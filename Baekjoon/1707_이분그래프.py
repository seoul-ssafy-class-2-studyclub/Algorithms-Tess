
'''
이분그래프란?
그래프의 모든 정점이 두 그룹으로 나눠지고,
서로 다른 그룹의 정점이 간선으로 연결되어져 있는
(<=> 같은 그룹에 속한 정점끼리는 서로 인접하지 않도록 하는) 그래프


이분 그래프인지 확인하는 방법은 BFS, DFS 탐색을 이용하면 된다.
이분 그래프는 BFS를 할 때 같은 레벨의 정점끼리는 무조건 같은 색으로 칠해진다.
**연결 성분의 개수(Connected Component)를 구하는 방법과 유사**
모든 정점을 방문하며 간선을 검사하기 때문에 
시간 복잡도는 O(V+E)로 그래프 탐색 알고리즘과 같다.
'''

'''
방문안됨 0 집합첫번째 1 집합두번째 -1
DFS 탐색을 통해 아직 방문하지 않은 노드(0)를 방문 -> 방문할 때 어떤 색인지 표시 
이 코드에서는 2개의 그룹으로 나눈다고 가정, 1과 -1의 그룹으로 구분
다음 노드는 현재 그룹 번호에 -1을 곱해서 1과 -1을 교차하여 그룹 짓도록 했다.
1) 만약 다음 노드가 이미 방문한 노드라면, 현재 노드의 그룹 번호와 다음 노드의 그룹번호가 같은지 확인한다.
번호가 같으면 인접한 노드가 같은 그룹이므로, false를 리턴한다.

2) DFS 탐색이 끝날 때 까지 false를 리턴하지 않았다면, 모든 노드를 이분화하는 것에 성공했으므로 true를 리턴한다.
https://jason9319.tistory.com/149
'''
# 이분그래프는 무방향이다.

import sys
# sys.stdin = open('1707.txt', 'r')
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(now, group, a, check):
    check[now] = group
    for i in a[now]:
        if check[i] == 0:
            if dfs(i, -group, a, check) is False: # False가 되면,
                return False #함수는 끝나.
        elif check[i] == check[now]: # 두번째 불렀을때, i로 시작하는 곳과 now로 시작하는 곳이 같은 집합이야?
            return False #그러면 False지.
    return True

for _ in range(int(input())):
    v, e = map(int, input().split())
    a = [[] for _ in range(v+1)]
    check = [0]*(v+1)
    for _ in range(e):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)
    ans = True
    for i in range(1, v+1):
        if check[i] == 0:
            if dfs(i, 1, a, check) is False:
                ans = False
                break
    if ans == True:
        print('YES')
    else:
        print('NO')
