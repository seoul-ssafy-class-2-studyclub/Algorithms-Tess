import sys
sys.stdin = open('1868.txt', 'r')

from pprint import pprint

'''
3
..*  02*
..*  24*
**.  **2

#1 2
'''

'''
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
'''

#* 이 있는 여덟 방향에 대해서 숫자를 더해준다.

for tc in range(int(input())):
    bigboard = []
    checkboard = [0]
    bigcheckboard = []
    N = int(input())
    for bi in range(N):
        bigboard.append(list(input()))
        bigcheckboard.append(list(checkboard*N))
    # 체크될 보드

    for bbi in range(N*2):  # bigboard의 인덱스
        for id in range(3): # 0 1 2
            id = bbi + id
            for ix in range(3): # 0 1 2
                ix = bbi + id
                try:
                    if bigboard[id][ix] == '*': # 0,0 0,1 0,2 # 1,0 1,1 1,2 이렇게 돌면서 찾아간다.
                        bigcheckboard[id][ix-1] = '1' # 0,0
                        bigcheckboard[id][ix + 1] = '1'  # 0,1
                        bigcheckboard[id - 1][ix + 1] = '1'  # 0,2
                        bigcheckboard[id + 1][ix - 1] = '1'  # 2,0
                        bigcheckboard[id + 1][ix] = '1'  # 2,1
                        bigcheckboard[id+1][ix+1] = '1' # 2,2
                        bigcheckboard[id-1][ix-1] = '1'  # 1,0
                        bigcheckboard[id + 1][ix + 1] = '1'  # 1,0
                        bigcheckboard[id-1][ix] = '1'
                    else:
                        bigcheckboard[id][ix] = 'x'
                except:
                    continue

    pprint(bigcheckboard)