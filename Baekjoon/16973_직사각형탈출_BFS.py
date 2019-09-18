'''
import sys
# sys.stdin = open('16973.txt', 'r')
# import collections



# 런타임에러, 메모리초과 발생/ recursion 없는 bfs로 재구현 필요


# 2. 꾸러미 안의 각 yx는 또 다른 꾸러미들을 만들 수 있는 후보가 된다.
# 2-1. 부모 후보들은 False인 상태여야 하며, 1이 있으면 안된다.
# 2-2. 모든걸 충족한 부모후보들은 자식후보를 낳는데, startij만들듯, 자식후보들 중에
# 3. 새로 생기는 꾸러미의 원소 중에 1이 있는 건 버린다.

# 4. 0만있는 완전한 꾸러미임이 확인되면,
# 5. 해당 부분중에 기준이 되는 왼쪽위만 visit처리하고, 다음 재귀에 추가, temp += 1
# 6. 다시 돌아올때의 가지치기 필요
sys.setrecursionlimit(10**9)

def BFS_recursion(i, j, tem, teml=[]):
    global my_min
    global visited

    if tem > my_min: # 가지치기, 종료조건
        return True

    # for idx in range(len(ij)):

    if i == Fr-1 and j == Fc-1:
        if my_min >= tem:
            my_min = tem
            return True

    elif board[i][j] == 0: # 가능한 부모
        for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
            iy = dy + i
            ix = dx + j

            if 0 <= iy < N-H+1 and 0 <= ix < M-W+1 and not visited[iy][ix]:
                # 완전히 선택된 부모

                # 자식낳기 시작
                # 낳은 자식 검열 후 리스트에 추가

                teml = []
                for idxi in range(iy, iy+H): #
                    for idxj in range(ix, ix+W):
                        if board[idxi][idxj] == 0:
                            teml.append((idxi, idxj))
                # print(teml)

                if len(teml) == H*W:
                    visited[iy][ix] = True
                    tem += 1
                    BFS_recursion(iy, ix, tem, teml)
                    visited[iy][ix] = False
                # 리스트 len이 H*W라면, 가능한 꾸러미
                # 재귀로 보내기, 보내기전에 가능한 부모는 vis에 표시


N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N)] # N cols M rows
H, W, Sr, Sc, Fr, Fc = map(int, input().split())

# 1. 초기 시작 좌표 꾸러미 생성
# startij = []
# for i in range(H):
#     for j in range(W):
#         startij.append((i,j)) # 처음에 항상 순서대로 들어옴

my_min = 999999

visited = [[False]*M for _ in range(N)]
temp = 0
# visited[0][0] = True

BFS_recursion(Sr-1, Sc-1, temp, visited)

if my_min == 999999:
    print(-1)
else:
    print(my_min)
'''



from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, stdin.readline().split())
Sr -= 1
Sc -= 1
Fr -= 1
Fc -= 1
walls = []
res = -1
for r in range(N): # 1. wall에 대한 모든 좌표를 담는다.
    for c in range(M):
        if board[r][c] == 1:
            walls.append((r, c))

queue = deque([(Sr, Sc, 0)])
board[Sr][Sc] = -1
while queue:
    y, x, cnt = queue.popleft()
    if y == Fr and x == Fc:
        res = cnt
        break
    for b, a in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        yi = y + b
        xi = x + a
        if 0 <= yi and yi + H - 1 < N and 0 <= xi and xi + W - 1 < M and not board[yi][xi]:
            flag = True
            for wy, wx in walls:
                if yi <= wy < yi + H and xi <= wx < xi + W:
                    flag = False
                    break
            if flag == True: # True라면,
                queue.append((yi, xi, cnt+1))
            board[yi][xi] = -1
print(res)