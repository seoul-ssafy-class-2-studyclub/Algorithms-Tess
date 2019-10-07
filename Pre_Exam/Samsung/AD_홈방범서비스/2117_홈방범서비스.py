import sys
sys.stdin = open('2117.txt', 'r')


'''
#1 5
#2 4
#3 24
#4 48
#5 3
#6 65
#7 22
#8 22
#9 78
#10 400
'''




# 도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M이 주어진다.
# 그 다음 줄부터 N*N 크기의 도시정보가 주어진다. 지도에서 1은 집이 위치한 곳이고, 나머지는 0

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    land = [ list(map(int, input().split())) for _ in range(N) ]

    # 마름모로 커버 가능한 테두리 범위
    # abs(a-x)+abs(b-y) <= K

    # 운영비용 = cost
    # cost = (K*K) + (K-1)*(K-1)
    # mymax = -1
    # maxprofit = (M * numofhouses) - cost
    # if maxprofit >= 0 and maxprofit >= mymax:
    # mymax = maxprofit

    # print(land, N, M)
    # 0,0 부터 끝까지 돌면서,

    for y in range(N):
        for x in range(N):
            # k를 +1로 늘려 나가면서, 늘어난 k마다 정해진 운영비용과,
            # 모든 시작점에서 1부터 N+1만큼 K를 늘려갈것,
            # N = 8 이면 K가 0.0에서 전부를 커버가능한건 8+1이다.
            # 손해만 보지 않으면 되고, 최대한 많은 집에게 공급하면되기때문,
            for k in range(1, N+1):
                print(k)
                # 몇개 집이 범위에 있는지 봄
                # 집이 있는 좌표 구한 것의 개수와,
                # 계산한다.
                # 개수가 가장 큰것을 mymax 저장하고,
                # 하다가 끝나면 그 다음 옆 자리로 넘어감 반복
                # 계속 0.0부터 끝까지 반복하면됨

'''
def calc_benefit():
    # 2. K == 1부터 K를 1씩 증가.
    # 설치 위치를 (ym, xm)이라고 했을 때, |ym - yn| + |xm - xn| < K이면 서비스가 제공 가능하다.
    # 반복문을 돌리며 완전탐색.
    global max_cnt
    K = 1
    while True:
        cost = K ** 2 + (K - 1) ** 2
        for r in range(N):
            for c in range(N):
                cnt = 0
                for y, x in houses:
                    dis = abs(y - r) + abs(x - c)
                    if dis < K:
                        cnt += 1
                # 3. 집의 수를 세어 주고 이익 계산
                # 만약 모든 집이 거리 안에 들어와 있으면서 이익이 0보다 작다면, 더 이상 진행할 필요가 없으므로 반복문을 끝낸다. 
                benefit = M * cnt - cost
                if cnt == H and benefit < 0:
                    return False
                if cnt > max_cnt and benefit >= 0:
                    max_cnt = cnt
        K += 1
 
for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    # 1. 집들의 좌표를 모두 저장함
    houses = []
    H = 0
    for r in range(N):
        for c in range(N):
            if city[r][c]:
                houses.append((r, c))
                H += 1
 
    max_cnt = 0
    calc_benefit()
 
    print(f'#{case} {max_cnt}')
'''
