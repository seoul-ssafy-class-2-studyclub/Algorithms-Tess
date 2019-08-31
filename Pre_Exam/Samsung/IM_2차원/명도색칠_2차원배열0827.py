import sys
sys.stdin = open('input.txt', 'r')

from pprint import pprint

# 0(흰색)번부터 10번(검은색)까지 총 11가지가 존재
# 인풋
# 사각형 위치 크기  페인트의 명도 번호
# 칠할 명도보다 더 높은 명도 번호를 가지면 색을 칠하지 않는다.
# 전체벽에서 가장 넓은 영역을 차지한 명도 번호를 찾는다.
# 크기를 구한다.

# 행은 0, N-1
# 열은 0, M-1

# 명도번호는 0, 10이하의 정수
# -1로 채우자

# K는 1, 20 페인트 칠하는 횟수
# 칠하다가 더 높은 부분이 존재하면 그 사각형 자체를 칠하지 않는다.

# 1 1 1 10 1
# 높이1 너비10 명도번호1
# 1 1 10 1 1
# 높이10 너비1 명도 1


#1 1 4 7 2
# y1, x1, (y1, y2), (x1, x2)

def check(arr):
    check_board = []

    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            # 색칠할 부분의 공간의 명도가 더 작은가?
            if arr[y][x] < color:
                check_board.append('Y')

            # 더큰가? 크면 'N'을 추가한다.
            elif arr[y][x] > color:
                check_board.append('N')

    # N 만 있는 걸 다시 뽑아내기 위해서 아래와 같이 선언했었다.
    new = check_board
    new_for = []
    for i in new:
        if i == 'N':
            new_for.append(i)

    # 해당 리스트가 0 이라면 'N'이 없다는 뜻이므로, 색칠해도 되지만,
    if len(new_for) == 0:
        return 1

    # 그렇지 않은 경우 색칠하면 안된다.
    else:
        return 0

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    gradient = [_ for _ in range(11)]
    cnt_list = []

    for k in range(K):
        y1, x1, y2, x2, color = map(int, input().split())
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if k == 0:
                    board[y][x] = color

                elif k > 0:
                    # 색칠하기전에 색칠이 가능한 명도인지 확인을 먼저한다.
                    res = check(board)
                    # res를 1 반환하는 경우 색칠 가능이므로 색칠 시작
                    if res == 1:
                        board[y][x] = color
                    # 그렇지 않은경우 색칠이 불가능하므로 색칠하지 않고 다음으로 넘어간다.
                    elif res == 0:
                        break

    cnt2_list = [0]*15
    for item in gradient:
        cnt2 = 0
        for y in range(N):
            for x in range(M):
                if item == board[y][x]: # runtime error #  행 열 제대로 확인!
                    cnt2 += 1

        # 인덱스를 명도 이름으로 하여 해당 명도==인덱스에 cnt2값을 추가한다.
        cnt2_list[item] = cnt2
    print('#{} {}'.format(tc, max(cnt2_list)))




