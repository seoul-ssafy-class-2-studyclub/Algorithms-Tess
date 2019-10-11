import sys
sys.stdin = open('11559.txt', 'r')
from pprint import pprint

#1~2까지는 q로 진행되며, visited를 사용
#1. '.'이 아닌 것들을 모두 startcnt한다.
#1-1. 맨 아래에서 부터 상하좌우로 봤을때 4개 이상 연결되어있는 경우, 1) 같은 색이여야한다.
#2. 빠져나왔을때, 담은 좌표들을 터트린다. 터트리면서 startcnt를 -1하고, 해당 부분을 '.'으로 수정한다.
#2-2. 한 판안에서 한 집합을 터트렸을때, True를 반환하여 밖에서 crash += 1을 한다.

#3. 그리고 다시 또 새로운 시작점을 잡는다. 이때 시작점은 R, B, P, Y 중 하나일 것
#4. 모든 곳을 다 돌았을때,
#4-1. 한 판을 돌아서, crash를 한 번이라도 했다면, turn += 1을 해준다.

#5. 보드에서 세로로 보면서 위에 발견을 하면, 내 q에 넣고 보드에 맨 아래에서 부터 추가한다.

#6. 중력으로 인해 새로 짜진 보드에서 모든 보드가 없어졌는지 startcnt가 0이면 while문을 종료시켜서 끝내고,
#7. *or* 그렇지 않고 모두 끝낼 수 없는 판일때는, 모두 다돌았을때 터트릴 수 있는게 하나도 없었을것이므로,
# 한 판에서 터트린 집합의 수가 0인 상태로 리턴되어 while문을 종료시킨다.

# 12*6
# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑

import sys
import collections
input = sys.stdin.readline

def findmorethanfour(Y, X):
    global gameboard, startcnt, visited

    q = collections.deque([])
    q.append((Y, X))
    color = gameboard[Y][X]
    visited[Y][X] = True

    candidates = [(Y, X)]
    candidatescheck = 1
    while q:
        y, x = q.popleft()
        for iy, ix in [(0,1), (1,0), (0,-1), (-1, 0)]:
            dy, dx = iy + y, ix + x
            if 0 <= dy < 12 and 0 <= dx < 6 and visited[dy][dx] == False and gameboard[dy][dx] == color:
                visited[dy][dx] = True
                candidatescheck += 1
                q.append((dy, dx))
                candidates.append((dy, dx))

    if candidatescheck >= 4:
        for candidate in candidates:
            gameboard[candidate[0]][candidate[1]] = '.'
            startcnt -= 1
        return True
    return False



def newboard():
    global gameboard

    paints = []
    for x in range(5, -1, -1):
        for y in range(12):
            if gameboard[y][x] != '.':
                paints.append((gameboard[y][x]))
                gameboard[y][x] = '.'

        for y in range(11, -1, -1):
            if paints:
                colour = paints.pop()
                gameboard[y][x] = colour
    return


gameboard = [ list(input()) for _ in range(12) ]
startcnt = 0
for y in range(12):
    for x in range(6):
        if gameboard[y][x] != '.':
            startcnt += 1

turn = 0

while True:
    # (11, 5), (11, 4), (11, 3) 순으로 (0, 0) 까지 본다.

    crash = 0
    visited = [ [False]*6 for _ in range(12) ]
    for y in range(11, -1, -1):
        for x in range(5, -1, -1):
            if gameboard[y][x] != '.':
                check = findmorethanfour(y, x)
                if check == True:
                    crash += 1
    if crash != 0:
        turn += 1


    newboard()

    if startcnt == 0:
        break
    elif crash == 0:
        break

print(turn)
