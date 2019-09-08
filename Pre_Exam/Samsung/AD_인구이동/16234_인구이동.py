import sys
sys.stdin = open('16234.txt', 'r')
from collections import deque

def search_companions(y, x):
    global fin
    q = deque()
    q.append((y, x))
    my_friends = deque()
    # 1. 스타트 포인트에서 상하좌우확인 후
    # 2. 내 옆과 차이가 L과 R안에 있다면, 연합이 가능한 애이다.
    # 3. 그렇지 않다면 연합 불가능한 애
    # 5. 해당 좌표에 나눈 값을 다시 재분배 한다.
    # 2. 연합이 가능한 애들의 좌표를 넣어서 리스트를 만든다. 삭제) 남아있는 애들로 스타트 포인트를 잡고 좌표를 찾아 저장한다.
    # 3. 중복되는 좌표가 발생할 수 있기때문에, 없는 경우만 정제한다.
    # 6. 해당 카운트는 바깥쪽에서 global선언하여 갱신한다.
    while q:
        y, x = q.popleft()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < N and visited[iy][ix] == False:
                if L <= abs(earth[y][x] - earth[iy][ix]) <= R:
                    visited[iy][ix] = True
                    q.append((iy, ix))
                    my_friends.append((iy, ix))

    my_temp_sum = 0
    ML = len(my_friends)
    if ML > 1:
        fin += 1 # 있을때만 카운트
        for y, x in my_friends: # 3. 저장한 좌표에 해당하는 애들을 특정 토탈에 더하고, # 튜플이 여러개 리스트안에 있는 경우 for 00 in 00이 가능하다.
                                # 튜플이 하나인 경우는 변수처리해야한다. y, x = my_friend 이것처럼.
            my_temp_sum += earth[y][x] # 4. 저장한 좌표의 길이만큼 나눈후,
        my_temp_res = my_temp_sum // ML
        for y, x in my_friends:
            earth[y][x] = my_temp_res # 5. 추가

N, L, R = map(int, sys.stdin.readline().split())
earth = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = -1
Com = N*N
while 1:
    res += 1
    visited = [[0] * N for _ in range(N)] # 이 부분이 핵심, 다시 비지티드를 생성해주어야한다. 방문+변화시킨 애들은 다시 가지않기위해서
    fin = 0
    for Y in range(N):
        for X in range(N):
            if earth[Y][X] != 0 and visited[Y][X] == 0:
                # 1. 전체에서 스타트 포인트를 잡고, 0이 아닌수를 스타트 포인트로 잡는다.
                search_companions(Y, X)

                # 6. visited가 모두 다 돌면,
                # 7. 인구이동을 한 번 한것이므로
                # 6. 또 인구이동이 이뤄지는 곳을 확인한다.
    # 7. 이번에는 visited가 다시 새롭게 만들어져야 한다.
    # 8. 조건에 만족하는 국가들이 없으면 좌표가 없는 리스트를 반환할 것이므로 이를 breakpoint로 쓴다.
    if fin == 0: # 전체를 다 돌아도 있는 경우가 없으면 breakpoint 성립
        break
print(res)


import time
st = time.time()
print(time.time() - st)
