import sys
sys.stdin = open('5188.txt', 'r')



def dfs_recursion(y, x, chk, temp):
    global my_min

    temp += board[y][x]



    if y == N-1 and x == N-1:
        if temp <= my_min:
            my_min = temp
            return True

    elif temp >= my_min: # 시간초과 해결
        return True

    else:
        for dy, dx in [(1,0), (0,1)]:
            iy = dy + y
            ix = dx + x

            if 0 <= iy < N and 0 <= ix < N and chk[iy][ix] == False:
                chk[iy][ix] = True
                dfs_recursion(iy, ix, chk, temp)
                chk[iy][ix] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    check = [[False]*N for _ in range(N)]
    my_min = 99999
    #check[0][0] = True

    dfs_recursion(0, 0, check, 0)
    print(f'#{tc}', my_min)
