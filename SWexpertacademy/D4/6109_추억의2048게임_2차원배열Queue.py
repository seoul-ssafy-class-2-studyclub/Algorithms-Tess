# import sys
# sys.stdin = open('6109.txt', 'r')

def Vertical(d):
    for i in range(N):
        queue = []
        for j in range(N):
            if game[j][i]:
                queue.append(game[j][i])
                game[j][i] = 0

        # 열을 하나 0으로 만들고 시작
        if d == 'up':
            idx = 0
            while queue:
                # 제일 처음 들어오는 애는 빈 열에 추가 된다.
                temp = queue.pop(0)
                if game[idx][i] == 0:
                    game[idx][i] = temp
                elif game[idx][i] == temp:
                    game[idx][i] += temp
                    idx += 1
                else:
                    idx += 1
                    game[idx][i] = temp


        elif d == 'down':
            idx = N-1
            while queue:
                temp = queue.pop()
                if game[idx][i] == 0:
                    game[idx][i] = temp
                elif game[idx][i] == temp:
                    game[idx][i] += temp
                    idx -= 1
                else:
                    idx -= 1
                    game[idx][i] = temp


def Horizontal(d):
    for i in range(N):
        queue = []
        for j in range(N):
            if game[i][j]:
                queue.append(game[i][j])
                game[i][j] = 0

        # 열을 하나 0으로 만들고 시작
        if d == 'left':
            idx = 0
            while queue:
                # 제일 처음 들어오는 애는 빈 열에 추가 된다.
                temp = queue.pop(0)
                if game[i][idx] == 0:
                    game[i][idx] = temp
                elif game[i][idx] == temp:
                    game[i][idx] += temp
                    idx += 1
                else:
                    idx += 1
                    game[i][idx] = temp

        elif d == 'right':
            idx = N - 1
            while queue:
                temp = queue.pop()
                if game[i][idx] == 0:
                    game[i][idx] = temp
                elif game[i][idx] == temp:
                    game[i][idx] += temp
                    idx -= 1
                else:
                    idx -= 1
                    game[i][idx] = temp

T = int(input())
for tc in range(1, T+1):
    N, D = input().split()
    N = int(N)
    game = [list(map(int, input().split())) for _ in range(N) ]
    if D == 'up' or D == 'down':
        Vertical(D)
    elif D == 'left' or D == 'right':
        Horizontal(D)
    print(f'#{tc}')
    for i in range(N):
        print(' '.join(map(str, game[i])))