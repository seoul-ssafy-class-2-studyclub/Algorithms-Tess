import sys
sys.stdin = open('11725.txt', 'r')

'''
7
1 6
6 3
3 5
4 1
2 4
4 7

4
6
1
3
1
4
'''


'''
루트 없는 트리가 주어진다. 
이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''

def find(n):
    global result, visit

    q = []
    q.append((adj_list[n], n))
    while q:
        children, parent = q.pop(0)
        for ix in children:
            if result[ix] == 0:
                result[ix] = parent
                q.append((adj_list[ix], ix))


# 트리의 입력을 그래프처럼 인접리스트로 받은 후에 BFS로 탐색하며 parent 배열에 부모노드 번호를 저장
N = int(input())
adj_list = [[] for i in range(N+1)]

temp = set()
for i in range(1, N):
    e = list(map(int, input().split()))
    adj_list[e[0]].append(e[1])
    adj_list[e[1]].append(e[0])

# BFS로 현재의 부모 출력? 각 노드의 부모를 출력한다.
result = [0]*(N+1)
find(1)

print('\n'.join(map(str, result[2:])))
# print()