import sys
sys.stdin = open('5102.txt', 'r')

def search(s, g):
    visited = [False]*1001

    queue = []
    cnt = 0
    queue.append((s, cnt))
    while queue:
        si, cnt = queue.pop(0)
        if visited[si] == False:
            visited[si] = True
            cnt += 1
            for sj in adj_list[si]:
                queue.append((sj, cnt))
                if sj == g:
                    return cnt, g
    cnt = 0
    return cnt, g




T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(1001)]

    for e in range(E):
        s, g = map(int, input().split())
        # 무방향 그래프에서 확인해줘야한다.
        adj_list[s].append(g)
        adj_list[g].append(s)
    print(adj_list)
    S, G = map(int, input().split())
    result = search(S, G)
    print(f'#{tc}', result[0])


