import sys
sys.stdin = open('14890.txt', 'r')

def solve(i, j, dir):
    global answer, L
    step = 0
    # 세로
    if dir == 0:

        while True:
            # print(i, j)
            # step이 크거나 같은 경우, 그리고, 다음 것의 차이가 1인 경우,
            if step >= L and 1 == abs(board[i][j] - board[i+1][j]):
                # 새로운 step이 된다.
                step = 0
                if i+1 < N:
                    i += 1
                else:
                    answer += 1
                    break

            # 같다면 step을 계속 늘려준다.
            if board[i][j] == board[i+1][j]:
                # print('--')
                step += 1
                i += 1

            if board[i][j] != board[i+1][j] and 1 == abs(board[i][j] - board[i+1][j]):
                temp = board[i + 1][j]
                # print(temp, board[i][j])
                while board[i][j] == temp and step != L:
                    i = i + 1
                    print(i)
                    step += 1
                # print(i)


            # 차이가 2 이상이라면 break
            if 2 <= abs(board[i][j] - board[i+1][j]):
                break

    elif dir == 1:
        pass







N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for i in range(N):
    print(0+i)
    solve(0, 0+i, 0) # 세로
    solve(0+i, 0, 1) # 가로
print(answer)