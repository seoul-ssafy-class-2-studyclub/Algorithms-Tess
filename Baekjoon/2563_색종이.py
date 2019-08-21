'''
https://www.acmicpc.net/problem/2563

3
3 7
15 7
5 2

260
'''

import sys
sys.stdin = open('2563.txt', 'r')


# N = 100
# M = 100
#
# mat = [[0]*M for _ in range(N)] # N*M의 mat
# #print(mat)
#
# T = int(input())
# papers = []
# for tc in range(1, T+1):
#     A, B = map(int, input().split()) # 3, 7
#
#     # 처리
#     #
#     for iy in range(10):
#         for ix in range(10):
#             mat[B+iy][A+ix] = 1
# cnt = 0
# for item in mat:
#     cnt += sum(item)
# print(cnt)

mat = [[0]*100 for _ in range(100)]
for _ in range(int(input())):
    x, y = map(int, input().split())

## 이부분 핸들링 재확인!
    for iy in range(y, y+10):
        for ix in range(x, x+10):
            mat[iy][ix] = 1
cnt = 0
for item in mat:
    for i in range(len(mat)):
        if item[i] == 1:
            cnt += 1
print(cnt)



































