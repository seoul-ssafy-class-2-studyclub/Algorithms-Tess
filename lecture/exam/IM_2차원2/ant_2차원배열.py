import sys
sys.stdin = open('ant.txt', 'r')

'''
#1 34 #2 23 #3 16
'''

from pprint import pprint

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
mirror_one = 1
mirror_two = 2

# 0 위로
# 1 왼쪽으로
# 2 아래로
# 3 오른쪽으로
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N = N + 6
    # 기본 시작
    ant_starty, ant_startx = 3, 3
    # 기본 방향 상태
    status = 3

    # 벽을 만나면 상태를 바꿔간다. == 상태는 델타인덱스

    # 나중에 영역 밖에 나갈때 break하기 위해서 패딩을 씌웠다.
    padding = [[-1]*N for _ in range(N)]
    for i in range(3, N-3):
        s = list(map(int, input()))
        padding[i][3:N-3] = s[:]

    stack = []
    stack.append((ant_starty, ant_startx, status))
    cnt = 0

    while stack:
        my, mx, status = stack.pop()
        cnt += 1

        if padding[my][mx] != -1:

            if status == 3:
                tempy = my + dy[status]
                tempx = mx + dx[status]
                if padding[tempy][tempx] == 0:
                    status = 3
                    stack.append((tempy, tempx, status))
                elif padding[tempy][tempx] == 1:
                    status = 0
                    stack.append((tempy, tempx, status))
                elif padding[tempy][tempx] == 2:
                    status = 2
                    stack.append((tempy, tempx, status))


            elif status == 0:
                tempy = my + dy[status]
                tempx = mx + dx[status]
                if padding[tempy][tempx] == 0:
                    status = 0
                    stack.append((tempy, tempx, status))
                elif padding[tempy][tempx] == 1:
                    status = 3
                    stack.append((tempy, tempx, status))
                elif padding[tempy][tempx] == 2:
                    status = 1
                    stack.append((tempy, tempx, status))


            elif status == 1:
                tempy = my + dy[status]
                tempx = mx + dx[status]
                if padding[tempy][tempx] == 0:
                    status = 1
                    stack.append((tempy, tempx, status))
                elif padding[tempy][tempx] == 1:
                    status = 2
                    stack.append((tempy, tempx, status))
                elif padding[tempy][tempx] == 2:
                    status = 0
                    stack.append((tempy, tempx, status))


            elif status == 2:
                tempy = my + dy[status]
                tempx = mx + dx[status]
                if padding[tempy][tempx] == 0:
                    status = 2
                    stack.append((tempy, tempx, status))
                elif padding[tempy][tempx] == 1:
                    status = 1
                    stack.append((tempy, tempx, status))
                elif padding[tempy][tempx] == 2:
                    status = 3
                    stack.append((tempy, tempx, status))

    print(f'#{tc}', cnt-1)









