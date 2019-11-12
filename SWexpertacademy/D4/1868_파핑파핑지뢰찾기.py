import sys
sys.stdin = open('1868.txt','r')
from pprint import pprint
import collections
def popping(y, x):
    global board, N
    q = collections.deque([])
    q.append((y, x, 0))
    while q:
        y, x, cnt = q.pop()
        for dy, dx in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < N and board[iy][ix] == '*':
                cnt += 1
        board[y][x] = str(cnt)
        if board[y][x] == '0':
            for dy, dx in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]:
                iy = dy + y
                ix = dx + x
                if 0 <= iy < N and 0 <= ix < N and board[iy][ix] == '.':
                    q.append((iy, ix, 0))

# 어디서 더 눌리고 있는건지 찾고싶다.
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]
    clicked = 0
    for y in range(N):
        for x in range(N):
            cnt = 0
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (1, 1), (-1, 1)]:
                iy = dy + y
                ix = dx + x
                if 0 <= iy < N and 0 <= ix < N and board[iy][ix] == '*':
                    cnt += 1
                    break
            if cnt == 0 and board[y][x] == '.':
                board[y][x] = str(cnt)
                popping(y, x)
                clicked += 1
            # 0으로 만든 후, 퍼트리고, 남는 칸만 센다.
    for y in range(N):
        for x in range(N):
            if board[y][x] == '.':
                clicked += 1

    print(f'#{tc} {clicked}')