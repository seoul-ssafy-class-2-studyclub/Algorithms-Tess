'''
12
'''
import sys
# sys.stdin = open('17406.txt', 'r')
import itertools
input = sys.stdin.readline

def rotate(m, d):
    for n in m:
        r,c,s = n
        r, c = r-1, c-1

        for i in range(1, s+1): # 0부터 s까지, 가장 안에서부터 시작한다. 0은 어차피 가만히 있으니까, 1부터 시작하도록 했다.
            temp = d[r-i][c-i]
            for x in range(c-i, c+i): # 오른쪽
                temp, d[r-i][x+1] = d[r-i][x+1], temp
            for y in range(r-i, r+i): # 아래
                temp, d[y + 1][c + i] = d[y + 1][c + i], temp
            for x in range(c+i, c-i, -1): # 왼쪽
                temp, d[r + i][x - 1] = d[r + i][x - 1], temp
            for y in range(r+i, r-i, -1): # 위
                temp, d[y - 1][c - i] = d[y - 1][c - i], temp
    return d

def findsum(rotateb):
    global mymin
    for i in rotateb:
        if sum(i) < mymin:
            mymin = sum(i)

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

data = []
for i in range(K):
    data.append(list(map(int, input().split())))

# 순서있는 조합 == 순열을 구한다.
candidates = list(itertools.permutations(data, K))

# 행의 수만큼 최소값일때 저장한다.
mymin = 99999999

for candidate in candidates:
    # 후보에 들어있는 연산 수 만큼 판을 돌리는 함수
    # 후보들은 q에 넣어져서 하나씩 빼가지면서 돌려진다.
    tempboard = [i[:] for i in board]
    rotatedboard = rotate(candidate, tempboard)

    # 최종적으로 돌려진 판에서 각행이 가진 합을 구하는 함수
    findsum(rotatedboard)

# 각행의 합중에 가장 최소값을 리턴하는 함수 -> 바깥쪽에 딕셔너리를 만들어서 각행에 대한 값들을 저장할까?
print(mymin)