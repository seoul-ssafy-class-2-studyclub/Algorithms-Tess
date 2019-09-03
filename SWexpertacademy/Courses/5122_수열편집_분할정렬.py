import sys
sys.stdin = open('5122.txt', 'r')
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    mylist = list(map(int, input().split()))

    for _ in range(M):
        myadd = list(map(str, input().split()))

        if myadd[0] == 'D':
            mylist.pop(int(myadd[1]))

        elif myadd[0] == 'I':
            ## -1을하면 1뒤부터 밀어진다.
            mylist.insert(int(myadd[1]), myadd[2])

        elif myadd[0] == 'C':
            mylist[int(myadd[1])] = myadd[2]

    if L >= len(mylist):
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', int(mylist[L]))
