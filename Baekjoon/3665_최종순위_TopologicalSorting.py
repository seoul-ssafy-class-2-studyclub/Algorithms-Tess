import sys
sys.stdin = open('3665.txt', 'r')

'''
5 3 2 4 1
2 3 1
IMPOSSIBLE

n개의 정수를 한 줄에 출력한다. 

출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력한다. -> N과 같으면 출력

만약, 확실한 순위를 찾을 수 없다면 "?"를 출력한다. -> N보다 작다?
-> 진입차수가 0인 노드가 한개가 아닌 경우이다. 즉, 동일한 등수를 가진 원소가 존재하기 때문에
확실하게 순위를 정할 수 없다는 뜻이다.
즉, q의 개수가 1을 초과하는 경우를 말한다.


데이터에 일관성이 없어서 순위를 정할 수 없는 경우에는 
"IMPOSSIBLE"을 출력한다.
-> 즉 2-3
     3-2
     처럼 사이클이 발생하는 경우이다.
     이런 경우는 진입차수가 0인 노드가 없게 된다. 
     왜냐하면 결국 다른 끝점에서 시작점으로 다시 연결되어 버리는 경우도 있기때문에

'''



'''
q는 진입차수가 0인 노드가 들어가는 구조
thisYear은 위상정렬의 결과값이 들어가는 구조

진입차수가 0인 노드를 queue에 넣고, queue에서 하나를 빼고 진입차수를 줄이고,
'''



# 높은 등수를 가장 먼저 방문하기 위해 진입으로 만들 것
n = int(input())
for _ in range(n):
    tiNum = int(input())
    lastYear = list(map(int, input().split()))

    ## 작년 순위를 기준으로 인접행렬 생성
    ## 리스트로 하면 관리하기 바로바로 빼기가 힘들어서 행렬로 관리해야한다.
    arr = [[0]*(tiNum+1) for _ in range(tiNum+1)]
    ## 진입차수 생성
    inDegree = [0]*(tiNum+1)
    for i in range(0, tiNum):
        for j in range(i+1, tiNum):
            arr[lastYear[i]][lastYear[j]] = 1
            inDegree[lastYear[j]] += 1
    m = int(input())

    ######### 문제는 뭐냐.........하..........
    for idx in range(1, m+1):
        s, e = map(int, input().split())
        # 상하관계를 바꾼다고 했었는데,
        if arr[s][e] == 1: ## 작년에 더 우위에 있었다면 상하관계를 바꿔준다.
            arr[s][e] = 0
            arr[e][s] = 1
            inDegree[s] += 1
            inDegree[e] -= 1
        else:
            arr[s][e] = 1
            arr[e][s] = 0
            inDegree[s] -= 1
            inDegree[e] += 1


    thisYear = [0]*(tiNum+1) ## 들어갈 자리를 만들어준다.

    q = []
    for idx in range(1, tiNum+1):
        if inDegree[idx] == 0: # 0 이라면 시작점이 될 수 있다.
            q.append(idx)

    startpoint = len(q) # 이걸로 세 종류의 답을 도출해낸다
    if startpoint == 1:
        i = 1
        while q:
            s = q.pop(0)
            thisYear[i] = s
            for j in range(1, tiNum+1):
                if arr[s][j] == 1:
                    inDegree[j] -= 1
                    if inDegree[j] == 0:
                        q.append(j)
            i += 1
        print(' '.join(map(str, thisYear[1:])))
    if startpoint == 0:
        print('IMPOSSIBLE')
    if startpoint > 1:
        print('?')


















#
# # 높은 등수를 가장 먼저 방문하기 위해 진입으로 만들 것
# n = int(input())
# for _ in range(n):
#     tiNum = int(input())
#     lastYear = list(map(int, input().split()))
#     names = dict()
#     for idx, val in enumerate(lastYear):
#         names[val] = idx
#
#     lastInDegree = [ i for i in range(0, tiNum)]
#
#     m = int(input())
#
#     ######### 문제는 뭐냐.........하..........
#     for idx in range(1, m+1):
#         s, e = map(int, input().split())
#         # 상하관계를 바꾼다고 했었는데,
#         lastInDegree[names[e]] += 1
#         lastInDegree[names[s]] -= 1
#         # names[e], names[s] = names[s], names[e]
#         # print(lastInDegree)
#
#     inDegree = [0] * (tiNum + 1)
#     ## index를 팀 이름으로 해서 진입 차수를 새로 짠다.
#     for idx, val in enumerate(lastInDegree):
#         inDegree[lastYear[idx]] = val
#     # print(inDegree) # [0, 4, 2, 1, 3, 0] 이런식으로 만들었음
#     # print(inDegree)
#     thisYear = []
#     # 새로 얻은 진입차수 정보를 가지고 만들면 되는데,
#     # (진입차수, 인덱스)로 저장해서 sort한다
#     q = []
#     # print(inDegree)
#     for idx in range(1, tiNum+1):
#         if inDegree[idx] == 0:
#             # inDegree[idx] = -1
#             q.append(idx)
#     # print(q)
#     if len(q) >= 1:
#         while q:
#             s = q.pop(0)
#             thisYear.append(s)
#             for idx in range(1, tiNum+1):
#                 if inDegree[idx] != 0:
#                     inDegree[idx] -= 1
#                     if inDegree[idx] == 0:
#                         # inDegree[idx] = -1
#                         q.append(idx)
#         print(' '.join(map(str, thisYear)))
#     elif len(q) == 0:
#         print('IMPOSSIBLE')
#     elif len(q) > 1:
#         q = '?'
#         print(q)
#
#




# import sys
# sys.stdin = open('3665.txt', 'r')
#
# '''
# 5 3 2 4 1
# 2 3 1
# IMPOSSIBLE
#
# n개의 정수를 한 줄에 출력한다.
#
# 출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력한다. -> N과 같으면 출력
#
# 만약, 확실한 순위를 찾을 수 없다면 "?"를 출력한다. -> N보다 작다?
#
# 데이터에 일관성이 없어서 순위를 정할 수 없는 경우에는
# "IMPOSSIBLE"을 출력한다. -> N보다 작다
# '''
#
#
# # 5가 일등인건데
# # 그럼 2-4면, 2가 앞이고!
# # 2 4
# # 3 4
#
# # 5 4 3 2 1 -> 0, 1, 2, 3, 4 이러한 진출차수가 형성되어있는데,
# # 2 4 이렇게 바뀌었다면,
# # 진출차수는 이렇게 바뀔 것, 바로 4의 진출차수가 하나 늘어났다는 이야기다.
# # 그리고 2의 진출차수가 하나 줄었다는 이야기다.
# # 0, 2, 2, 2, 4
# # 3 4
# # 0, 3, 2, 1, 4
#
# # 이렇게 만들어진 수를 가지고 정렬하면 되는데, 바뀐다는 정보를 얻는 곳 빼고만 바꿔야 한다.
#
#
# # 5 3 2 4 1
#
# # 높은 등수를 가장 먼저 방문하기 위해 진입으로 만들 것
# n = int(input())
# for _ in range(n):
#     # print('======')
#     tiNum = int(input())
#     lastYear = list(map(int, input().split()))
#     names = dict()
#     for idx, val in enumerate(lastYear):
#         names[val] = idx
#     # print(names)
#     lastInDegree = [ i for i in range(0, tiNum)]
#     # print(lastInDegree)
#
#     m = int(input())
#     adj_list = [[] for _ in range(tiNum+1)] # 1~n까지 존재하므로
#     inDegree = [0]*(tiNum+1)
#     # if m == 0:
#     #     thisYear = lastYear
#     # print(inDegree)
#     for idx in range(1, m+1):
#         s, e = map(int, input().split())
#         lastInDegree[names[e]] += 1
#         lastInDegree[names[s]] -= 1
#     # print(lastInDegree)
#
#     thisYear = []
#     # 새로 얻은 진입차수 정보를 가지고 만들면 되는데,
#     # (진입차수, 인덱스)로 저장해서 sort한다
#     toSort = []
#     for idx, val in enumerate(lastInDegree):
#         toSort.append((val, idx))
#
#     toSort = list(sorted(toSort))
#     # print(toSort)
#     for dump, idx in toSort:
#         # print(idx, dump)
#         thisYear.append(lastYear[idx])
#         if dump == -1:
#             thisYear = 'IMPOSSIBLE'
#             break
#     # print(thisYear)
#
#     #     adj_list[s].append(e)
#     #     inDegree[e] += 1
#     # print(adj_list)
#     # print(inDegree)
#     #
#     # q = []
#     # for idx in range(1, m+1):
#     #     if inDegree[idx] == 0:
#     #         inDegree[idx] = -1
#     #         q.append(idx)
#     # while q:
#     #
#     #     for _ in range(len(q)):
#     #         s = q.pop(0)
#     #         thisYear.append(s)
#     #
#     #         for e in adj_list[s]:
#     #             inDegree[e] -= 1
#     #             if inDegree[e] == 0:
#     #                 q.append(e)
#
#     if thisYear != 'IMPOSSIBLE':
#         print(' '.join(map(str, thisYear)))
#     else:
#         print(thisYear)
#
# ## 위는 50%에서 끝난다.



