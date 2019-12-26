## BFS


import heapq
import sys
sys.stdin = open('1175.txt', 'r')




def solve(status):
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    visit = [[False]*M for _ in range(N)]
    q = []
    # 시작의 status는 4가지 경우가 있다.
    heapq.heappush(q, (0, 0, minsik, status))
    while q:
        mins, Cs, current, status = heapq.heappop(q)
        cury, curx = current[0], current[1]

        if Cs == -2:
            return mins # -1을 해야 할 수도 있다.


        for i in range(4):
            if i != status:
                nxty, nxtx = direction[i][0], direction[i][1]
                if 0 <= nxty < N and 0 <= nxty < M and bd[nxty][nxtx] == False:
                    ##
                    pass

                    if pass:
                        pass







    return 1e9






N, M = map(int, input().split())
bd = [list(input()) for _ in range(N)]

print(N, M)
print(bd)

flag = True
for y in range(N):
    if flag:
        for x in range(M):
            if flag:
                if bd[y][x] == 'S':
                    minsik = (y, x)
                    bd[y][x] = '.'
                    flag = False

mymin = 1e9
for st in range(4):
    result = solve(st)
    if mymin > result:
        mymin = result


