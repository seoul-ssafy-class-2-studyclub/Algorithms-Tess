import sys
sys.stdin = open('1979.txt', 'r')

for tc in range(int(input())):

    # 보드
    N, k = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]


    # 가로
    row_result = 0
    for y in range(N):
        rowcnt = 0  # 가로줄에서 1을 셀 카운트
        for x in range(N):
            if board[y][x] == 1:  # 1이라면
                rowcnt += 1  # 카운트 추가

            if x == N - 1 or board[y][x] == 0:  # 벽 혹은 0을 만나면,
                if rowcnt == k:  # 이 글자수와 동일하면,
                    row_result += 1  # 결과값에 1 추가
                rowcnt = 0
                '''
                카운트 초기화!!!! 중요 
                다음 가로줄, 혹은 다음 0이후의 1로 넘어가서 다시 카운트
                '''

    # 세로
    col_result = 0
    for m in range(N):
        colcnt = 0
        for l in range(N):
            if board[l][m] == 1:
                colcnt += 1
            if l == N - 1 or board[l][m] == 0:
                if colcnt == k:
                    col_result += 1
                colcnt = 0

    res = row_result + col_result
    print(f'#{tc + 1} {res}')




