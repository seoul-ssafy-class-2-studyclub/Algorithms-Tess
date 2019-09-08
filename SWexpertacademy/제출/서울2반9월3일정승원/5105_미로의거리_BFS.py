import sys
sys.stdin = open('5105.txt', 'r')

'''
#1 5
#2 5
#3 0
'''

d = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def Search(y, x):
    maze_visit = [ [False]*N for _ in range(N) ]
    queue = []
    res = 0
    queue.append((y, x, res))

    while queue:
        # 같은 단계에 있는 애들을 뽑아올때 카운트를 늘려준다.
        y, x, res = queue.pop(0)
        res += 1
        for dy, dx in d:
            iy = y + dy
            ix = x + dx
            if 0 <= ix < N and 0 <= iy < N:
                # 0이라면, 간다.
                if maze[iy][ix] == 0 and maze_visit[iy][ix] == False:
                    maze_visit[y][x] = True
                    queue.append((iy, ix, res))
                elif maze[iy][ix] == 3:
                    return res
    res = 0
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [ list(map(int, input())) for _ in range(N) ]
    # 2의 시작 인덱스를 발견
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                starty = y
                startx = x
                res = Search(starty, startx)
                break
    # print(starty, startx)
    # exist에 도착하면 탐색을 중지하고 res 반환
    #BFS로 시작해서 탐색하고 길에대한 경로를 카운트한다.
    if res == 0:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', res-1)

