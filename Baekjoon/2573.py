import sys
sys.stdin = open('2573.txt', 'r')

import copy


def change(iy, ix):

    visit_board = copy.deepcopy(board)
    queue = []
    queue.append((iy, ix))
    ########## visit_board 배열ㅅㅅ : visit한곳은 'V' = visited했다고 바꾸고,
    # 원래 board에서 양수만 처리한다.

    while len(queue) >= 0:
        iiy, iix = queue.pop(0)
        # 0, 0
        if board[iiy][iix] == 0:
            for dy, dx in directions:
                # 0, -1  =
                tempy, tempx = iiy + dy, iix + dx
                if 0 <= tempx < N and 0 <= tempy < N: # 0이 아니고 양수라면 추가
                    if board[tempy][tempx] > 0:
                        board[tempy][tempx] -= 1
                    if board[tempy][tempx] == 0:
                        queue.append((tempy, tempx))


# board를 아예 슬라이싱으로 따로 복사해본후
# 0보다 큰수의 덩어리를 아예 0으로 만들어서 없애면서
#체크
def check_in(iiy, iix):

    #board를 new_board로 만들어서 체크
    stack2 = []
    stack2.append((iiy, iix))
    while len(stack2) >= 0:
        iiy, iix = stack2.pop()
        if iiy == (N-1) and ix == (M-1):
            return 0

        if board[iiy][iix] != 0:  # 문제해결: 1면 pop한 iy, ix는 버려진다. (중복이기때문에)
            board[iiy][iix] = 0
            for dy, dx in directions:
                iiy, iix = iiy + dy, iix + dx
                if 0 <= iix < N and 0 <= iiy < N and board[iiy][iix] >= 1:
                    if board[iiy][iix] == 0:
                        stack2.append((iiy, iix))
    return 1


def check(arr):

    flag2 = True
    cnt = 0

    while flag2 == True:
        for iy in range(N):
            if iy == (N - 1) and ix == (M - 1):
                flag2 = False
                break

            for ix in range(M):
                if board[iy][ix] > 0:
                    cnt += check_in(iy, ix)
                    if iy == (N-1) and ix == (M-1):
                        flag2 = False
                        break


    return cnt



# 행, 열
N, M = 5, 7 # map(int, input().split())
board = [[0, 0, 0, 0, 0, 0, 0], [0, 2, 4, 5, 3, 0, 0], [0, 3, 0, 2, 5, 2, 0], [0, 7, 6, 2, 4, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


# [list(map(int, input().split())) for _ in range(N)]

directions = [[0,-1],[-1,0],[1,0],[0,1]]

flag = True
year = 0

while flag == True:
    for iy in range(N):
        if flag == False:
            break

        for ix in range(M):
            if board[iy][ix] == 0:
                res1 = change(iy, ix) #한 번 보드를 싹 돌면서 바꿔줄 함수
                year += 1 # change함수가 시작되면 year이 늘어난다.

                res2 = check(board) # 몇개의 빙산이 있는지 확인하는 함수
                if res2 == 0:
                    res2 = 0
                    flag = False
                    break

                if res2 > 1:
                    res2 = res2
                    flag = False
                    break
print(year, res2)






