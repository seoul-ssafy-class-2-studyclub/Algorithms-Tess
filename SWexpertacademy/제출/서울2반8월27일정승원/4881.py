
def permutation(sums, length):
    global result

    if length == N:

        if sums < result:
            result = sums

        return True

    for nxt in range(N):
        if visited[nxt]:
            continue
        temp = board[length][nxt]
        if sums + temp >= result:
            continue
        visited[nxt] = True
        permutation(sums + temp, length + 1)
        visited[nxt] = False

for ro in range(int(input())):
    N = int(input())
    board = []
    per_list = []
    visited = [False for _ in range(N + 1)]
    result = 9*N
    for _ in range(N):
        board.append(list(map(int, input().split())))

    for i in range(N):
        visited[i] = True
        permutation(board[0][i], 1)
        visited[i] = False

    print('#%d %d' % (ro + 1, result))