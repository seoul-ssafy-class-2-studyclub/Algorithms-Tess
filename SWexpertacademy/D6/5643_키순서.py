'''
#1 1
'''

import sys
sys.stdin = open('5643.txt', 'r')

T = int(input())
N = int(input())
M = int(input())

'''
자신이 몇번째인지 알려면,
1. 나를 기준으로 모든 사람들이 연결되어있어야 한다.
그런애들이 몇명인가를 확인만하면됨
방향그래프
전체를 돌면서


플로이드 워셜로 푼다.
'''
def find(s):
    global vis, visited
    vis[s] = True

    for st in adj_list[s]:
        if vis[st] == False:
            visited[st].append(s)
            find(st)

for tc in range(1, T+1):
    adj_list = [[] for _ in range(N+1)]
    for _ in range(M):
        s, l = map(int, input().split())
        adj_list[s].append(l)
    print(adj_list)
    visited = [[] for _ in range(N + 1)]
    for start in range(1, N+1):
        vis = [True] + ([False]*(N))
        find(start)
        print(vis)
    print(visited)