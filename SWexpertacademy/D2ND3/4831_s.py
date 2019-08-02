
import sys
sys.stdin = open('4831.txt', 'r')

for tc in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    C = list(map(int, input().split()))
    Car = K
    moved_distance = 0
    '''
    K 갈 수 있는 거리
    N 종점
    M 정류장 수
    C 배터리가 있는 곳
    '''
    count = 0

    for n in range(N):
        if Car < N: # 종점에 도착하기 전까지 True
            for charger in C: # [1, 3, 5, 7, 9]
                if charger <= Car: # 충전소의 위치를 돌면서 움직인 위치 전까지의 충전소 위치로 값을 바꿔준다.
                    moved_distance = charger
                    #가능한 충전소 위치가 moved_distance가 된다.
            count += 1
            Car = moved_distance + K
        if count == N:
            count = 0

    print('#{} {}'.format(tc, count))



