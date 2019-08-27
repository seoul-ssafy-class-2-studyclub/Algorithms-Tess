# 분할정복

import sys
sys.stdin = open('4880.txt', 'r')

'''
1
2
3
if A == 1 and B == 2:
    # 가위  바위
    B win
    A loose

if A == 1 and B == 3:
    A win
    B loose

if A == 1 and B == 1:
    check index
    index가 작은애가 win
'''


def checkwin(W1, W2):
    #print(W1, W2)
    if W1 > W2:
        W1, W2 = W2, W1

    if root[W1] == 3 and root[W2] == 1:
        # 가위  바위
        return W2

    elif root[W1] == 1 and root[W2] == 3:
        return W1

    elif root[W1] >= root[W2]:
        return W1

    else:
        return W2


def battle(s, e):

    if s == e:
        return s

    if abs(s - e) == 1:
        return checkwin(s, e)

    if abs(s - e) >= 2:
        p = (s+e)//2
        win1 = battle(s, p)
        win2 = battle(p+1, e)
        #print('nw', win1, win2)
        return checkwin(win1, win2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    root = list(map(int, input().split()))
    # 배틀이라는 함수에  0, N-1
    res = battle(0, N-1)
    print(f'#{tc} {res+1}')



