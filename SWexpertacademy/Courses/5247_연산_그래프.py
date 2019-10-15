import sys
sys.stdin = open('5247.txt', 'r')


'''
#1 3
#2 4
#3 8
+1, -1, *2, -10
2 7
3 15
36 1007
N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산
'''


import collections

num_lst = {} # 모든 테케를 돈 dp를 계속 가지고 있기때문에 훨씬 빠르다.
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    result = 0
    depth = 0
    q = collections.deque([])
    q.append((N, depth)) # N 시작 번호와 depth

    while result != M:
        result, depth = q.popleft()
        num_lst[result] = tc

        for i in range(4):
            if i == 0:
                res = result + 1
                # 만약 num_lst안에 있는 res의 키값으로 불렀을때 해당하는 tc가 아닌 경우, 다음을 실행한다.
                if 0 < res <= 1000000 and num_lst.get(res) != tc:
                    q.append((res, depth + 1))
                    num_lst[res] = tc
            elif i == 1:
                res = result - 1
                if 0 < res <= 1000000 and num_lst.get(res) != tc:
                    q.append((res, depth + 1))
                    num_lst[res] = tc
            elif i == 2:
                res = result * 2
                if 0 < res <= 1000000 and num_lst.get(res) != tc:
                    q.append((res, depth + 1))
                    num_lst[res] = tc
            elif i == 3:
                res = result - 10
                if 0 < res <= 1000000 and num_lst.get(res) != tc:
                    q.append((res, depth + 1))
                    num_lst[res] = tc
    print(f'#{tc}', depth)


# def cals(a, b):
#
#     if b == '+1':
#         res = a + 1
#         return res
#     if b == '-1':
#         res = a - 1
#         return res
#     if b == '*2':
#         res = a * 2
#         return res
#     if b == '-10':
#         res = a - 10
#         return res
#
# def start(num, depth):
#     global tools, M, mydepth
#
#     dp[depth] = (0, 0)
#     if num == M:
#         if depth < mydepth:
#             mydepth = depth
#             return
#
#     nums = []
#     for temp in ['+1', '-1', '*2', '-10']:
#
#         if dp[depth].get((num, temp)) == None:
#             newnum = cals(num, temp)
#             nums.append(newnum)
#             dp[depth][(num, temp)] = newnum
#
#         elif dp[depth].get((num, temp)) != None:
#             nums.append(dp[depth].get((num, temp)))
#
#
#     for one in nums:
#         start(one, depth+1)
#
# dp = [{} for _ in range(1000000)]
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     # 4개의 다른 tools로 분할해서 시작하는 것
#     # M을 만나거나 연산의 중간결과가 100만 이상이 되면 return한다.
#     mydepth = 999999
#     result, cntresult = start(N, 0)
#     print(mydepth)