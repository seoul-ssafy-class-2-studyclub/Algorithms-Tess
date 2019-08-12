import sys
sys.stdin = open('1210.txt', 'r')



def Search(x, y, num = 100):

    corner = 0

    while num > 0:
        if mat[x][y - 1] == 1:  # 1 == 1
            y = y - 1
            x = x
            num -= 1
            return Search(x, y)

        if mat[x][y + 1] == 1:  # 1 == 1
            y = y + 1
            x = x
            num -= 1
            return Search(x, y)

        if mat[x -1][y] == 1:  # 1 == 1
            y = y
            x = x -1
            num -= 1
            return Search(x, y)


for tc in range(10):
    T = int(input())
    N = 100

    # 2 차원 배열
    mat = []
    for n in range(N):
        row = list(map(int, input().split()))
        mat.append(row)

    find_index = 2
    print(mat[-1])
    goal_point = mat[-1].index(find_index) # 1tc에서는 57번째 index에 2가 있다.

    start_point = mat[-2][goal_point] # 반드시 1일 것


    res = Search(-2, goal_point)

