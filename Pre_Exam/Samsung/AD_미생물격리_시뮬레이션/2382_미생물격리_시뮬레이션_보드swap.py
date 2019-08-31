import sys
sys.stdin = open('2382.txt', 'r')


# 미생물을 움직이는 함수 (현재 위치, 미생물의 크기, 끝 인덱스, 방향)
def move(idx, size, p, di):
    # 만약 방향이 위(1)거나 왼쪽(3)이면 위치를 -1, 아래(2)거나 오른쪽(4)이면 위치를 +1
    if di == 1 or di == 3:
        nxt = idx - 1
    elif di == 2 or di == 4:
        nxt = idx + 1
    # 만약 다음 위치의 인덱스가 0이거나 끝이면 사이즈를 줄이고 방향을 바꾼다.
    if nxt == 0:
        size //= 2
        if di == 1:
            di = 2
        elif di == 3:
            di = 4
    elif nxt == p:
        size //= 2
        if di == 2:
            di = 1
        elif di == 4:
            di = 3
    return nxt, size, di


result_list = []
T = int(input())
for case in range(T):
    N, M, K = map(int, input().split())
    # 현재 미생물의 위치를 표시할 보드
    board = [[0] * N for _ in range(N)]
    # 미생물이 이동하게 될 보드
    chk = [[0] * N for _ in range(N)]
    # 미생물들의 정보를 담을 리스트
    micro = []
    for i in range(K):
        r, c, m, d = map(int, input().split())
        # micro에 미생물의 정보를 담고 board[r][c]에 담은 정보를 복사한다.
        # 둘이 연결되게 할 것이기 떄문에 deepcopy를 사용하지 않는다.
        # 마지막 m은 미생물 충돌 시 병합 전 원래 크기를 비교하기 위한 변수.
        micro.append([r, c, m, d, m])
        board[r][c] = micro[-1]

    for _ in range(M):
        for i in range(len(micro)):
            r, c, m, d, o = micro[i]

            # 크기가 0이면 소멸된 미생물이므로 무시. 정보를 빼낸 뒤 board[r][c]를 0으로 초기화 해 준다.
            if m == 0:
                continue
            board[r][c] = 0

            # 방향이 위(1)이나 아래(2)면 r값을, 왼쪽(3)이나 오른쪽(4)이면 c값을 바꾸어준다.
            if d == 1 or d == 2:
                r, m, d = move(r, m, N - 1, d)
            else:
                c, m, d = move(c, m, N - 1, d)

            # micro[i]의 값들을 갱신해 준다.
            micro[i][0] = r
            micro[i][1] = c
            micro[i][2] = m
            micro[i][3] = d
            micro[i][4] = m

            # 만약 chk[r][c]가 비어 있다면 아직 아무 미생물도 없는 것이므로 mirco[i]를 복사해 준다.
            if not chk[r][c]:
                chk[r][c] = micro[i]
            else:
                # 만약 chk[r][c]에 있는 미생물의 원래 크기(chk[r][c][4])가 새로 도착한 미생물의 크기(micro[i][4])보다 크다면
                # 누적합 크기(chk[r][c][2])에 흡수될 미생물의 크기(micro[i][2])를 더해주고,
                # micro[i][2]를 0으로 바꿔준다.
                if chk[r][c][4] > micro[i][4]:
                    chk[r][c][2] += micro[i][2]
                    micro[i][2] = 0
                else:
                    # 반대의 경우라면  새로 온 미생물의 크게(micro[i][2])에 기존의 것(chk[r][c][2])을 더해주고,
                    # 원래 미생물의 크기(chk[r][c][2])를 0으로 바꾸어 준다.
                    # deepcopy를 안 했기 때문에 이 과정에서 micro에 저장되어 있는 값도 동시에 0으로 바뀌게 된다.
                    # chk[r][c]에 새로운 값(micro[i])를 복사해 놓는다.
                    micro[i][2] += chk[r][c][2]
                    chk[r][c][2] = 0
                    chk[r][c] = micro[i]

        # 기존의 board는 텅 비게 되었으므로 미생물들이 모두 이동한 chk와 바꾸어 준다.
        board, chk = chk, board

    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                result += board[i][j][2]
    result_list.append(result)

for i in range(T):
    print(f'#{i + 1} {result_list[i]}')
