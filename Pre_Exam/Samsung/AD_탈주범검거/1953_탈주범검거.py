import sys
sys.stdin = open('1953.txt', 'r')

'''
이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수를 계산
탈주범은 시간당 1의 거리를 움직일 수 있다.
지하 터널은 총 7 종류의 터널 구조물로 구성되어 있으며 각 구조물 별 설명은 [표 1]과 같다.



첫 줄에 총 테스트 케이스의 개수 T가 주어진다.
두 번째 줄부터 T개의 테스트 케이스가 차례대로 주어진다.
각 테스트 케이스의 첫 줄에는 지하 터널 지도의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.
그 다음 N 줄에는 지하 터널 지도 정보가 주어지는데, 각 줄마다 M 개의 숫자가 주어진다.
숫자 1 ~ 7은 해당 위치의 터널 구조물 타입을 의미하며 숫자 0 은 터널이 없는 장소를 의미한다.


# 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L
룩업테이블: 터널마다 갈 수 있는 길을 적어둔다
# R,C 부터 L만큼 돌아다니면서 지나가게된 경로를 바깥에 저장하고 마지막에 바깥에 저장된 길의 길이를 구한다.
# dfs 재귀돌린다.
'''

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
tunnel = {
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [1, 3],
    4: [0, 1],
    5: [1, 2],
    6: [2, 3],
    7: [0, 3]
}
nxt = {
    0: [1, 2, 5, 6],
    1: [1, 3, 6, 7],
    2: [1, 2, 4, 7],
    3: [1, 3, 4, 5]
}
T = int(input())
def solve(y, x, l):
    global vis
    path.add((y, x))
    if l == L-1:
        return
    for i in tunnel[board[y][x]]:
        dy, dx = d[i]
        iy = dy + y
        ix = dx + x
        if 0 <= iy < N and 0 <= ix < M and vis[iy][ix] == False:
            if board[iy][ix] in nxt[i]:
                vis[y][x] = True
                solve(iy, ix, l+1)
                vis[y][x] = False
for tc in range(1, T+1):
    N,M,R,C,L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    path = set()
    vis = [[False]*M for _ in range(N)]
    vis[R][C] = True
    solve(R, C, 0)

    print(f'#{tc} {len(path)}')
