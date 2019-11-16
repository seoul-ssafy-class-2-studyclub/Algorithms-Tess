import sys
sys.stdin = open('5654.txt', 'r')
from pprint import pprint

### 줄기세포(cell)를 배양용기(board)에 도포후
# 일정시간(K)동안 배양시킨후
# 죽지않은 세포인 비활성+활성상태 줄기 세포의 개수를 출력

# 하나의 줄기세포는 가로, 세로 크기가 1인 정사각형 형태
# 용기는 격자 그리드로 구성되어있고, 하나의 그리드 셀은 줄기세포 크기와 동일


# 초기상태에서 줄기세포는 비활성 상태, x시간 동안 비활성상태이고, x시간이 지나면 활성상태가 된다.
# 활성상태에서 x시간동안 살아있을 수 있고, x시간이 지나면 죽는다.
# 죽어도 소멸되는 것은 아니고 죽은 상태로 해당 그리드 셀을 차지
# 활성화된 줄기세ㅐ포는 첫 1시간동안은 상하좌우 네방향 동시번식
# 번식이 끝나면 비활성
# 가려는 방향에 다른 줄기세포가 존재하면 추가적으로 번식하지 않는다.
# 두개 이상의 줄기세포가 하나의 그리드셀에 동시 번식하고자 하면,
# 생명력 수치가 높은 줄기세포가 혼자 셀을 차지 (셀끼리는 병합되지 않는다)


# 초기상태의 보드에서 줄기세포가 퍼지는 만큼 보드가 커져야하는데
# 이걸 어떻게 처리할지?
# 보드를 그리는게 맞는걸까?
# *2차원 배열 내에 있는 중기세포의 상태를 확인하고 상태 조건에 맞게 2차원 배열 업데이트


# K는 1<=K<=300이기때문에 리스트를 사용해도 될것같다.
# 생명력 X는 1<=X<=10이다.
# 0인경우 줄기세포가 존재하지 않는 그리드 이다.

# 그리드 자체가 내가 갖고올 수 있는 정보다.
# 보드에서 0이아닌 곳의 정보는 생명력, x좌표 y좌표


d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for tc in range(1): # 테케1만
    N, M, K = map(int, input().split())
    XM = 600
    XN = 600
    #보드 진행할때 사용

    board = [ list(map(int, input().split())) for _ in range(N)]
    # chk에 board를 껴넣어주자
    # print(board)
    chk = [[0]*XN for _ in range(XM)]
    # pprint(chk)

    cells_info = []
    for y in range(N):
        for x in range(M):
            if board[y][x] != 0: # 0이 아니라면 cell이 존재하므로
                chk[y+300][x+300] = board[y][x]
                cells_info.append([board[y][x], 1, y+300, x+300, 0])
    cells_info = list(reversed(list(sorted(cells_info))))
    # [(y, x)좌표, 생명력, status(0 죽음, 1 비활성, 2 활성), 생명력과 비례한 나이]를 2차원 배열에 추가
    # cell : 생명력, 죽은상태, 비활성상태, 활성상태, 태어나서 시간이 얼마나 지났는지 카운트될곳
    # 비활성 상태인 셀만 상태가 바뀐다.

    # 비활성 시간이 지났을 경우 활성상태로 바꿔준다
    # 활성상태에서 번식 시작하고 번식이 끝난 셀은 죽은 상태로 바꾼다.


    for k in range(K):
        fin = len(cells_info)
        cells_info = list(reversed(list(sorted(cells_info))))

        count = 0
        while fin:
            lifes, status, y, x, cnt = cells_info.pop(0)
            if cnt == lifes and status == 1:
                # life가 같고, 비활성화 상태라면,
                # 활성화상태로 바꾸고,
                cells_info.append((lifes, status+1, y, x, cnt))
            if (cnt < lifes and status == 1) or (lifes*2 > cnt > lifes and status == 2):
                # life보다 작은 상태면,
                # 아직 작으면 더 시간이 지나야 한다.
                # 그래서 비활성화 상태를 유지하면서 cnt를 늘려준다.
                cells_info.append((lifes, status, y, x, cnt+1))
            if cnt == lifes and status == 2:
                # life가 cnt와 같고 활성상태라면, lifes만큼 이제 퍼트리고 죽게된다.
                for iy, ix in [(0,1), (1, 0), (0,-1), (-1,0)]:
                    dy = iy + y
                    dx = ix + x
                    if 0 <= dy < XM and 0 <= dx < XN: # and lifes > chk[dy][dx]
                        if chk[dy][dx] == 0:
                            chk[dy][dx] = lifes
                            # 새롭게 생긴 애들은 비활성화 상태로 시작한다.
                            cells_info.append((lifes, 1, dy, dx, 0))
                            # life 보다 보드에 적힌게 더 큰 경우 버린다.
                        else:
                            continue
                cells_info.append((lifes, status, y, x, cnt+1))
            if lifes*2 == cnt and status == 2:
                # life*2 한만큼 시간이 지났다면, 활성화 된 후 지난 것이므로 없애준다.

                continue # 이 continue때문에 fin이 되지않았음

            fin -= 1
            # print(fin, count)
        print(cells_info)
        print(len(cells_info))
    print(len(cells_info))
    # print(chk)

#
# for i in range(10):
#     if i == 30:
#         print(i)
#         # break를 만나지 않아서 -1을 출력
#         break
#
# else:
#     print(-1)
#
# a = [[1,2], [2,3]]
# b = sum(sum(a, []))
# print(b)