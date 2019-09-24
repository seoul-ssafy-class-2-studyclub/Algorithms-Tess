import sys
sys.stdin = open('5208.txt', 'r')


'''
유망하지 않으면 그 부모노드로 돌아가서 유망한 다른 노드를 시도한다.
그러므로 백트래킹은 DFS를 사용해서 푼다.
"스택을 사용하고, 넣기 전에 유망성을 검사한다"
즉, 유망하지 않는 자식은 스택에 넣지 않는다.
유망한 자식만 넣어서 트래킹한다.
가지치기가 중요하다.

 : 해를 찾는 도중에 막히면 즉, 해가 아니면 되돌아가서 다시 해를 찾아 가는 기법.
- 최적화 문제와 결정 문제 해결 가능.
- 탐색 과정에서 해가 될 수 없는 경우들은 탐색 범위에서 제외되기 때문에 완전 검색에 비해 효율적.
- 상태 공간 트리에 기반하여 탐색 수행.
- 상태공간 트리
- 해를 찾기 위한 과정을 트리로 표현
- 내부 노드는 최종상태로 가는 중간 상태 표현
- 단말 노드는 하나의 후보해에 대한 최종 상태
- 트리를 깊이 우선 탐색하는 방법이 백트래킹 알고리즘의 기본 형태
- 깊이 우선 탐색은 모든 경로를 추적하는 데 비해 백트래킹은 가지치기로 불필요한 경로 조기 차단 가능.
- 경우의 수가 너무 많은 경우, 즉 N! 의 경우의 수를 가진 문제에 대해 DFS를 가하면 경우의 수가 너무 많아져서 처리 불가능.
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들게 되어 처리 가능.
- but, 최악의 경우에는, 지수함수 시간을 요하므로 처리 불가능.
'''
'''
3
5 2 3 1 1
'''

# 백트래킹

# def backtracking(now, mybattery, charge=0):
#     global minchargenum
#
#     if minchargenum < charge:
#         return
#
#     # 자신의 자식노드의 유망성을 점검한다.
#     starts = [i for i in range(now + 1, now+1+stations[now])]
#     # print(starts)
#     if N-1 in starts:
#         if minchargenum > charge:
#             minchargenum = charge
#             return
#
#     else:
#         for i in starts:
#             new_now = i
#             backtracking(new_now, stations[new_now], charge+1)
#
#
#
# for tc in range(int(input())):
#     stations = list(map(int, input().split())) + ['G']
#
#     N = stations.pop(0)
#     # print(stations)
#     #
#     # print(N)
#     # battery[0] # 첫 시작점이 될 수 있는 노드 인덱스들까지라고 했지만,
#     # 사실
#     # 나의 현재위치에서 유망한 다음 인덱스들을 모두 거쳐가면서(stack에 넣고) minchargenum을 갱신한다.
#     # - 버리는 경우
#     # minchargenum보다 클때 가지치기하기
#     # 하나씩 움직일때마다 -1할 필요없고, 내 자식에 바로 갔을때 충전하고 그 자식의 자식에서 충전하는 식으로 최적해를 찾아나간다.
#     pos = 0
#     battery = stations[0]
#     minchargenum = 99999
#     backtracking(pos, battery)
#     print(f'#{tc+1}', minchargenum)



## DP

def DP():
    global dp
    # 1. 뒤에서부터 보면서 각 부모가될 자식들이 가지는 배터리 횟수를 갱신해나간다.
    for idx in range(N - 1 ,0, -1): # 현재위치
        # 4 3 2 1
        # 4+1 = 5
        if idx + stations[idx] >= N:
            dp[idx] = 1
        else:
            children = idx+stations[idx]
            temp = 9999
            for child in range(children, idx, -1):
                if dp[child] != 0 and temp > dp[child]:
                    temp = dp[child]
            dp[idx] = temp + 1
    return

for tc in range(int(input())):
    stations = list(map(int, input().split()))
    N = stations[0]
    dp = [0]*N
    DP()
    print(dp[1]-1)









#
# def dfs_recursion(bat, visited, nowbattery, chargeN, pos, path):
#     global mymin
#
#     if 0 <= pos < N:
#         if bat[pos] == 'G':
#             if mymin > chargeN:
#                 mymin = chargeN
#                 return
#         if nowbattery > 0 and visited[pos+1] == False:
#             visited[pos] = True
#             path.append(pos+1)
#             dfs_recursion(bat, visited, nowbattery - 1, chargeN, pos + 1, path)
#
#         elif nowbattery == 0 and visited[pos] == False and bat[pos]:
#             visited[pos] = True
#             dfs_recursion(bat, visited, bat[pos], chargeN + 1, pos, path)
#
#     return
#
#
#
# for tc in range(int(input())):
#     battery = list(map(int, input().split())) + ['G']
#     print(battery)
#     N = len(battery)+1
#     vis = [False]*N
#     vis[0] = True
#     mymin = 999999
#     current = 1
#     dfs_recursion(battery, vis, battery[0], 0, current, [])
#     print(mymin)
