import sys
sys.stdin = open('4991.txt', 'r')
input = sys.stdin.readline
import itertools
from pprint import pprint
# Travelling salesman problem
'''
로봇 청소기는 더러운 칸(*)을 방문해서 깨끗한 칸(.)으로 바꿀 수 있다.
일부 칸에는 가구가 놓여져 있고, 가구의 크기도 1×1이다. 로봇 청소기는 가구가 놓여진 칸으로 이동할 수 없다. 
로봇은 한 번 움직일 때, 인접한 칸으로 이동할 수 있다. 또, 로봇은 같은 칸을 여러 번 방문할 수 있다.
방의 정보가 주어졌을 때, 더러운 칸을 모두 깨끗한 칸으로 만드는데 필요한 이동 횟수의 최솟값
-> BFS
.: 깨끗한 칸
*: 더러운 칸
x: 가구
o: 로봇 청소기의 시작 위치
'''

def solve(y, x, board, sty, stx):
    global tc
    q = []
    visited = [[False]*w for _ in range(h)]
    # visited[y][x] = True
    q.append((y, x, 1, visited))
    while q:
        y, x, move, visit = q.pop(0)
        if visit[y][x] == False:
            visit[y][x] = True
            for dy, dx in [(0,1), (1,0), (-1,0), (0,-1)]:
                nvisit = [i[:] for i in visit]
                iy = y + dy
                ix = x + dx
                if 0 <= iy < h and 0 <= ix < w:
                    if board[iy][ix] == '.':
                        q.append((iy, ix, move+1, nvisit))
                        # print('----', tc)
                        # pprint(nvisit)
                    if iy == sty and ix == stx:
                        # print('----')
                        return move, sty, stx
    return -1, -1, -1

for tc in range(1,4):
    # 가로 w 세로 h
    w, h = map(int, input().split())
    board = [list(map(str, input())) for _ in range(h)]
    # 찾을것
    # 로봇의 위치
    y = x = 0
    # 더러운 칸의 개수
    dirty = 0
    dirtyyx = []

    for hy in range(h):
        for wx in range(w):
            if board[hy][wx] == '*':
                dirty += 1
                dirtyyx.append((hy, wx))
            if board[hy][wx] == 'o':
                board[hy][wx] = '.'
                y = hy
                x = wx
    INF = float('inf')
    distance = [[INF]*(dirty+1) for _ in range(dirty+1)]
    permut = list(itertools.permutations(dirtyyx, dirty))
    resmin = []
    for startpoint in permut:
        # permut를 하나씩 꺼내면서,
        ny = y
        nx = x
        mymin = 1e9
        myminsum = 0
        for starty, startx in startpoint:
            # print(startpoint)
            # print(ny, nx)
            # 가장빨리 발견한게 답이므로
            movecnt, ny, nx = solve(ny, nx, board, starty, startx)
            # print(ny, nx)
            myminsum += movecnt
        resmin.append(myminsum)
    print(min(resmin))
    # 더러운 칸의 개수가 0이 되지 않으면 -1 출력할 것
    # 직접 경로를 설정하면서 가장 이동횟수가 최소일때의 경우를 찾는다.
    # 즉 더러운 칸의 개수가 0이 될때 그만 청소하고 이동횟수를 리턴하면 된다.
    # 그러면 bfs를 돌면서 4방향을 다 들어간다.
st, sy = map(int, input().split())


