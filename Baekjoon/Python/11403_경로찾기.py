'''
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0
'''


import sys
# sys.stdin = open('11403.txt', 'r')
input = sys.stdin.readline

def DFS(I, name, vis):
    global result
    result[name][I] = 1

    for i in adj_list[I]:
        if vis[i] == False:
            vis[i] = True
            DFS(i, name, vis)

# 0 에서부터
N = int(input())
adj_list = [[] for _ in range(N)]
for i in range(N):
    data = list(map(int, input().split()))
    # 받은 한 줄에서 쭉 돌면서 1이 있으면 해당 인덱스에 +1을 해서 
    # 인접리스트에 추가하고
    # 그래프를 그린다

    for j in range(N):
        if data[j] == 1:
            adj_list[i].append(j)

result = [[0]*N for _ in range(N)]

start = 0
for x in adj_list:
    vis = [False]*N
    for i in x:
        DFS(i, start, vis)
    start += 1 # 다 돌고 +1 처리

for r in result:
    print(' '.join(map(str,r)))