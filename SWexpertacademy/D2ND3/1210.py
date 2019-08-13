import sys
sys.stdin = open('1210.txt', 'r')


for _ in range(10):
    T = int(input())
    N = 100

    # 2 차원 배열
    mat = []
    for _ in range(N):
        row = list(map(int, input().split()))
        mat.append(row)

    goal_index = mat[99].index(2) # 1tc에서는 57번째 index에 2가 있다.
    #print(goal_index)


    all_directions = [[0, 1],[0, -1],[-1, 0]]

    tempdy = 99
    tempdx = goal_index

    while tempdy >= 0: ######## 실수: while문 제어

        if tempdy == 0:
            print(f'#{T}',tempdx)  # 여기까지 안온다.
            break

        elif tempdx == 0:
            #print(tempdx)
            for (dy, dx) in [[0, 1], [-1, 0]]:
                if mat[tempdy+dy][tempdx+dx] == 1:
                    mat[tempdy + dy][tempdx + dx] += 2
                    tempdy = tempdy + dy
                    tempdx = tempdx + dx

        elif tempdx == 99:
            #print(tempdx)
            for (dy, dx) in [[0, -1], [-1, 0]]:
                if mat[tempdy + dy][tempdx + dx] == 1:
                    mat[tempdy + dy][tempdx + dx] += 2
                    tempdy = tempdy + dy
                    tempdx = tempdx + dx

        elif 1 <= tempdx < 99: # 1~98
            #print(tempdx)
            for (dy, dx) in all_directions:
                if mat[tempdy + dy][tempdx + dx] == 1:
                    mat[tempdy + dy][tempdx + dx] += 2
                    tempdy = tempdy + dy
                    tempdx = tempdx + dx



'''
near = [(0, -1), (0, 1), (-1, 0)]
def ladder_orgi(y, x, ladder):
    if y != 1:
        for dy, dx in near:
            if y + dy == 0: #여기서 걸려서 실행 안되고 아래의 if들을 태운다
                return x

    if x == 99:
        for dy, dx in [(0, -1), (-1, 0)]:
            if ladder[y + dy][x + dx] == 1:
                ladder[y][x] = 3
                return ladder_orgi(y + dy, x + dx, ladder)

    if x == 0:
        for dy, dx in [(0, 1), (-1, 0)]:
            if ladder[y + dy][x + dx] == 1:
                ladder[y][x] = 3
                return ladder_orgi(y + dy, x + dx, ladder)

    for dy, dx in near:
        if ladder[y + dy][x + dx] == 1:
            ladder[y][x] = 3
            return ladder_orgi(y + dy, x + dx, ladder)


for rounds in range(1, 11):
    ladder = []
    ro = int(input())
    for i in range(100):
        ladder.append(list(map(int, input().split())))

    for i in range(100):
        if ladder[99][i] == 2:
            exit_index = i
    print(f'#{rounds} {ladder_orgi(99, exit_index, ladder)}')



for case in range(1, 11):
    board = []
    N = int(input())
    for row in range(100):
        board.append(list(map(int, input().split())))
    j = board[99].index(2)
    for i in range(99, 0, -1):
        if j != 0 and board[i][j-1]:
            while j > 0 and board[i][j-1]:
                j -= 1
        elif j != 99 and board[i][j+1]:
            while j < 99 and board[i][j+1]:
                j += 1

    print(f'#{case} {j}')


'''