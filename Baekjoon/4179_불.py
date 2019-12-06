'''

입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.
다음 입력으로 R줄동안 각각의 미로 행이 주어진다.
각각의 문자들은 다음을 뜻한다.
#: 벽
.: 지나갈 수 있는 공간
J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
F: 불이난 공간
J는 입력에서 하나만 주어진다.


지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는경우 IMPOSSIBLE 을 출력한다.
지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.
'''

import sys
sys.stdin = open('4179.txt', 'r')
# from collections import deque
# N, M = map(int, input().split())
# room = [ list(input()) for _ in range(N) ]
#
# def findExit(jy, jx):
#     global room
#     stack = []
#     stack.append((jy, jx))
#     visit = [[False]*M for _ in range(N)]
#     visit[jy][jx] = True
#     while stack:
#         jy, jx = stack.pop()
#         for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
#             iy = dy + jy
#             ix = dx + jx
#             if ix < 0 or ix >= M or iy < 0 or iy >= N:
#                 return 'Try'
#             # if iy == 0 and 0 <= ix <= M-1 and room[iy][ix] == '.' and visit[iy][ix] == False:
#             #     #           0, 1, 2, 3
#             #     return 'Try'
#             # elif 1 <= iy < N-1 and (ix == 0 or ix == M-1) and room[iy][ix] == '.' and visit[iy][ix] == False:
#             #     #   1, 2
#             #     return 'Try'
#             # elif iy == N-1 and 0 <= ix <= M-1 and room[iy][ix] == '.' and visit[iy][ix] == False:
#             #     return 'Try'
#             elif 0 <= iy < N and 0 <= ix < M:  # 위의 경우가 모두 아닌 경우
#                 if room[iy][ix] == '.' and visit[iy][ix] == False:
#                     visit[iy][ix] = True
#                     stack.append((iy, ix))
#     return 'IMPOSSIBLE'
#
#
# def solve(room, J, F, fvisit):
#     # fvisit = [[False] * M for _ in range(N)] # 지훈이가 움직인 곳으로 확정된 곳
#     jq = J
#     fq = F
#     while jq:
#
#         # 불
#         if len(fq) != 0:
#             for _ in range(len(fq)):
#                 ffy, ffx = fq.popleft()
#                 room[ffy][ffx] = 'F'
#                 fvisit[ffy][ffx] = True
#                 for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
#                     fx = dx + ffx
#                     fy = dy + ffy
#                     if 0 <= fy < N and 0 <= fx < M and fvisit[fy][fx] == False and (room[fy][fx] == '.' or room[fy][fx] == 'J'):
#                         fvisit[fy][fx] = True
#                         fq.append((fy, fx))
#
#         # 지훈이
#         # BFS 이므로 도착하면 그냥 바로 return
#         for _ in range(len(jq)):
#             jjy, jjx, cnt = jq.popleft()
#             for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
#                 jy = dy + jjy
#                 jx = dx + jjx
#                 if jx < 0 or jx >= M or jy < 0 or jy >= N:
#                     return cnt
#                 # if jy == 0 and 0 <= jx <= M-1 and room[jy][jx] == '.':
#                 #     #           0, 1, 2, 3
#                 #     return cnt
#                 # elif 1 <= jy < N-1 and (jx == 0 or jx == M-1) and room[jy][jx] == '.':
#                 #     #   1, 2
#                 #     return cnt
#                 # elif jy == N-1 and 0 <= jx <= M-1 and room[jy][jx] == '.':
#                 #     return cnt
#                 elif 0 <= jy < N and 0 <= jx < M: # 위의 경우가 모두 아닌 경우
#                     if room[jy][jx] == '.' and fvisit[jy][jx] == False:
#                         room[jy][jx] = 'J'
#                         fvisit[jy][jx] = True
#                         jq.append((jy, jx, cnt + 1))
#
#     return 'IMPOSSIBLE'
#
#
# J = deque([])
# F = deque([])
# # 불은 하나가 아닐 수도 있다.
# visit = [[False] * M for _ in range(N)]
#
# for y in range(N):
#     for x in range(M):
#         if room[y][x] == 'J':
#             J.append((y, x, 1))
#             visit[y][x] = True
#         if room[y][x] == 'F':
#             F.append((y, x))
#             visit[y][x] = True
# branch = findExit(J[0][0], J[0][1])
# if branch == 'Try':
#     ans = solve(room, J, F, visit)
#     print(ans)
# elif branch == 'IMPOSSIBLE':
#     print(branch)
#
#

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
room = [ list(input()) for _ in range(N) ]

def solve(room, J, F, fvisit):
    jq = J
    fq = F
    while jq:

        # 불
        if len(fq) != 0:
            for _ in range(len(fq)):
                ffy, ffx = fq.popleft()
                room[ffy][ffx] = 'F'
                fvisit[ffy][ffx] = True
                for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
                    fx = dx + ffx
                    fy = dy + ffy
                    if 0 <= fy < N and 0 <= fx < M and fvisit[fy][fx] == False and (room[fy][fx] == '.' or room[fy][fx] == 'J'):
                        fvisit[fy][fx] = True
                        fq.append((fy, fx))

        # 지훈이
        # BFS 이므로 도착하면 그냥 바로 return
        for _ in range(len(jq)):
            jjy, jjx, cnt = jq.popleft()
            for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
                jy = dy + jjy
                jx = dx + jjx
                if jx < 0 or jx >= M or jy < 0 or jy >= N: # 이 부분 범위조절 기억
                    return cnt
                elif 0 <= jy < N and 0 <= jx < M: # 위의 경우가 모두 아닌 경우
                    if room[jy][jx] == '.' and fvisit[jy][jx] == False:
                        room[jy][jx] = 'J'
                        fvisit[jy][jx] = True
                        jq.append((jy, jx, cnt + 1))

    return 'IMPOSSIBLE'

J = deque([])
F = deque([])
# 불은 하나가 아닐 수도 있다.
visit = [[False] * M for _ in range(N)]
for y in range(N):
    for x in range(M):
        if room[y][x] == 'J':
            J.append((y, x, 1))
            visit[y][x] = True
        if room[y][x] == 'F':
            F.append((y, x))
            visit[y][x] = True
ans = solve(room, J, F, visit)
print(ans)