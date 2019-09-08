import sys
sys.stdin = open('2105_디저트카페.txt', 'r')

# 이동방향은 대각선
# 사각형 모양을 그리면서 출발한다



# 하나의 카페만 있는 것도 안된다
# 왔던 길을 돌아가는 것도 안된다.

# 시작점을 임의로 정해서
# 대각선 방향으로 움직인다.
# 그러고 나서 움직인후 출발점으로 돌아오는 경우에서 가장 많이 먹을 수 있는 경로
# 그 경로가 가진 디저트 수의 합

# 모든 경로가 불가능할땐  -1


# 이동방향은 항상 다를 수 있다.
# 오른쪽 아래 대각선, 왼쪽 아래 대각선, 왼쪽 위 대각선, 오른쪽 위 대각부터 시작해서
# 다르게도 돌 수 있다.

# 즉, 같은 지점을 기준으로 네번을 돌필요는 없다.이렇게 도나 저렇게 도나 똑같으니까.

# 탐색한 경로값을 저장하고,
# 이후 탐색할 경로 이전 경로보다 짧으 더 살펴보지 않고 다음으로 넘긴다.


# 노드를 뽑아올 수 있음
def node(y, x):
    # node 생성기
    for idx in range(4):
        iy = y + dy[idx]  # [idx-idx_add]
        ix = x + dx[idx]  # [idx-idx_add]
        if 0 <= iy < N and 0 <= ix < N:
            # print(cafes[iy][ix])
            return cafes[iy][ix]

def adj_list_creation(y, x):
    global cafes
    global adj_list
    # adj_list = [[]*11 for _ in range(11)]
    # print(cafes[y][x])
    adj_list[cafes[y][x]].append(node(y, x))
    return adj_list

def move(s, adj):
    global cafes

    visit_order = []
    stack = []
    stack.append(s)

    while stack:
        temp = []
        for q in range(len(stack)):
            node = stack.pop()
            print(node)
            if visited[node] == 0:
                visited[node] = 1
                print(node)
                stack.extend(adj[node])
                temp.append(node)
        visit_order.append(temp)
    return visit_order

dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    adj_list = [[] * 11 for _ in range(11)]
    N = int(input())
    cafes = [ list(map(int, input().split())) for _ in range(N) ]
    visited = [0 for _ in range(N*N)]
    res = -1

    # 이동거리에는 중복되 숫자가 있으면 안된다.
    # 중복된 숫자를 가진카페를 들리지 않기위해 표시하는 배열 생성

    # N, 0  N, N  0, N  0, 0 은 시작 지점이 될 수 없다.
    for Y in range(N):
        for X in range(N):
            adj_list = adj_list_creation(Y, X)

            print(adj_list)
            # [[], [], [], [7], [7, 7, 7], [8, 7], [7], [3, 5], [9, 9, 5, 3], [6, 4, 8], []]
            res = move(cafes[Y][X], adj_list)
    print(res)






