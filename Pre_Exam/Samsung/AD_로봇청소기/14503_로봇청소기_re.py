import sys
sys.stdin = open('14503.txt', 'r')
from pprint import pprint

'''
1.현재 위치를 청소한다.
2.현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    a.왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    b.왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    c.네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    d.네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
next = {0:3, 2:1, 1:0, 3:2}

def solve(cur_x, cur_y, cur_dir, fin):
    global board
    cnt = 0
    while True:
        if fin == 4:
            bnext_x = cur_x - dx[cur_dir]
            bnext_y = cur_y - dy[cur_dir]
            if board[bnext_x][bnext_y] == 2:
                cur_x, cur_y, cur_dir, fin = bnext_x, bnext_y, cur_dir, 0
            else:
                return cnt

        if board[cur_x][cur_y] == 0: # 1
            board[cur_x][cur_y] = 2
            cnt += 1

        # 2
        left_dir = next[cur_dir]
        next_x = cur_x + dx[left_dir]
        next_y = cur_y + dy[left_dir]

        if board[next_x][next_y] == 0:
            # 2. a
            cur_x, cur_y, cur_dir, fin = next_x, next_y, left_dir, 0
        else: # 2. b : 회전만 한다. 현재의 위치를 유지한다.
            cur_x, cur_y, cur_dir, fin = cur_x, cur_y, left_dir, fin + 1

N, M = map(int, input().split())
x, y, current = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solve(x, y, current, 0))


