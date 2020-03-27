## 백트래킹 : 주어진 문제의 답을 구하기 위해 현재 상태에서 가능한 모든 후보군에 따라 들어가며 탐색하는 알고리
# 1. 시작점의 좌표를 구한다.
# 2. 해당 좌표에 후보 번호(1-9)들을 넣어본다. 이때 행과 열을 보면서 가능한지 False or True
# 3. 후보 번호들을 넣으면서 맞는 번호가 있으면 temperately fix 한다.
# 4. 반복하다가
'''
# 5. [Backtracking] False가 나오는 경우가 있으면 Backtracking을 시작한다.
현재위치에서 이전에 했던 것을 지우고 
이전 위치에서 넣었던 번호를 제외하고 가능한 번호를 넣는다. 
만약 그것도 잘 되지 않는다면,
그 이전 위치에서 더 이전 위치에서 해당 검사를 반복한다.
'''



import sys
sys.stdin = open('2580.txt', 'r')
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# main, inside of itself
def solve(bo):
    find = find_empty(bo)  # 시작점에서 가능한 곳인지 확인
    if not find:
        return True

    else: # find로 찾은 좌표부터 시작한다.
        row, col = find # 튜플로 들어온 행과 열에 대한 좌표를 받아서,
    for i in range(1, 10): # 1부터 10까지 해당 좌표를 기준으로 가로 세로 3*3을 검사한다.
        if vaild(bo, i, (row, col)): # valid에 변수들이 할당되는데, 보드, 임시로 넣는 번호, 그리고 그 좌표가 들어간다.
            bo[row][col] = i  # 1-1. 만약 valid하다고 판단되었다면, 위와 같이 보드에 추가해준다.
            if solve(bo):
                # 그 상태에서 재귀적으로 solve함수를 호출하는데,
                # 만약 True를 반환한다면,
                # 즉 더이상 0이 없다면 함수는 여기서 끝나고 그렇지 않은 경우 다시 재귀적으로 0이 없어질때까지 호출될 것이다.
                return True


            # 1-2. 그리고, valid하다고 판단되지 않은 경우 False를 반환
            bo[row][col] = 0
    return False

def vaild(bo, num, pos):
    # valid한 num인지 해당 position(pos)에서 확인하는 함수이다.
    # 행, 열, 3*3 으로 검사한다.

    # check row
    for i in range(len(bo[0])): # 0-8을 돌면서,
        if bo[pos[0]][i] == num and pos[1] != i:
            # num과 보드에서 우리가 확인해야할 좌표의 열에 해당하는 행의 0-8까지 있는 곳의 번호가 같고
            # 확인해야할 좌표의 행에 해당하는 것이 i가 아니라면(자기 자신은 확인할 필요가 없음)
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check 3*3 cube
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3+3): # 열
        for j in range(box_x * 3, box_x * 3 + 3): # 행
            if bo[i][j] == num and (i, j) != pos: # 같고, 아니라면,
                return False
    return True # everythings fine

# 시작점을 찾는다.
def find_empty(bo): # 보드가 들어간다.
    for i in range(len(bo)): # 보드의 길이 9만큼,
        for j in range(len(bo[0])): # 보드 행의 길이 9만큼,
            if bo[i][j] == 0: # 0이 있는 곳의 좌표를 전달한다.
                # print(i, j)
                return (i, j) # row, col
    return None

res = solve(board) # solve라는 main 함수에 넣는다.
# print(res)
while res == True:
    board = [i[:] for i in board]
    for line in board:
        print(' '.join(list(map(str, line))))
    break




'''
from sys import stdin
def chk_line(y, x):
    chk = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for r in range(9):
        if sudoku[r][x] in chk:
            chk.remove(sudoku[r][x])
        if not chk:
            return chk
    for c in range(9):
        if sudoku[y][c] in chk:
            chk.remove(sudoku[y][c])
        if not chk:
            return chk 
    row = (y // 3) * 3
    col = (x // 3) * 3
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            if sudoku[r][c] in chk:
                chk.remove(sudoku[r][c])
    return chk
def fill_sudoku(k=0):
    global flag
    if k >= N:
        flag = True
        return True
    y, x = blank[k]   
    chk = chk_line(y, x)
    if not chk:
        return False
    for num in chk:
        sudoku[y][x] = num
        fill_sudoku(k+1)
        if flag:
            return True
        sudoku[y][x] = 0
sudoku = [list(stdin.readline().split()) for _ in range(9)]
blank = []
flag = False
for r in range(9):
    for c in range(9):
        if sudoku[r][c] == '0':
            blank.append((r, c))
N = len(blank)
fill_sudoku()
for i in range(9):
    print(' '.join(sudoku[i]))
'''