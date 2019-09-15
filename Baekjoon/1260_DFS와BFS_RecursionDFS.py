import sys
sys.stdin = open('1260.txt', 'r')

# parents 가 되는 부분을 출력해야하는데..
import collections

# 재귀는 for문으로 앞에서 부터 빼오므로 adj_list의 children을 reversed할 필요 없음

def DFS(s, path):
    global adj_list
    global DFS_res
    global visited2
    # 재귀스택으로 해보기
    # 찾으면, 작은 숫자부터 출력

    flag = True
    for i in adj_list[s]:
        if visited2[i] == False:
            flag = False
            visited2[i] = True
            return DFS(i, path + [i])
            visited2[i] = False

    if flag:
        DFS_res.append(path)
        return True


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
        s = queue.popleft() # 앞에서부터 pop한다.
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

DFS_res = []
visited2 = [False] * 10001
visited2[Start] = True
DFS(Start, [Start])
print(DFS_res)
BFS_res = BFS(Start)

for i in DFS_res:
    print(i, end=' ')
print()

for i in BFS_res:
    print(i, end=' ')
print()