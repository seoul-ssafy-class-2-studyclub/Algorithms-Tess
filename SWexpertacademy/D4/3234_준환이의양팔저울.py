import sys
sys.stdin = open('3234.txt', 'r')


def solve(i, left, right, visi, cnt, now):

    visi = visi[:]
    visi[i] = True
    if dp[now] != -1:
        return dp[now]

    if left < right: # 가지를 먼저 쳐야함
        return 0

    if cnt == N:
        return 1 # 맨마지막에서 올라감

    else:
        res = 0
        for i in range(N):
            if visi[i] == False and left >= right:
                res += solve(i, left+candi[i], right, visi, cnt+1, now + (1 << i + N)) # 왼쪽
                res += solve(i, left, right+candi[i], visi, cnt+1, now + (1 << i)) # 오른쪽
    dp[now] = res
    return res
for tc in range(int(input())):
    N = int(input())
    candi = list(map(int, input().split()))
    vis = [False] * N
    dp = [-1] * (1 << N * 2)
    result = []
    res = 0
    for i in range(N):
        if vis[i] == False:
            visited = [False] * N
            res += solve(i, candi[i], 0, visited, 1, 1 << i + N)
            # 이진법으로 숫자가 위치한 자리를 저장해서 중복을 제거
            #

    print(f'#{tc+1}', res)

    '''
    1 << 2 -> 100
    '''
    # print(1<<2)






#
# #
# def solve(i, left, right, visi, cnt):
#     global res
#     visi = visi[:]
#     visi[i] = True
#
#     # if left < right or dpleft[cnt].get(left) == visi or dpright[cnt].get(right) == visi: # 가지치기
#     #     return
#     #
#     # if dpleft[cnt].get(left) == None or dpright[cnt].get(right) == None: # 아직 dp에 없다면,
#     #     dpleft[cnt][left] = visi # visi을 값으로 저장해준다.
#     #     dpright[cnt][right] = visi # visi을 값으로 저장해준다.
#     #     if cnt == N:  # 완성된 경우, 더해준다.
#     #         res += 1
#     #         return
#     #
#     #     for i in range(N):
#     #         if visi[i] == False and left >= right:
#     #             solve(i, left+candi[i], right, visi, cnt+1)
#     #             solve(i, left, right+candi[i], visi, cnt+1)
#
#     # if left < right or dp[cnt].get((left, right)) == visi: # 가지치기
#     #     return
#     #
#     # if dp[cnt].get((left, right)) == None: # 아직 dp에 없다면,
#     #     dp[cnt][(left, right)] = visi # visi을 값으로 저장해준다.
#     #     if cnt == N:  # 완성된 경우, 더해준다.
#     #         res += 1
#     #         return
#     #
#     #     for i in range(N):
#     #         if visi[i] == False and left >= right:
#     #             solve(i, left+candi[i], right, visi, cnt+1)
#     #             solve(i, left, right+candi[i], visi, cnt+1)
#
#     # print(dp[cnt].get(tuple(visi)))
#     # if left < right:
#     #     return
#     #
#     # if dp[cnt].get(tuple(visi)) != None: # 가지치기
#     #     if (left, right) in dp[cnt].get(tuple(visi)):
#     #         return
#     #     else:
#     #         dp[cnt][tuple(visi)].append((left, right))
#     #
#     # if cnt == N+3:  # 완성된 경우, 더해준다.
#     #     res += 1
#     #     return
#     #
#     # if dp[cnt].get(tuple(visi)) == None: # 아직 dp에 없다면,
#     #     dp[cnt][tuple(visi)] = []
#     #     dp[cnt][tuple(visi)].append((left, right)) # visi을 값으로 저장해준다.
#     #     for i in range(N):
#     #         if visi[i] == False and left >= right:
#     #             solve(i, left+candi[i], right, visi, cnt+1)
#     #             solve(i, left, right+candi[i], visi, cnt+1)
#     #
#     if left < right:
#         return
#
#     if dp[cnt].get(tuple(visi)) != None: # 가지치기
#         print(dp[cnt].get(tuple(visi)))
#         if (left, right) in dp[cnt].get(tuple(visi)):
#             dp[cnt][tuple(visi)][(left, right)] += 1
#             return
#
#     if cnt == N+3:  # 완성된 경우, 더해준다.
#         res += 1
#         return
#
#     if dp[cnt].get(tuple(visi)) == None: # 아직 dp에 없다면,
#         dp[cnt][tuple(visi)] = {}
#         dp[cnt][tuple(visi)][(left, right)] = 1 # visi을 값으로 저장해준다.
#         for i in range(N):
#             if visi[i] == False and left >= right:
#                 solve(i, left+candi[i], right, visi, cnt+1)
#                 solve(i, left, right+candi[i], visi, cnt+1)
#
#
#
#
#
# for tc in range(int(input())):
#     N = int(input())
#     candi = list(map(int, input().split()))
#     vis = [False] * N
#     result = []
#     res = 0
#     # dp = [{} for i in range(N+1)]
#     dp = [{} for i in range(N+1)]
#     print(dp)
#
#     for i in range(N):
#         if vis[i] == False:
#             visited = [False] * N
#             solve(i, candi[i], 0, visited, 1)
#
#     # print(dpright[-1], dpleft[-1])
#     print(dp)
#     print(f'#{tc+1}', res)



'''
제한시간초과
def solve(i, left, right, visi, cnt):
    global res
    visi = visi[:]
    visi[i] = True

    if left < right: # 가지를 먼저 쳐야함
        return

    if cnt == N:
        res += 1
        return

    else:
        for i in range(N):
            if visi[i] == False and left >= right:
                solve(i, left+candi[i], right, visi, cnt+1)
                solve(i, left, right+candi[i], visi, cnt+1)

for tc in range(int(input())):
    N = int(input())
    candi = list(map(int, input().split()))
    vis = [False] * N
    result = []
    res = 0
    for i in range(N):
        if vis[i] == False:
            visited = [False] * N
            solve(i, candi[i], 0, visited, 1)
    print(f'#{tc+1}', res)
'''