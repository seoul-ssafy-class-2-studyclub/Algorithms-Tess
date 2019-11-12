import sys
sys.stdin = open('1868.txt','r')
import collections
def popping(y, x):
    global board
    q = collections.deque([])
    q.append((y, x, 0))
    while q:
        y, x, cnt = q.pop()
        for dy, dx in near:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < N and board[iy][ix] == '*':
                cnt += 1
        board[y][x] = str(cnt)
        if board[y][x] == '0':
            for dy, dx in near:
                iy = dy + y
                ix = dx + x
                if 0 <= iy < N and 0 <= ix < N and board[iy][ix] == '.':
                    q.append((iy, ix, 0))

near = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]
    clicked = 0
    for y in range(N):
        for x in range(N):
            cnt = 0
            for dy, dx in near:
                iy = dy + y
                ix = dx + x
                if 0 <= iy < N and 0 <= ix < N and board[iy][ix] == '*':
                    cnt += 1
                    break
            if cnt == 0 and board[y][x] == '.':
                board[y][x] = str(cnt)
                popping(y, x)
                clicked += 1
    for y in range(N):
        for x in range(N):
            if board[y][x] == '.':
                clicked += 1
    print(f'#{tc} {clicked}')



'''
def opn(ls, x, y):
    if ls[x][y] != '*':
        near = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        cnt = 0
        for a, b in near:
            if 0 <= x+a < len(ls) and 0 <= y+b < len(ls):
                if ls[x+a][y+b] == '*':
                    cnt += 1
        ls[x][y] = cnt

def click(ls, x, y):
    A = ls[x][y]
    if ls[x][y] != '*':
        ls[x][y] = 'X'
    near = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    if A == 0:
        for a, b in near:
            if 0 <= x+a < len(ls) and 0 <= y+b < len(ls):
                click(ls, x+a, y+b)
def check_dot(bd):
    rs = 0
    for i in bd:
        rs += i.count('.')
    if rs == 0:
        return False
    else:
        return True
for T in range(int(input())):
    N = int(input())
    bd = []
    for i in range(N):
        row = [i for i in input()]
        bd.append(row)
    while check_dot(bd):
        for x in range(len(bd)):
            for y in range(len(bd)):
                if bd[x][y] == '.':
                    # print(x,y)
                    opn(bd, x, y)
    cnt = 0
    for x in range(len(bd)):
        for y in range(len(bd)):
            if bd[x][y] == 0:
                cnt += 1
                click(bd, x, y)
    for x in range(len(bd)):
        for y in range(len(bd)):
            if type(bd[x][y]) == int:
                bd[x][y] == 'X'
                cnt += 1 
    print(f'#{T+1} ',end='')
    print(cnt)

'''