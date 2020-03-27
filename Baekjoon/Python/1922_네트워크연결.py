import sys
sys.stdin = open('1922.txt', 'r')
def find(x):
    # 만약 x의 루트가 x 자신이라면, x는 x가 속한 트리의 루트이다.
    # 따라서 루트인 x를 반환한다.
    if root[x] == x:
        return x
    # 재귀호출로 올라오는 루트 번호를 root 리스트에 기록한다. (경로 압축)
    root[x] = find(root[x])
    # 그 루트를 계속해서 반환한다.
    return root[x]

def union(x, y):
    # 각 정점의 루트를 찾는다.
    print('-----------')
    print(root)
    print(rank)
    x = find(x)
    y = find(y)
    # 만약 x의 루트와 y의 루트가 같다면 둘은 같은 그래프에 속해 있는 것이다.
    # 따라서 x와 y를 잇게 되면 사이클이 형성된다.
    if x == y:
        return False
# x의 루트와 y의 루트가 같지 않을 때 union을 실행한다.
# 1) 트리의 높이가 낮은 쪽이 높은 쪽에게 합쳐지거나
# 2) 그래프의 크기가 작은 쪽이 큰 쪽에게 합쳐지게 된다.
# 여기선 트리의 높이를 기준으로 병합한다.
# 만약 rank[y]가 rank[x]보다 크면 == y가 속한 트리의 높이가 x가 속한 트리의 높이보다 높으면
    if rank[x] < rank[y]:
        # x의 루트를 y로 바꾼다.
        root[x] = y
    # 반대의 경우
    else:
        # y의 루트를 x로 바꾼다. 둘의 높이가 같을 경우에는 왼쪽인 x에게 y가 합쳐지게 된다.
        root[y] = x
        # 만약 두 트리의 높이가 같다면 트리가 합쳐졌을 때 높이가 1 증가하게 된다.
        if rank[x] == rank[y]:
            rank[x] += 1
    print(rank)
    print(root)
    return True

input = sys.stdin.readline
N = int(input())
M = int(input())
# 1. 각 정점들의 루트가 기록될 root 리스트와, 트리의 높이를 기록할 rank 리스트를 만들어 놓는다.
root = [i for i in range(N + 1)]
rank = [0] * (N + 1)
res = 0
edges = [list(map(int, input().split())) for _ in range(M)]

# 2. 간선을 가중치 기준 오름차순으로 정렬한다.
edges.sort(key=lambda x: x[2])
for n1, n2, w in edges:
    # 3. 두 정점을 union한다.
    # 만약 union에 실패했다면, 두 정점을 이었을 때 사이클이 형성된다는 뜻이므로 간선을 잇지 않는다.
    if union(n1, n2):
        res += w
print(res)