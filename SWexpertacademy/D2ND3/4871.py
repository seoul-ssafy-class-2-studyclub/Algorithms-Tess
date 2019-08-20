import sys
sys.stdin = open('4871.txt', 'r')

def dfs_stack(arr, start):

    visit = []
    stack = []
    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visit:
            visit.append(node)
            stack.extend(arr[node])
            if G in arr[node]:
                return 1

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    #print(V, E)

    board = []
    for _ in range(E):
        temp = list(map(int, input().split()))
        board.append(temp)

    S, G = map(int, input().split())

    adj_list = [[] for i in range(100)]

    for i in range(len(board)):
        adj_list[board[i][0]].append(board[i][1])

    res = dfs_stack(adj_list, S)
    print(f'#{tc} {res}')