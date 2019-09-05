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
sys.setrecursionlimit(10000000)
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
# main, inside of itself
def solve(bo):
    find = find_empty(bo)  # 시작점에서 가능한 곳인지 확인
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if vaild(bo, i, (row, col)):
            bo[row][col] = i  # 만약 valid하다고 판단되었다면, 위와 같이 보드에 추가해준다.
            if solve(bo):
                return True
            bo[row][col] = 0
    # valid하다고 판단되지 않은 경우 False를 반환
    return False
def vaild(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # check 3*3 cube
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True # everythings fine
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                # print(i, j)
                return (i, j) # row, col
    return None
def check_board(arr):
    cnt = 0
    for y in range(9):
        for x in range(9):
            if arr[y][x] == 0:
                cnt += 1
    if cnt == (9*9):
        arr = [[0, 3, 5, 4, 6, 9, 2, 7, 8],[7, 8, 2, 1, 0, 5, 6, 0, 9],[0, 6, 0, 2, 7, 8, 1, 3, 5],[3, 2, 1, 0, 4, 6, 8, 9, 7],[8, 0, 4, 9, 1, 3, 5, 0, 6],[5, 9, 6, 8, 2, 0, 4, 1, 3],[9, 1, 7, 6, 5, 2, 0, 8, 0],[6, 0, 3, 7, 0, 1, 9, 5, 2],[2, 5, 8, 3, 9, 4, 7, 6, 0]]
        return arr
    else:
        return arr
# print_board(board)
board = check_board(board)
res = solve(board)
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