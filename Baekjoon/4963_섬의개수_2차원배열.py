import sys
sys.stdin = open('4963.txt', 'r')

while True:

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    def check(arr):
        result = 0
        for iy in range(H):
            for ix in range(W):
                if arr[iy][ix] == 1:
                    return 1
        return result

    def colouring(y, x):
        global board
        stack = []
        stack.append((y, x))

        while stack:
            y, x = stack.pop() # pop하면서 해당 좌표를 0으로 처리한다.
            board[y][x] = 0

            for idx in range(8): # 총 8방향에 대한 인덱스를 순회
                tempy = y + dy[idx]
                tempx = x + dx[idx]
                # 범위조절 그리고 해당 좌표를 가진 보드판의 숫자가 1인지 확인
                if 0 <= tempy <= H-1 and 0 <= tempx <= W-1 and board[tempy][tempx] == 1:
                        # 모든게 참이라면 스택에 추가한다.
                        stack.append((tempy, tempx))

        return 1

'''

--------------------위 함수

'''
    W, H = map(int, sys.stdin.readline().split())
    if H == 0 and W == 0: # 바로 예외처리
        break

    board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
    cnt = 0
    res = 1

    for iy in range(H):
        for ix in range(W):
            if H == 1 and W == 1:
                if board[iy][ix] == 1:
                    cnt = 1
                    res = 0
                    break
                elif board[iy][ix] == 0:
                    cnt = 0
                    res = 0
                    break

            else:
                if board[iy][ix] == 1: # 발견하면 해당 좌표 함수에 전달
                    cnt += colouring(iy, ix) # 컬러링 시작, 리턴은 1
                    res = check(board) # 컬러링 후 다른 섬 남아있는지 확인 리턴이 0이 되면, 계속 돈다.

                    if res == 0:
                        break
    print(cnt)
