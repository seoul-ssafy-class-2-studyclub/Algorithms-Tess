import sys
sys.stdin = open('1260.txt', 'r')

'''
4 5 1
1 2
1 3
1 4
2 4
3 4

처음줄에는 DFS
1 2 4 3

두번째줄에는 BFS
1 2 3 4
'''

# parents 가 되는 부분을 출력해야하는데..
import collections

def DFS(s):
    global adj_list
    # 재귀스택으로 해보기
    # 찾으면, 작은 숫자부터 출력
    myres = []
    stack = collections.deque()
    stack.append(s)
    visited = [False]*10001
    while stack:
        s = stack.pop()
        if s not in myres:
            myres.append(s)
        visited[s] = True
        children = list(sorted(adj_list[s], reverse=True)) # 작은 아이부터 출력
        for i in children:
            if visited[i] == False:
                stack.append(i)
    return myres

# 1 -> 2 3 4
# 2 -> 4
# 3 -> 4

def BFS(s):
    global adj_list
    myres = []
    queue = collections.deque()
    queue.append(s)
    myres.append(s)
    visited = [False]*10001
    while queue:
        s = queue.popleft()
        children = list(sorted(adj_list[s]))
        for i in children:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                if i not in myres:
                    myres.append(i)
    return myres



N, M, Start = map(int, input().split())

adj_list = [[] for _ in range(10001)] # 10000 으로 진행
for i in range(M):
    parent, child = map(int, input().split())
    adj_list[parent].append(child)
    adj_list[child].append(parent)
DFS_res = DFS(Start)
BFS_res = BFS(Start)

for i in DFS_res:
    print(i, end=' ')
print()

for i in BFS_res:
    print(i, end=' ')
print()