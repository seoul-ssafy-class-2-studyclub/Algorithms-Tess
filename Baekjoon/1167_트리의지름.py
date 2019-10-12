import sys
sys.stdin = open('1167.txt', 'r')
sys.setrecursionlimit(10000000)
'''
https://oneshottenkill.tistory.com/436
트리의 지름은 두 vertex간의 길이가 가장 긴 값입니다. 
이 문제에서는 간선에 가중치가 있기 때문에 멀어도 길이가 짧은 수 있고 그 반대가 될 수도 있습니다. 

트리의 지름을 구하는 방법은 다음과 같이 공식이 존재한다.
https://blog.myungwoo.kr/112
1. 트리에서 임의의 정점 x를 잡는다.
2. 정점 x에서 가장 먼 정점 y를 찾는다.
3. 정점 y에서 가장 먼 정점 z를 찾는다.
트리의 지름은 정점 y와 정점 z를 연결하는 경로다.

저는 큐를 이용해 BFS로 풀었습니다. 
BFS로 계속 풀어서 그런지 이게 편하네요. 
임의의 정점을 1번노드로 잡아서 BFS를 한번 수행하고, 
거기서 나온 정점으로 한번 더 수행해서 구했습니다.

어떤 정점에서 가장 먼 정점은 트리의 지름에 포함된다
'''

# DFS로 끝까지 탐색하고, 끝날때 들고있는 cost가 큰경우 갱신시킨다.
def find(s, cnt, visit):
    global adj_list, maxcost, x

    visit[s] = True

    if maxcost <= cnt:
        maxcost = cnt
        x = s

    for children in adj_list[s]:
        kidid, costs = children

        if visit[kidid] == False:
            find(kidid, cnt+costs, visit)

V = int(input())
adj_list = [[] for _ in range(V+1)] # 1부터 시작하므로 V+1을 해준다.

for v in range(V):
    data = list(map(int, input().split()))
    q = data[1:-1]
    for i in range(0, len(q), 2):
        adj_list[data[0]].append((q[i], q[i+1]))

# print(adj_list)
maxcost = -1
x = 0
visited = [False] * (V + 1)
find(1, 0, visited)

visited = [False] * (V + 1)
find(x, 0, visited)

print(maxcost)

#
# # DFS로 끝까지 탐색하고, 끝날때 들고있는 cost가 큰경우 갱신시킨다.
# def find(s, cnt, visit):
#     global adj_list, maxcost
#
#     visit[s] = True
#
#     if maxcost <= cnt:
#         maxcost = cnt
#
#     for children in adj_list[s]:
#         kidid, costs = children
#
#         if visit[kidid] == False:
#             find(kidid, cnt+costs, visit)
#
# V = int(input())
# adj_list = [[] for _ in range(V+1)] # 1부터 시작하므로 V+1을 해준다.
#
# for v in range(V):
#     data = list(map(int, input().split()))
#     q = data[1:-1]
#     for i in range(0, len(q), 2):
#         adj_list[data[0]].append((q[i], q[i+1]))
# # print(adj_list)
# maxcost = -1
# for start in range(1, V+1):
#     visited = [False] * (V + 1)
#     find(start, 0, visited)
#
# print(maxcost)



#
# # DFS로 끝까지 탐색하고, 끝날때 들고있는 cost가 큰경우 갱신시킨다.
# def find(s, cnt, visit):
#     global adj_list, maxcost
#
#     visit[s] = True
#
#     if maxcost <= cnt:
#         maxcost = cnt
#
#     for children in adj_list[s]:
#         kidid, costs = children
#
#         if visit[kidid] == False:
#             find(kidid, cnt+costs, visit)
#
# V = int(input())
# adj_list = [[] for _ in range(V+1)] # 1부터 시작하므로 V+1을 해준다.
#
# for v in range(V):
#     data = list(map(int, input().split()))
#     q = data[1:-1]
#     for i in range(0, len(q), 2):
#         adj_list[data[0]].append((q[i], q[i+1]))
# # print(adj_list)
# maxcost = -1
# for start in range(1, V+1):
#     visited = [False] * (V + 1)
#     find(start, 0, visited)
#
# print(maxcost)
