import sys
# sys.stdin = open('17135.txt', 'r')
import collections
import itertools
input = sys.stdin.readline

def alivenum():
    alive = 0
    for y in range(len(land)-1, len(land)-D-1, -1): # 뒤에서부터보는데,
        for x in range(M):
            # print(y, x)
            if land[y][x] == 1:
                alive += 1
    return alive

N, M, D = map(int, input().split())
lands = collections.deque([list(map(int, input().split())) for _ in range(N)])

'''
죽이는 우선순위
1. D이하 에서 가장 가깝고,
2. 왼쪽에 있다.

턴이 하나 지나면, 칸이 점점 밀려나간다.
뒤 리스트를 pop처리해서 없애고 
앞에 appendleft [0]*M을 해주면 될듯? -> 그냥 land가 빌때 끝내면 됨
'''

shooter = list(range(M))
positions = list(itertools.combinations(shooter, 3))
mymax = -99999


for posi in positions:
    land = collections.deque([i[:] for i in lands])
    flag = 0
    dead = 0
    while flag != N:
        # 6이면, 6, 6-1-1, -1
        # 4까지면, (5, 4, -1) 그러면 5를 보는데,
        num = alivenum()
        shooting = 0
        for y in range(len(land)-1, len(land)-D-1, -1): # 뒤에서부터보는데,
            # 가장가까운애 위로 거리
            for ix in range(D): # 0일때,
                for dx in posi:
                    iy = y + ix
                    # print(y)
                    if 0 <= iy < N:
                        if land[iy][dx] == 1:
                            land[iy][dx] = 0
                            dead += 1
                            shooting += 1
                            num -= 1
                        if shooting == 3 or num == 0:
                            break
                if shooting == 3 or num == 0:
                    break
            if shooting == 3 or num == 0:
                break
            # 그리고 왼쪽
            for ix in range(D):
                for dx in posi:
                    x = ix + dx
                    if 0 <= x < M and 0 <= y < N:
                        if land[y][x] == 1:
                            land[y][x] = 0
                            dead += 1
                            shooting += 1
                            num -= 1
                        if shooting == 3 or num == 0:
                            break
                if shooting == 3 or num == 0:
                    break
            if shooting == 3 or num == 0:
                break
        land.pop()
        land.appendleft([0]*M)
        flag += 1
    if mymax < dead:
        mymax = dead
print(mymax)


#
# def alivenum():
#     alive = 0
#     for y in range(len(land)-1, len(land)-D-1, -1): # 뒤에서부터보는데,
#         for x in range(M):
#             # print(y, x)
#             if land[y][x] == 1:
#                 alive += 1
#     return alive
#
# N, M, D = map(int, input().split())
# lands = collections.deque([list(map(int, input().split())) for _ in range(N)])
#
# '''
# 죽이는 우선순위
# 1. D이하 에서 가장 가깝고,
# 2. 왼쪽에 있다.
#
# 턴이 하나 지나면, 칸이 점점 밀려나간다.
# 뒤 리스트를 pop처리해서 없애고
# 앞에 appendleft [0]*M을 해주면 될듯? -> 그냥 land가 빌때 끝내면 됨
# '''
#
# shooter = list(range(M))
# positions = list(itertools.combinations(shooter, 3))
# mymax = -99999
#
#
# for posi in positions:
#     land = collections.deque([i[:] for i in lands])
#     flag = 0
#     dead = 0
#     while flag != N:
#         # 6이면, 6, 6-1-1, -1
#         # 4까지면, (5, 4, -1) 그러면 5를 보는데,
#         num = alivenum()
#         shooting = 0
#         for y in range(len(land)-1, len(land)-D-1, -1): # 뒤에서부터보는데,
#             # 가장가까운애 위로 거리
#             for ix in range(D): # 0일때,
#                 for dx in posi:
#                     iy = y + ix
#                     # print(y)
#                     if 0 <= iy < N:
#                         if land[iy][dx] == 1:
#                             land[iy][dx] = 0
#                             dead += 1
#                             shooting += 1
#                             num -= 1
#                         if shooting == 3 or num == 0:
#                             break
#                 if shooting == 3 or num == 0:
#                     break
#             if shooting == 3 or num == 0:
#                 break
#             # 그리고 왼쪽
#             for ix in range(D):
#                 for dx in posi:
#                     x = ix + dx
#                     if 0 <= x < M and 0 <= y < N:
#                         if land[y][x] == 1:
#                             land[y][x] = 0
#                             dead += 1
#                             shooting += 1
#                             num -= 1
#                         if shooting == 3 or num == 0:
#                             break
#                 if shooting == 3 or num == 0:
#                     break
#             if shooting == 3 or num == 0:
#                 break
#         land.pop()
#         land.appendleft([0]*M)
#         flag += 1
#     if mymax < dead:
#         mymax = dead
# print(mymax)

