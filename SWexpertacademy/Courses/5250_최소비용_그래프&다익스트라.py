import sys
sys.stdin = open('5250.txt', 'r')


def makegraph(y, x, name):
    global graph, land

    graph[(y, x, land[y][x])] = []

    for dy, dx in [(0, 1), (1, 0)]:
        iy = dy + y
        ix = dx + x

        if 0 <= iy < N and 0 <= ix < N:
            graph[(y, x, land[y][x])].append((iy, ix, land[iy][ix]))
    return


def start(y, x):




    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    land = [ list(map(int, input().split())) for _ in range(N) ]
    print(land)


    graph = {}
    # print(graph)
    point = 0
    for x in range(N):
        for y in range(N):
            makegraph(y, x, point)
            point += 1

    print(graph) # 만들 graph를 사용해서 start

    # 다익스트라
    # n-1, n-1 이 end-point이다.
    start(0, 0)


