import sys
sys.stdin = open('17780.txt', 'r')

N, K = map(int, input().split())
staticBoard = [list(map(int, input().split())) for _ in range(N)]
# 그냥 만들면 얕은 복사가 되어서 참조형식의 행렬이 만들어 진다.
# 때문에 이중 for문으로 해야한다.
movingBoard = [[[] for _ in range(N)] for _ in range(N)]
print(movingBoard)

dir = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}

for horsename in range(1, K+1):
    y, x, d = map(int, input().split())
    y, x = y-1, x-1

    movingBoard[y][x].append((horsename, y, x, d))
print(movingBoard)
