import sys
sys.stdin = open('5176.txt', 'r')
'''
이진 탐색 트리는
어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙

중위순회 : 왼쪽 -> 현재 -> 오른쪽


추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들수 있다.

N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과,
N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램
'''


def inorder(node):
    global idx, N

    if node <= N:   # 노드번호가 N보다 작은 경우만 실시 # node가 6보다 작거나 같을때까지
        inorder(node * 2)       # 왼쪽 서브트리 방문(*2를 처리하면 된다)
        tree[node] = idx
        # print(node, idx)
        # 중위 순회로 현재 노드값 저장
        idx += 1    # 다음 인덱스로 이동한다
        inorder(node * 2 + 1)   # 오른쪽 서브트리 방문(*2+1로 처리)


for tc in range(1, int(input())+1):
    N = int(input())  # 정점의 수
    idx = 1
    tree = [0 for i in range(N + 1)]  # 리스트를 이용한 완전 이진 트리 저장
    inorder(1) # 루트번호는 1부터시작한다.
    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))