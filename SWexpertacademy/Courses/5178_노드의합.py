import sys
sys.stdin = open('5178.txt', 'r')

# 리프노드 값을 입력받아 저장한다.
# 1부터 노드의 수까지 재귀를 통해 
# 나머지 Tree를 채운다.

# def postOrder(node):           # 후위 순회
#     global N # 5
#     if node > N: # 1 > 5       # 유효한 노드(리프노드)가 아니면 0 반환
#         return 0
#     else:
#         if tree[node] != 0:    # 리프노드인 경우 저장된 값 리턴
#             return tree[node]
#         else:
#             a = postOrder(2 * node)   # 왼쪽 자식으로 이동
#             b = postOrder(2 * node + 1)   # 오른쪽 자식으로 이동
#             tree[node] = a + b    # 양쪽의 값을 더해서 부모 노드(현재)에 저장
#         return tree[node]       # 노드에 저장된 값을 반환

# T = int(input())


# for tc in range(1, T + 1):
#     N, M, L = map(int, input().split())  # 노드의 수, 리프노드의 수, 값을 출력할 노드번호
#     tree = [0 for i in range(N + 1)]    # 트리 생성

#     for i in range(M):
#         idx, value = map(int, input().split())  # 리프노드 값을 입력받아 저장
#         tree[idx] = value
#     postOrder(1) # 1부터 노드의 수까지 재귀
#     print('#{} {}'.format(tc, tree[L]))
#     #print(tree)

def postOrder(node):
    global N
    # node가 N보다 크면 재귀를 종료하고,
    if node > N:
        return 0
    else:
    # node가 N보다 작으면 재귀 시작 및 tree를 채운다.
        # node가 리프노드인경우, 저장된 리프노드의 값을 리턴한다.
        if tree[node] != 0:
            return tree[node]
        else:
            a = postOrder(2 * node)
            b = postOrder(2 * node + 1)
            tree[node] = a + b # 리프노드가 아닌 node에 자식값들이 더해진 값을 저장한다.
        return tree[node]

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0 for i in range(N+1)]

    for i in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    postOrder(1)
    print(f'#{tc} {tree[L]}')


'''
정확한 답이 나오지 않았다.
'''

# for tc in range(1, int(input())+1):
#     # 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
#     # 다음 줄부터 M개의 줄에 걸쳐 리프 노드 번호와 1000이하의 자연수가 주어진다.
#     N, M, L = map(int, input().split())
#     Tree = [0 for i in range(N+1)]
#     for i in range(M):
#         ln, value = map(int, input().split())
#         Tree[ln] = value

#     print(Tree)

#     for i in range(N, -1, -2):
#         p = i//2
#         Tree[i//2] = Tree[i] + Tree[i-1]
#     print(Tree)
#     print(f'#{tc} {Tree[L]}')
