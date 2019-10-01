import sys
sys.stdin = open('1247.txt', 'r')



'''
#1 200
#2 304
#3 366

회사와 집의 위치, 각 고객의 위치
이차원 정수 좌표 (x, y)로 주어지고 (0 ≤ x ≤ 100, 0 ≤ y ≤ 100)

두 위치 (x1, y1)와 (x2, y2) 사이의 거리는 |x1-x2| + |y1-y2|으로 계산

|x|는 x의 절대값을 의미하며 |3| = |-3| = 3이다. 
회사의 좌표, 집의 좌표, 고객들의 좌표는 모두 다르다.

회사에서 출발하여 N명의 고객을 모두 방문하고 집으로 돌아오는 경로 중 가장 짧은 것을 찾으려 한다.



회사와 집의 좌표가 주어지고, 2명에서 10명 사이의 고객 좌표가 주어질 때,

회사에서 출발해서 이들을 모두 방문하고 집에 돌아가는 경로 중
총 이동거리가 가장 짧은 경로를 찾는 프로그램을 작성


각 테스트 케이스의 첫째 줄에는 고객의 수 N이 주어진다. 
둘째 줄에는 회사의 좌표, 집의 좌표, N명의 고객의 좌표가 차례로 나열된다.
좌표는 (x,y)쌍으로 구성되는데 입력에서는 x와 y가 공백으로 구분되어 제공
'''
# import itertools
#
#
# def solve(xys):
#     global mymin
#
#     # 모든 xys를 계산식에 따라 돌면서 mymin을 갱신하되,
#     # 갱신된 mymin보다 클때 가지치기 해주면된다.
#
#     result = 0
#     for i in range(0, N+2-1):
#         result += abs(xys[i][0] - xys[i+1][0]) + abs(xys[i][1] - xys[i+1][1])
#
#     if result < mymin:
#         mymin = result
#     return
#
# for tc in range(int(input())):
#     N = int(input())
#     # 받고 나눠주기
#     mytemp = list(map(int, input().split()))
#     companyxy = (mytemp[0], mytemp[1])
#     housexy = (mytemp[2], mytemp[3])
#     customers = mytemp[4:]
#
#     all_customersxy = []
#     for idx in range(0, N*2, 2):
#         all_customersxy.append((customers[idx], customers[idx+1]))
#
#     # 뽑은 모든 경우의 수를 하나씩 for문으로 순회하면서 이동거리가 가장 짧은 경로를 찾는다.
#     # set에 값을 넣으면서 개수구하기
#     mymin = 99999
#     for i in itertools.permutations(all_customersxy):
#         candidate = [companyxy, *list(i), housexy]
#         solve(candidate)
#
#     print(f'#{tc+1}', mymin)
#

# import itertools
#
# def solve(xys):
#     global mymin
#     result = 0
#     for i in range(0, N+2-1):
#         result += abs(xys[i][0] - xys[i+1][0]) + abs(xys[i][1] - xys[i+1][1])
#
#     if result < mymin:
#         mymin = result
#     return
#
# for tc in range(int(input())):
#     N = int(input())
#     mytemp = list(map(int, input().split()))
#     companyxy = (mytemp[0], mytemp[1])
#     housexy = (mytemp[2], mytemp[3])
#     customers = mytemp[4:]
#
#     all_customersxy = []
#     for idx in range(0, N*2, 2):
#         all_customersxy.append((customers[idx], customers[idx+1]))
#
#     mymin = 99999
#     for i in itertools.permutations(all_customersxy):
#         candidate = [companyxy, *list(i), housexy]
#         solve(candidate)
#     print(f'#{tc+1}', mymin)


import itertools

def solve(xys):
    global mymin
    result = 0
    for i in range(0, N+2-1):
        result += abs(xys[i][0] - xys[i+1][0]) + abs(xys[i][1] - xys[i+1][1])

    mymin = min(mymin, result)
    return

for tc in range(int(input())):
    N = int(input())
    mytemp = list(map(int, input().split()))
    companyxy = (mytemp[0], mytemp[1])
    housexy = (mytemp[2], mytemp[3])
    customers = mytemp[4:]

    all_customersxy = []
    for idx in range(0, N*2, 2):
        all_customersxy.append((customers[idx], customers[idx+1]))

    mymin = 99999
    for i in itertools.permutations(all_customersxy):
        candidate = [companyxy, *list(i), housexy]
        solve(candidate)
    print(f'#{tc+1}', mymin)