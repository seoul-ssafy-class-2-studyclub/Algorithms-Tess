# 은성
## 각각의 노선 저장
## visited
## 어떤 정류장을 갔는지
# 안가면 안가고
# 환승개수, 시간,
# 모든 경우를 다 보면 안된다.
# a를 들르는데 다른 정류장에서 온거 작은거만 간다.
# 백트레킹 힙큐 visited
# 완탐

# 신호..
# visit 2차원 배열? 1차원 배열?
# 코스트가 가장 낮은 애를 빼면서 도착지에 도착하면 멈추도록 한다.
# 그러면 가장 낮은 거부터 할까?
# 저장안하고 쭉 가게?

import sys
sys.stdin = open('17940.txt', 'r')


# 2 18


N, endPoint = map(int, input().split())

names = []
for name in range(N):
    r = input()
    names.append(name)
print(names)

board = [list(map(int, input().split())) for i in range(N)]
print(board)