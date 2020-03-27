'''
3
7
8
9
'''

import sys
sys.stdin = open('2667.txt', 'r')


def change(iy, ix):
    cnt = 0
    stack = []
    stack.append((iy, ix)) # 처음 1을 만난 iy, ix 부터 시작하기 위해 스택에 넣는다.
    #print(stack)

    while len(stack) > 0: # stack의 길이가 []가 될때까지, 아래를 실행
        iy, ix = stack.pop()

        if board[iy][ix] != 0: # 문제해결: 1면 pop한 iy, ix는 버려진다. (중복이기때문에)
            board[iy][ix] = 0
            cnt += 1

            if 0 < ix < (N-1) and 0 < iy < (N-1):
                for y, x in all_direction:
                    tempx = x+ix
                    tempy = y+iy
                    if board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))

            if (N-1) == ix and (N-1) == iy:
                for y, x in [[0, -1], [-1, 0]]:
                    tempx = x + ix
                    tempy = y + iy
                    if board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))

            if 0 == ix and 0 == iy:
                for y, x in [[0,1], [1,0]]:
                    tempx = x + ix
                    tempy = y + iy
                    if board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))

            if (N-1) == ix and 0 == iy:
                for y, x in [[0, -1], [1, 0]]:
                    tempx = x + ix
                    tempy = y + iy
                    if board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))

            if 0 == ix and (N-1) == iy:
                for y, x in [[-1, 0], [0, 1]]:
                    tempx = x + ix
                    tempy = y + iy
                    if board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))

            if 0 < ix < (N-1) and 0 == iy:
                for y, x in [[0, -1], [1,0], [0, 1]]:
                    tempx = x + ix
                    tempy = y + iy
                    if board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))

            if 0 < iy < (N-1) and 0 == ix:
                for y, x in [[-1, 0], [1,0], [0, 1]]:
                    tempx = x + ix
                    tempy = y + iy
                    if board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))

            if 0 < iy < (N-1) and (N-1) == ix:
                for y, x in [[-1, 0], [0,-1], [1, 0]]:
                    tempx = x + ix
                    tempy = y + iy
                    if board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))

            if (N-1) == iy and 0 < ix < (N-1):
                for y, x in [[0, -1], [-1,0], [0, 1]]:
                    tempx = x + ix
                    tempy = y + iy
                    if board[tempy][tempx] == 1:
                        stack.append((tempy, tempx))

    return cnt


def check():
    cnt = 0
    for iy in range(N):
        for ix in range(N):
            if board[iy][ix] == 0:
                cnt += 1
                if cnt == (N*N):
                    return False
            else:
                return True



N = int(input())
board = [list(map(int, input())) for _ in range(N)]
all_direction = [[-1,0], [0,-1], [1,0], [0,1]]

houses = 0
flag = True
number_of_houses = []
while flag == True:
    for iy in range(N):
        if flag == False:
            break
        for ix in range(N):
            if board[iy][ix] == 1:
                res = change(iy, ix)
                number_of_houses.append(res)
                houses += 1
                flag = check()
                if flag == False:
                    break

print(houses)
for res in sorted(number_of_houses):
    print(res)




'''
범위를 한 번에 조절가능
adj = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]] 
 def checkIsland(i,j):                   # i,j에 대해 그 주변을 조사하여 같은 섬인 땅을 같은 숫자로 표시해주는 함수
        base_list[i][j] = -(cnt+1)
        for [dx,dy] in adj:
            if 0 <= i+dx < N and 0 <= j+dy < N and base_list[i+dx][j+dy] > 0:
                base_list[i+dx][j+dy] = -(cnt+1)
                checkIsland(i+dx, j+dy)

'''