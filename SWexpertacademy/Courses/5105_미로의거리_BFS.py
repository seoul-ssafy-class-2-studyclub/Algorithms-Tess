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
    queue.append((y, x, res)) # 처음부터 좌표와 카운트할 res를 같이 보내준다.

    while queue:
        # 같은 단계에 있는 애들을 뽑아올때 카운트를 늘려준다.
        y, x, res = queue.pop(0)
        res += 1
        for dy, dx in d:
            iy = y + dy
            ix = x + dx
            # 범위처리
            if 0 <= ix < N and 0 <= iy < N:
                # 0이라면, 간다.
                # visit한 곳이 아니라면 간다.
                if maze[iy][ix] == 0 and maze_visit[iy][ix] == False:
                    maze_visit[y][x] = True
                    queue.append((iy, ix, res)) # 성공적으로 넣어지는 경우의 res가 넣어질 것
                elif maze[iy][ix] == 3: # 3에 도착했다는 것은 도착점에 왔다는 것이므로 카운트 결과를 반환
                    return res
    # 큐에서 모든게 빠져나왔다면 여태까지 카운트 한것은 의미가 없으므로
    # 0으로 바꿔 반환
    res = 0
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [ list(map(int, input())) for _ in range(N) ]
    # 2의 시작 인덱스를 발견
    # 보드를 전체 돌면서 시작 인덱스를 찾아 전달한다.
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                starty = y
                startx = x
                res = Search(starty, startx)
                break # 해당 케이스에서 2를 가진건 한 경우이므로 메모리를 아끼기 위해서 찾고 함수를 호출하면 바로 break해서 포문을 빠져나온다.
    # print(starty, startx)
    # exist에 도착하면 탐색을 중지하고 res 반환
    # BFS로 시작해서 탐색하고 길에대한 경로를 카운트한다.
    if res == 0:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', res-1)

