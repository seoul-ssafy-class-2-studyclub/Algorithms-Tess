'''
빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임


'.'은 빈 칸을 의미하고,
'#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며,
'O'는 구멍의 위치를 의미한다.
'R'은 빨간 구슬의 위치,
'B'는 파란 구슬의 위치


구슬을 손으로 건드릴 수는 없고,
중력을 이용해서 이리 저리 굴려야 한다.

1) 왼쪽으로 기울이기,
2) 오른쪽으로 기울이기,
3) 위쪽으로 기울이기,
4) 아래쪽으로 기울이기와 같은 네 가지 동작


출력
# 시작하는 기울기에 따른 구멍에 빠지는 횟수가 바뀔
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다.
만약,
10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력

구슬이 움직이는 방향은 상 하 좌 우 총 4가지
최대 10번의 움직임만 고려
4의 10승 1048576 의 경우의 수중에서 가장 빠른것을 출력하면 된다.
보드가 최대 10*10이고,
한번의 기울임에 10번의 방향만 체크하면 되므로
1048576 * 10의 체크 필요

제한시간2초내에 가능

- 4방향이지만 가장 마지막의 움직임은 제외해야할듯, 같은 방향으로 움직이면 구슬이 움직이지 않는다.
- 이전과 반대방향으로 움직이면 그 이전의 위치와 동일해져서 움직일 필요가 없음
그래서 4*2^9인 2048의 경우의수
그래서 2048*10의 체크로 풀릴 수 있

큐를 이용해서 구슬의 위치를 매번 기억하고
다음 상태로 구슬의 위치를 이용시키면 문제가 쉽게 풀린다.

이전 구슬 위치를 모두 기록하여 이전에 구슬위치와 동일하면 큐에 넣지 않는다.(중복제거)
빨간구슬만 잘 움직이게 한다.
빨간골과 파란공은 같은위치에 있을 수 없음!

'''
'''
5 5
#####
#..B#
#.#.#
#RO.#
#####
'''





N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
dy = [-1, 1, 0, 0] # 상하좌우
dx = [0, 0, -1, 1]

def bfs(ry, rx, by, bx, cnt):
    visitied = [[0]*M for _ in range(N)]
    queue = []
    visitied[ry][rx] = 1
    visitied[by][bx] = 1
    queue.append((ry, rx, by, bx, cnt))
    ret = -1
    while queue:
        cur_ry, cur_rx, cur_by, cur_bx, cur_cnt = queue.pop(0)
        if cur_cnt > 10:
            break

        if board[cur_ry][cur_rx] == 'O' and board[cur_by][cur_bx] != 'O':
            print (cur_cnt)
            ret = cur_cnt
            return ret

        for dir in range(4):
            next_ry = cur_ry
            next_rx = cur_rx
            next_by = cur_by
            next_bx = cur_bx
            while 1:
                if board[next_ry][next_rx] != '#' and board[next_ry][next_rx] != 'O':
                    next_ry += dy[dir]
                    next_rx += dx[dir]
                else:
                    if board[next_ry][next_rx] == '#':
                        next_ry -= dy[dir]
                        next_rx -= dx[dir]
                    break
            while 1:
                if board[next_by][next_bx] != '#' and board[next_by][next_bx] != 'O':
                    next_by += dy[dir]
                    next_bx += dx[dir]
                else:
                    if board[next_by][next_bx] == '#':
                        next_by -= dy[dir]
                        next_bx -= dx[dir]
                    break

            if next_ry == next_by and next_rx == next_bx:
                if board[next_ry][next_rx] != 'O':
                    red_dist = abs(next_ry-cur_ry) + abs(next_rx-cur_rx)
                    blue_dist = abs(next_by-cur_by) + abs(next_bx-cur_bx)
                    if red_dist > blue_dist:
                        next_ry -= dy[dir]
                        next_rx -= dx[dir]
                    else:
                        next_by -= dy[dir]
                        next_bx -= dx[dir]
            if visitied[next_ry][next_rx] == 0 and visitied[next_by][next_bx] == 0:
                visitied[next_ry][next_rx] = 1
                visitied[next_by][next_bx] = 1
                queue.append((next_ry, next_rx, next_by, next_bx, cur_cnt + 1))
    return ret
ry = 0
rx = 0
by = 0
bx = 0
for y in range(N):
    for x in range(M):
        if board[y][x] == 'R':
            rx = x
            ry = y
        if board[y][x] == 'B':
            bx = x
            by = y
res = bfs(ry, rx, by, bx, 0)

print(res)




