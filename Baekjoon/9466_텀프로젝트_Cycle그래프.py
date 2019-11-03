'''
3
0
'''

import sys
sys.stdin = open('9466.txt', 'r')
sys.setrecursionlimit(10**6)
'''
Cycle을 확인해서 하나의 팀인 애들을 확인하기 위해서는 아래와 같은 요소들이 필요하다.
1) 각각의 학생을 방문했는지에 대한 유무 (visited)
2) 방문할 때마다 몇 번 째로 방문했는지 (cnt)
3) 방문할 때 가장 첫 번째로 시작한 학생이 누구인지를 각각 비교해야 한다. (cycle 확인)
'''

def find(start, parent, cnt, pre):
    global visited
    visited[parent] = True
    res[start].append(parent, cnt)
    if visited[start] == True:
        return (res[pre], res[start])


    elif visited[start] == False:
        find(arr[start], parent, cnt+1, start)


T = int(input())
for _ in range(T):

    N = int(input())
    arr = [0]*(N+1)
    data = list(map(int, input().split()))

    sub = 0
    for i in range(1, N+1):
        # 1. 그래프를 1부터 시작해서 그린다.
        arr[i] = data[i-1]
    # 2. 그러한 경우를 제외한 시작점에서 시작해서 다시 시작점으로 돌아오는 사이클을 가진 한 팀인지 확인한다.

    visited = [False]*(N+1)
    res = [[] for _ in range(N+1)] # 시작의 부모와 cnt를 저장할 곳
    for i in range(1, N+1):
        if not visited: # False 라서 방문하지 않았다면,
            # 비지않았다면 들어간다.
            ans = find(arr[i], i, 2, i)
    print(ans)
'''
import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()


def make_group(x, cnt, step):
    # step은 시작정점
    global d, check, s
    # 탐색할수록 정점의 개수(cnt)는 늘어간다.
    # d 배열에 탐색할때마다 해당 정점을 기준으로 탐색된 정점의 개수를 저장한다.

    while True:
        if check[x] != False:
            # 이미 들어간거
            if step != s[x-1]:
                # 이미 방문했고, 정점 시작점이 다를 경우 사이클 x
                return 0
            return cnt - check[x]
            # 그러던 중 사이클이 존재하면, 사이클이 존재하는 정점을 인덱스로 활용하는 것이다.
            # (탐색된 정점 개수 - 사이클 정점에 대한 길이)를 통해 사이클을 이루는 정점의 개수를 구하게 된다.

        check[x] = cnt
        # check는 x에 도착했을 때 탐색한 개수를 저장하는 곳이다.
        s[x-1] = step
        # x가 어디에서 시작했는지를 알려주는 것
        x = d[x]
        # 다음애...
        cnt += 1

for _ in range(int(read())):
    n = int(read())
    check = [False]*(n+1)

    d = {}
    s = list(map(int, read().split()))
    for i in range(1, n+1):
        d[i] = s[i-1]

    ans = 0
    for i in d:
        if check[i] == False:
            ans += make_group(i, 1, i);

    print(n-ans)
'''

