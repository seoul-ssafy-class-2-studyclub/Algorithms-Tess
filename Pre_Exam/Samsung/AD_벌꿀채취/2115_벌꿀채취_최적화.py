import sys
sys.stdin = open('2115.txt', 'r')


def value(M, C, jud):
    global bee

    maxV = 0
    # M = 3이라 생각하면
    for x in range(1 << M):  # 1<<M을 2**M-1 로 줄 수 있다.
        s = 0  # 부분 집합의 합
        ss = 0
        for y in range(M):  # 0,1,2번 비트
            if x & (1 << y) != 0 and s + jud[y] <= C:  # i의 j번 비트가 1이고, 합계가 제한량 이하면
                s += jud[y]
                ss += jud[y] * jud[y]  # 채취한 벌꿀의 가치
        if maxV < ss:
            maxV = ss

    return maxV


for t in range(int(input())):
    N, M, C = map(int, input().split())  # NxN행렬, 한 일꾼의 벌통의 수 M(연속)가로, 한 일꾼의 최대양 C

    bee = [list(map(int, input().split())) for i in range(N)]
    # M개의 원소에서 1개 이상, 최대 M개를 고르는 방법

    m = []
    for i in range(N):
        mm = 0
        for j in range(N - M + 1):
            jud1 = bee[i][j:j + M]
            a = value(M, C, jud1)
            if mm < a:
                mm = a
        m.append(mm)
    m1 = m.pop(m.index(max(m)))
    m2 = m.pop(m.index(max(m)))
    print('#{} {}'.format(t + 1, m1 + m2))

#
# # import heapq
# # input = sys.stdin.readline
# import itertools
#
# '''
# 우선순위 큐(priority queue)를 위한 heapq 모듈 사용법
# h = []
# heapq.heappush(h, (3, "Go to home"))
# first = heapq.heappop(h)
#
# 최대 힙 (max-heap)
#
# sorted reversed
# '''
#
# '''
# #1 174
# #2 131
# #3 145
# #4 155
# #5 166
# #6 239
# #7 166
# #8 172
# #9 291
# #10 464
# '''
#
# # 모든 부분 집합을 구해서
# # 수익을 구함
# # 부분 집합들 중에서 C를 넘지 않고 첫번째 일꾼의 최대수익인것
# # 배열을 만들어서 넣고
# # M을 제외한 이후의 값들 중에 가장 최대값이 두번째 일꾼의 최대이익이 될 것
# # dp = [[0] * N for i in range(N)]
# '''
# 2
# 9
# [5, 6, 5]
# 5
# 6
# 5 6
# 5 5
# 5 6 5
#
# 1, 2, 3
# M만큼의 조합
# 그것들중 C 가 넘지 않고 가장 최대 수익인 경우
# '''
#
# def find_profit(temp):
#     global M, C
#     max_profit = -1
#     honeys = temp[0]
#     for i in range(0, M):
#         myhoneys = list(itertools.combinations(honeys, i+1))
#
#         for myhoney in myhoneys:
#             if sum(myhoney) <= C:
#                 mysum = 0
#                 for ix in myhoney:
#                     mysum += ix * ix
#                 if max_profit <= mysum:
#                     max_profit = mysum
#     return max_profit
#
# for tc in range(1, int(input())+1):
#     #  벌통들의 크기 N, 선택할 수 있는 벌통의 개수 M, 꿀을 채취할 수 있는 최대 양 C
#     N, M, C = map(int, input().split())
#     hives = [ list(map(int, input().split())) for _ in range(N) ]
#     dp = [[0]*N for _ in range(N)]
#     first_heap = []
#     for y in range(N):
#         for x in range(N-M+1):
#             yxtemp = []
#             numstemp = []
#             for ix in range(x, x+M):
#                 yxtemp += [(y, ix)]
#                 numstemp += [(hives[y][ix])]
#             first_heap += [[numstemp, yxtemp]]
#
#     for first in first_heap:
#         profit = find_profit(first)
#         dp[first[1][0][0]][first[1][0][1]] = profit
#     # dp
#     temp_result = []
#     for y in range(N):
#         for x in range(N):
#             result = -1
#             for iy in range(y, N):
#
#                 if y == iy: # 같은 경우
#                     for ix in range(x+M, N):
#                         comp = dp[iy][ix] + dp[y][x]
#                         if comp > result:
#                             result = comp
#                 else:
#                     for ix in range(N): # 같은 줄이 아닌 경우
#                         comp = dp[iy][ix] + dp[y][x]
#                         if comp > result:
#                             result = comp
#             temp_result += [(result)]
#     print(f'#{tc}', max(temp_result))
#
#     '''
# [[[6, 1], [(0, 0), (0, 1)]], [[6, 1], [(0, 0), (0, 1)]], [[1, 9], [(0, 1), (0, 2)]], [[1, 9], [(0, 1), (0, 2)]], [[9], [(0, 3)]], [[9], [(1, 1)]], [[8, 5], [(1, 1), (1, 2)]], [[8, 5], [(1, 1), (1, 2)]], [[5, 8], [(1, 2), (1, 3)]], [[5, 8], [(1, 2), (1, 3)]], [[3, 4], [(2, 0), (2, 1)]], [[3, 4], [(2, 0), (2, 1)]], [[4, 5], [(2, 1), (2, 2)]], [[4, 5], [(2, 1), (2, 2)]], [[5, 3], [(2, 2), (2, 3)]], [[5, 3], [(2, 2), (2, 3)]], [[8, 2], [(3, 0), (3, 1)]], [[8, 2], [(3, 0), (3, 1)]], [[2, 6], [(3, 1), (3, 2)]], [[2, 6], [(3, 1), (3, 2)]], [[6, 7], [(3, 2), (3, 3)]], [[6, 7], [(3, 2), (3, 3)]]]
#     '''