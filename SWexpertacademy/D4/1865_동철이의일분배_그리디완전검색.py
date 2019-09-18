import sys
sys.stdin = open('1865.txt', 'r')
import itertools
# 순열로 풀기
'''
# 메모리초과

T = int(input())

# 식 (0.13*0.7*1.0)*100 = 9.1%
for tc in range(1, T+1):
    Nums = int(input())
    candidates = [list(map(int, input().split())) for _ in range(Nums)]
    temp = [x for x in range(Nums)]
    my_candidates = list(itertools.permutations(temp, Nums))

    mymax = -9999999
    for i in range(len(my_candidates)):
        my_candidate = my_candidates[i]
        tempmax = 1
        for idx in range(len(my_candidate)):
            tempmax *= candidates[idx][my_candidate[idx]]
        if tempmax > mymax:
            mymax = tempmax

    print(f'#{tc}', '%.7f' % (mymax/1000000))
'''
#
# def my_permutation(pro=1, k=0):
#     global max_pro # 높은 값으로 갱신
#     if k == N: # k와 N이 같아지면 다음을 실행
#         if pro > max_pro: # max_pro 갱신
#             max_pro = pro
#             return True
#
#     for i in range(N):
#         if not vis[i]:
#             temp = pro * (pro_arr[k][i] / 100)
#             if temp != 0 and (not max_pro or temp > max_pro):
#                 vis[i] = True
#                 my_permutation(temp, k+1)
#                 vis[i] = False
#
# for case in range(1, int(input()) + 1):
#     N = int(input())
#     pro_arr = [list(map(int, input().split())) for _ in range(N)]
#     vis = [False] * N
#     print(vis)
#     max_pro = 0
#     res = my_permutation()
#     print(f'#{case} {max_pro * 100:.6f}')
#


def mpermut(pro=1, k=0):
    global mmax
    if k == N:
        if pro > mmax:
            mmax = pro
            return True
    for i in range(N): # 0-4
        if visited[i] == False:
            temp = pro * (board[k][i] / 100)
            if temp != 0 and (not mmax or temp > mmax):
                visited[i] = True
                mpermut(temp, k+1)
                visited[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N
    mmax = 0
    mpermut()
    print(f'#{tc} {mmax * 100:.6f}')