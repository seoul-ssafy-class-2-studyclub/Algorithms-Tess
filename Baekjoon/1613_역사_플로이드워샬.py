import sys
sys.stdin = open('1613.txt', 'r')
#
# from pprint import pprint
# '''
# 0
# -1
# 1
# '''
#
# n, k = map(int, input().split())
#
# adj_arr = [[0]*(n+1) for _ in range(n+1)]
# indegree = [0]*(n+1)
# recognition = [False]*(n+1)
# for _ in range(k):
#     P, C = map(int, input().split())
#     adj_arr[P][C] = -1
#     adj_arr[C][P] = 1
#     indegree[C] += 1
#     if not recognition[P]:
#         recognition[P] = True
#     if not recognition[C]:
#         recognition[C] = True
#
# # print(adj_arr)
# # print(indegree)
# q = []
# for idx in range(1, n+1):
#     if indegree[idx] == 0 and recognition[idx] == True:
#         q.append(idx)
#
# res = []
# while q:
#
#     for _ in range(len(q)):
#         p = q.pop(0)
#         res.append(p)
#         for idx in range(1, len(adj_arr[p])):
#             if adj_arr[p][idx] == -1:
#                 indegree[idx] -= 1
#                 if indegree[idx] == 0:
#                     q.append(idx)
# # pprint(adj_arr)
# # print(indegree)
# # print(res)
#
# # for name in res:
# #     for idx in range(1, n+1):
# #         if recognition[idx] == True:
# #             if adj_arr[name][idx] == 0:
# #                 adj_arr[name][idx] = -1
# #                 adj_arr[idx][name] = 1
# # pprint(adj_arr)
# ans = []
# tc = int(input())
# for _ in range(tc):
#     F, B = map(int, input().split())
#     ans.append(adj_arr[F][B])
# print('\n'.join(map(str,ans)))



'''
플로이드 와샬 알고리즘은 단 4줄이기 때문에 외우기 굉장히 쉽다.
for k for i for j ,  ij, ikj 이렇게만 외우면 끝
플로이드를 돌린 후
서로 다른 두 사건의 번호가 주어질 때(만약 a,b라고 주어질 때)
D[a][b] != INF 이면 -1
D[b][a] != INF 이면 1
D[a][b] == INF 이면 0을 출력하면 된다.
'''
import sys
input = sys.stdin.readline
n,m=map(int,input().split())

Max = 1e9
S = [[Max]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    S[a][b] = 1

for k in range(n+1): # 거쳐 가는 곳
    for i in range(n+1): # 시작
        for j in range(n+1): # 도착
            S[i][j] = min(S[i][j], S[k][j]+S[i][k])
res = []
for i in range(int(input())):
    a,b = map(int,input().split())
    if S[a][b] != Max:
        res += ['-1']
        continue
    elif S[b][a] != Max:
        res += ['1']
        continue
    else:
        res += ['0']
print('\n'.join(res))




