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

import sys
input = sys.stdin.readline

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
            continue
        if arr[s][e] == 0:
            arr[s][e] = 1
            arr[e][s] = 0
            inDegree[s] -= 1
            inDegree[e] += 1

    thisYear = [0]*(tiNum+1) ## 들어갈 자리를 만들어준다.

    q = []
    for idx in range(1, tiNum+1):
        if inDegree[idx] == 0: # 0 이라면 시작점이 될 수 있다.
            q.append(idx)
            ans = str(idx)

    # 중간 q 개수 세는거
    # q에는 무조건 하나만 들어가야 한다.
    i = 1
    while True:
        if len(q) == 1:
            s = q.pop(0)
            thisYear[i] = s
            i += 1
            for j in range(1, tiNum+1):
                if arr[s][j] == 1:
                    inDegree[j] -= 1
                    if inDegree[j] == 0:
                        q.append(j)
                        ans += ' ' + str(j)

        if i < tiNum and len(q) == 0: # cycle
            ans = 'IMPOSSIBLE'
            break

        elif len(q) >= 2: # 같은 등수
            ans = '?'
            break

        elif len(q) == 0: # 제대로 된 경우
            ans = ans
            break

    print(ans)
