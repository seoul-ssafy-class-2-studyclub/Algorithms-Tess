import sys
sys.stdin = open('5177.txt', 'r')

# 완전이진트리를 만들어야 한다 + 부모는 자식보다 작아야 한다(삽입할 경우 부모만 비교하면 된다)
# 루트만 삭제되어야 하고 삽입을 해도 완전이진트리를 유지해야 한다 = 힙 정렬
# 힙을 만드는 이유는 우선순위 큐를 만들기 위함 -> 2차원 배열로 만들어도 정렬이 가능하나 각 배열을 모두 탐색해야 하므로 n^2이 걸리기 때문
# 그림으로 그릴 수 있으면 만들 수 있다

'''
enQ : 추가하기
'''

def enQ(n): # 0이 들어온 경우, # 1이 들어온 경우
    global last
    last += 1  # 마지막 노드번호 증가
    c = last   # 마지막 노드를 자식 노드로
    p = c // 2  # 부모 노드 번호 계산 # 1//2 -> 0.5 -> 0 # 2//2 -> 1
    # print(3//2)
    Q[last] = n  # 마지막 노드에 값 저장 # Q[1] = 7 # Q[2] = 2

    # c = 2 and 7 > 2 이 경우 swap을 시작한다. 아닐때까지. p = 1, c = 2 
    while c > 1 and Q[p] > Q[c]:  # c가 루트가 아니고, 부모 노드의 값이 더 크면(c=1이면 0이 되므로)
        Q[p], Q[c] = Q[c], Q[p]  # 저장된 값 바꿈 # swap을 하고,
        c = p  # 바뀐 값에 맞춰서 c를 바꿔주고,
        p = p // 2 # c의 p또한 찾아준다.


'''
deQ : 삭제하기
1. 루트 노드의 원소 삭제
2. 마지막 노드를 루트 노드 위치로 이동
3. 삽입노드 < 자식노드 비교하여 자리 바꾸기
4. 삽입되면 삭제연산 완료
'''

def deQ():   # 개수만큼 반복해야 한다
    global last
    r = Q[1]  # 리턴값 (루트노드)
    Q[1] = Q[last]  # 마지막을 루트노드로 이동
    last -= 1  # 카운터 감소
    p = 1
    while p < last:   # 루트노드로 옮긴 것이 자식 노드보다 작아야 한다
        c1 = p * 2  # 왼쪽자식
        c2 = p * 2 + 1  # 오른쪽 자식
        if c2 <= last:  # 양쪽 자식이 다 있는 경우
            if Q[c1] < Q[c2]:  # 둘 중에 작은 쪽을 찾아야 한다
                c = c1
            else:
                c = c2
            if Q[c] < Q[p]:  # 둘 중 작은쪽과 부모를 비교
                Q[c], Q[p] = Q[p], Q[c]
                p = c
            else:
                break
        elif c1 <= last:  # 왼쪽자식만 있는 경우
            if Q[c1] < Q[p]:  # 둘 중 작은쪽과 부모를 비교
                Q[c1], Q[p] = Q[p], Q[c1]
                p = c1
            else:
                break
        else:
            break
    return r


def find():  # 마지막 노드의 조상 노드 찾기 == 마지막 노드의 부모/조상의 값 더하기
    global N
    c = N           # child
    p = c // 2      # parent
    s = 0           # start
    while p > 0:
        s += Q[p]  # 조상 노드 값을 더함
        print(s) # 5+2 = 7
        p = p // 2
    return s

T = int(input())
for tc in range(1, T + 1):
    # print('--------------')
    N = int(input())
    last = 0  # 노드가 하나도 없는 상태 -> 하나씩 채울때마다 +1이 된다.
    Q = [0 for i in range(N + 1)]  # 이진 힙 구현을 위한 리스트 생성
    l = list(map(int, input().split()))
    print(l)
    print(Q)
    for i in range(N):  # 힙에 저장 # 받은 원소 개수만큼의 원소를 돌면서 추가한다.
        enQ(l[i]) 
    # print(last)
    print('#{} {}'.format(tc, find()))
    print(Q)
    # 삭제하기
    # for i in range(N):  # 힙에 저장
    #     print(deQ(), end=" ")
    # print()
