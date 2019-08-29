'''

#1 3
#2 0
#3 4

'''

import sys
sys.stdin = open('4831.txt', 'r')

for tc in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    C = list(map(int, input().split()))
    KC = K

    # board 생성
    board = [0]*(N+1-M) # 인덱스는 -1이기때문에 종점때문에 +1을 해준다.
    for i in C:
        board.insert(i, 1) # 1이 있는 곳이 정류장 충전소가 있는 곳이다.

    count = 0
    for n in range(N): # 총 10까지의 길이라면, 10까지 돈다.
        # print('현재위치', n)
        K = K - 1 # 갈때마다 K는 1씩 줄어든다.

        if board[n] == 1:# 만약 해당 인덱스가 1일때, 자동차 충전소라는 이야기이며,
            if K < 0:  # 이때에 K가 만약 -1 이면 충전을 할 수 없으므로
                count = 0 # count에 0을 준다.

            elif K >= 0:
                stop = 0
                for c in range(len(C)-1):
                    print(c)
                    if n+C[stop+1] - n < K:
                        stop += 1
                        # 0보다 크거나 같으면, 충전할 수 있는 충전소이므로
                    else:
                        K = KC # K에 충전을 해주고
                        count += 1 #충전 횟수를 저장해준다.
                        # print('충전', count)

    print('충전횟수', count)