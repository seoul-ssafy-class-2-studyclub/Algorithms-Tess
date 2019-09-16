import sys
sys.stdin = open('5202.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    my_es = []
    for _ in range(N):
        s, e = map(int, input().split())
        my_es.append((e, s))

    my_es = list(sorted(my_es)) # 빨리 끝나는 순서대로 하기위해 종료시간을 앞으로 append
    # print(my_es)

    mycheck = [False]*N
    mycheck[0] = True

    res = []
    res.append(my_es[0])

    for idx in range(1, N):
        if my_es[idx][1] >= res[-1][0] and mycheck[idx] == False:
            mycheck[idx] = True
            res.append(my_es[idx])
    print(f'#{tc}', len(res))


# 조건은 두 가지
# 1. 가장 빨리 끝나야할 것
# 2. 다음 후보의 시작시간이 이미 저장된값의 종료시간과 충돌되지 않고, 크거나 같을것
