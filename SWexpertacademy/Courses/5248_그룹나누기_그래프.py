import sys
sys.stdin = open('5248.txt', 'r')
'''
#1 3
#2 2
#3 3
'''

def find(s):
    global visited
    visited[s] = True
    for child in adj_list[s]:
        if visited[child] == False:
            find(child)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    adj_list = [[] for i in range(N+1)]

    for i in range(0, M*2, 2): # input 항상 어떤 형식으로 들어오는지 잘 확인 필요
        adj_list[data[i]].append(data[i+1])
        adj_list[data[i + 1]].append(data[i])
    visited = [True] + [False] * N
    res = 0
    for i in range(1, N+1):
        if visited[i] == False:
            res += 1
            find(i)
    print(f'#{tc}', res)