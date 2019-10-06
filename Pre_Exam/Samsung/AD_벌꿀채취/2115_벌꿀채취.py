import sys
sys.stdin = open('2115.txt', 'r')
# import heapq
# input = sys.stdin.readline
import itertools

'''
우선순위 큐(priority queue)를 위한 heapq 모듈 사용법
h = []
heapq.heappush(h, (3, "Go to home"))
first = heapq.heappop(h)

최대 힙 (max-heap)

sorted reversed
'''

'''
#1 174
#2 131
#3 145
#4 155
#5 166
#6 239
#7 166
#8 172
#9 291
#10 464
'''



# 모든 부분 집합을 구해서
# 수익을 구함
# 부분 집합들 중에서 C를 넘지 않고 첫번째 일꾼의 최대수익인것
# 배열을 만들어서 넣고
# M을 제외한 이후의 값들 중에 가장 최대값이 두번째 일꾼의 최대이익이 될 것
# dp = [[0] * N for i in range(N)]
'''
2
9
[5, 6, 5]
5
6
5 6
5 5
5 6 5

1, 2, 3
M만큼의 조합
그것들중 C 가 넘지 않고 가장 최대 수익인 경우
'''

def find_profit(temp):
    global M, C
    max_profit = -1
    honeys = temp[0]
    for i in range(0, M):
        myhoneys = list(itertools.combinations(honeys, i+1))

        for myhoney in myhoneys:
            if sum(myhoney) <= C:
                mysum = 0
                for ix in myhoney:
                    mysum += ix * ix
                if max_profit <= mysum:
                    max_profit = mysum
    return max_profit



for tc in range(int(input())):
    #  벌통들의 크기 N, 선택할 수 있는 벌통의 개수 M, 꿀을 채취할 수 있는 최대 양 C
    N, M, C = map(int, input().split())
    hives = [ list(map(int, input().split())) for _ in range(N) ]


    dp = [[0]*N for _ in range(N)]


    first_heap = []
    for y in range(N):
        for x in range(N-M+1):
            yxtemp = []
            numstemp = []
            for ix in range(x, x+M):
                yxtemp.append((y, ix))
                numstemp.append(hives[y][ix])
            first_heap.append([numstemp, yxtemp])


    for first in first_heap:
        profit = find_profit(first)
        dp[first[1][0][0]][first[1][0][1]] = profit

    # dp

    temp_result = []
    for y in range(N):
        for x in range(N):
            result = -1
            for iy in range(y, N):

                if y == iy: # 같은 경우
                    for ix in range(x+M, N):
                        comp = dp[iy][ix] + dp[y][x]
                        if comp > result:
                            result = comp
                else:
                    for ix in range(N): # 같은 줄이 아닌 경우
                        comp = dp[iy][ix] + dp[y][x]
                        if comp > result:
                            result = comp
            temp_result.append(result)

    print(f'#{tc+1}', max(temp_result))

    '''
[[[6, 1], [(0, 0), (0, 1)]], [[6, 1], [(0, 0), (0, 1)]], [[1, 9], [(0, 1), (0, 2)]], [[1, 9], [(0, 1), (0, 2)]], [[9], [(0, 3)]], [[9], [(1, 1)]], [[8, 5], [(1, 1), (1, 2)]], [[8, 5], [(1, 1), (1, 2)]], [[5, 8], [(1, 2), (1, 3)]], [[5, 8], [(1, 2), (1, 3)]], [[3, 4], [(2, 0), (2, 1)]], [[3, 4], [(2, 0), (2, 1)]], [[4, 5], [(2, 1), (2, 2)]], [[4, 5], [(2, 1), (2, 2)]], [[5, 3], [(2, 2), (2, 3)]], [[5, 3], [(2, 2), (2, 3)]], [[8, 2], [(3, 0), (3, 1)]], [[8, 2], [(3, 0), (3, 1)]], [[2, 6], [(3, 1), (3, 2)]], [[2, 6], [(3, 1), (3, 2)]], [[6, 7], [(3, 2), (3, 3)]], [[6, 7], [(3, 2), (3, 3)]]]
    '''