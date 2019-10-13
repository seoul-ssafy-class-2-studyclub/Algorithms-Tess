import sys
# sys.stdin = open('1231.txt', 'r')

'''
나중에 다시 한 번 확인할 것
'''


for tc in range(1, 11):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    ch = [''] * (N + 1)

    for i in range(N):
        arr = list(input().split())

        id = int(arr[0])
        ch[id] = arr[1]
        if len(arr) > 2: # 자식이 한명이라면,
            # print(arr)
            L[id] = int(arr[2])
        if len(arr) > 3: # 입력 노드가 자식이 두명이라면, 입력값에서의 3 인덱스의 자식도 추가한다.
            # print(arr)
            R[id] = int(arr[3])

    # print(L)
    # print(R)
    # print(ch)

    # 왼쪽 -> 현재 -> 오른쪽 순으로 확인한다.
    # 재귀를 호출할때, 왼쪽, 오른쪽 순으로 호출하고, 재귀가 나오면서
    def inorder(v):
        if v == 0: # 0이 나오면 더이상 나올게 없는 단말노드이다. 이러면 재귀가 끝난다.
            return
        inorder(L[v]) # 0을 만나서 나올게 없어 재귀가 끝난 재귀는 값을 갖고 오는데, 끝난 시점에서부터 값을 끌고온다.

        print(ch[v], end='') # 가져온 값을 출력한다. == 현재

        inorder(R[v]) # 그리고, 오른쪽에 대한 재귀를 호출한다.
    # print(ch)
    print('#{} '.format(tc), end='')
    inorder(1) # 1부터 시작해서 방문한다.
    print()
