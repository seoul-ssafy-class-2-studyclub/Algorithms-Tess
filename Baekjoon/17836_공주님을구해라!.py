import sys
# sys.stdin = open('17836.txt', 'r')

input = sys.stdin.readline
import collections

def solve():
    global maze, T
    q = collections.deque([])
    q.append((SY, SX, 0))
    maze[SY][SX] = 1
    ans = 1e9
    comp = 1e9
    goal = 0

    while q:

        for _ in range(len(q)):
            sy, sx, cnt = q.popleft()

            if sy == EY and sx == EX:
                ans = cnt
                goal = 1
                return goal, comp, ans

            if T + 1 < cnt: # 그냥 cnt가 temp를 넘는지 관리필
                if goal == 0:
                    return goal, comp, ans

            for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                iy = dy + sy
                ix = dx + sx
                if 0 <= iy < N and 0 <= ix < M:
                    if maze[iy][ix] == 2:  # 2면, 뚫고 갈 수 있는 시간중 가장 짧은 시간을 바로 찾을 수 있다.
                        maze[iy][ix] = 1

                        # 정리
                        if comp == 1e9:  # 1을 뚫고가는 가장 빠른길
                            temp = abs(iy - EY) + abs(ix - EX) + cnt + 1

                            if T + 1 >= temp: # temp가 t를 넘는지 관리필
                                comp = temp
                                goal = 1

                        q.append((iy, ix, cnt + 1))  # 2를 얻고 0만 갈 수 있기 때문에

                    if maze[iy][ix] == 0:  # 0인 길만 갈 수 있다.
                        maze[iy][ix] = 1
                        q.append((iy, ix, cnt + 1))

    return goal, comp, ans

# y, x, 제한시간
N, M, T = map(int, input().split())
maze = [ list(map(int, input().split())) for _ in range(N) ]
EY = N-1
EX = M-1
SY = 0
SX = 0
goal, comp, ans = solve()

if goal:
    print(min(comp, ans))
else:
    print('Fail')
