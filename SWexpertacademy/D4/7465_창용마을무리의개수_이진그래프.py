import sys
sys.stdin = open('7465.txt', 'r')

def solve(y):
    global vistied

    vistied[y] = True
    for neighbor in adj_list[y]:
        if vistied[neighbor] == False:
            solve(neighbor)

for tc in range(int(input())):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]

    for i in range(M):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)

    vistied = [True] + [False]*N
    cnt = 0
    for y in range(1, N+1):
        if vistied[y] == False: # False 라면, 들어간다.
            cnt += 1
            solve(y)
    print(f'#{tc+1}', cnt)