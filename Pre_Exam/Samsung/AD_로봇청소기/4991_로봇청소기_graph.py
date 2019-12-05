from pprint import pprint
import collections
import itertools
import sys
sys.stdin = open('4991.txt', 'r')

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    board = [list(input()) for _ in range(h)]
    dusts = []
    d_num = 1

    for y in range(h):
        for x in range(w):
            if board[y][x] == '*':
                dusts.append((y, x))    # 번호 = 인덱스 + 1(로봇)
                board[y][x] = d_num
                d_num += 1
            elif board[y][x] == 'o':
                board[y][x] = 0
                sy, sx = y, x
    INF = float('inf')
    distance = [[INF] * d_num for _ in range(d_num)]
    # pprint(distance)
    for dust in dusts:
        oi, oj = dust
        board[oi][oj], temp = '.', board[oi][oj]
        queue = collections.deque([(oi, oj, 0)])
        visit = [[False] * w for _ in range(h)]
        while queue:
            idx1, idx2, move = queue.popleft()
            if visit[idx1][idx2] == False:
                visit[idx1][idx2] = True
                if board[idx1][idx2] == '.':
                    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        nxt1 = idx1 + dy
                        nxt2 = idx2 + dx
                        if 0 <= nxt1 < h and 0 <= nxt2 < w and visit[nxt1][nxt2] == False:
                            if board[nxt1][nxt2] == 'x':
                                continue
                            elif board[nxt1][nxt2] != 'x': # . 혹은 0~먼지
                                queue.append((nxt1, nxt2, move + 1))
                else:
                    distance[temp][board[idx1][idx2]] = move
                    distance[board[idx1][idx2]][temp] = move
        board[oi][oj] = temp
    for d in distance:
        pprint(d)
    dusts = list(range(1, d_num))
    perms = itertools.permutations(dusts)
    min_value = INF
    for perm in perms:
        arr = [0] + list(perm)
        total = 0
        flag = True
        for i in range(d_num - 1):
            total += distance[arr[i]][arr[i + 1]]
            if min_value <= total:
                flag = False
                break
        if flag is True:
            min_value = total
    if min_value == INF:
        print(-1)
    else:
        print(min_value)