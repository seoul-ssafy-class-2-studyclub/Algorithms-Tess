import sys
sys.stdin = open('2623.txt', 'r')
input = sys.stdin.readline
import collections

N, M = map(int, input().split())
# 인접리스트를 저장할 배열
adj_list = [[] for _ in range(N+1)]
# 진입차수를 저장할 배열
inDegree = [0]*(N+1)
for _ in range(M):
    data = list(map(int, input().split()))
    num = data[0]
    info = data[1:]
    head = 0
    for child in data[2:]:
        adj_list[info[head]].append(child)
        head += 1
        inDegree[child] += 1
# print(adj_list) # [[], [4], [5, 3], [], [3], [4], [2]]
# print(inDegree) # [0, 0, 1, 2, 2, 1, 0]

# 위상 정렬된 결과를 저장할 배열
res = []

# q를 돌면서 한다.
# 1. 진입차수가 0인 것들을 q에 넣는다.

q = collections.deque([])
for idx in range(1, N+1): # 1~6 까지 돈다.
    # print(idx)
    if inDegree[idx] == 0:
        inDegree[idx] = -1
        q.append(idx)
# print(q)

# q에 넣고 같은 레벨인 것들 먼저 돌면서 값에 넣어준다.
while q:

    for _ in range(len(q)):
        # 1. 정점하나를 뽑는다.
        parent = q.popleft()
        res.append(parent)

        for child in adj_list[parent]:
            # 해당 정점(parent)에서 나가는 간선(child)를 제거한다.
            # 그리고 in-degree를 업데이트 한다.
            inDegree[child] -= 1

            # indegree가 0인 정점만 queue에 추가한다.
            if inDegree[child] == 0:
                inDegree[child] = -1
                q.append(child)
# print(res)
# res의 길이가 N 일때 값을 쭉 출력해주고 그렇지 않은 경우 0으로 출력한다.

if len(res) == N:
    print('\n'.join(map(str, res)))
else:
    print(0)