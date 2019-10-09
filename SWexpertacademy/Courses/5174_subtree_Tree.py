import sys
sys.stdin = open('5174.txt', 'r')

'''
b. 전위 순회(pre-order traversal): 현재 노드 -> 왼쪽 가지 -> 오른쪽 가지
1. 현재 노드 n을 방문하여 처리 
2. 현재 노드 n의 왼쪽 서브트리로 이동
3. 현재 노드 n의 오른쪽 서브트리로 이동
'''

def preorder(n):   # 전위 순회
    global cnt
    if n != 0:
        cnt += 1   # 방문한 노드 개수
        # print(tree[n][0])
        # print('--',tree[n][1])
        preorder(tree[n][0])
        preorder(tree[n][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())   # 간선, 시작정점
    tree = [[0]*3 for i in range(E+2)]   # 정점의 개수는 간선보다 1개 크다 + 0열 추가
    # 테케는 자식이 최대 2개, [자식1, 자식2, 내부모] 의 자리를 만든다.
    temp = list(map(int, input().split()))
    # print(temp)
    cnt = 0

    for i in range(E):    # E개의 간선을 처리
        p = temp[i * 2]
        c = temp[i * 2 + 1]
        # print(p, c)
        if tree[p][0] == 0:
            tree[p][0] = c
        else:            # 이미 자식이 한 개 있는 경우
            tree[p][1] = c

        tree[c][2] = p  # 부모도 저장
    # print(N)
    preorder(N)
    # print(tree)
    print('#{} {}'.format(tc, cnt))