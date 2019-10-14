import sys
# sys.stdin = open('17143.txt', 'r')
# from pprint import pprint
input = sys.stdin.readline

def catchShark(currentstep):
    global ocean, catched
    # 준비되어있는 보드에서 가장 가까운 상어를 사라지게 한다.
    for y in range(R):
        if ocean[y][currentstep] != False:
            catched.append(ocean[y][currentstep][0])
            ocean[y][currentstep] = False
            return
    return

def moveShark(idx_s, w, speed, di):
    while True:
        idx_s += speed
        if 0 <= idx_s <= w:
            return idx_s, di
        if idx_s >= w:
            speed = w - idx_s
            idx_s = w
            if di == 2:
                di = 1
            elif di == 3:
                di = 4
        if idx_s <= 0:
            speed = abs(idx_s)
            idx_s = 0
            if di == 1:
                di = 2
            elif di == 4:
                di = 3

def findsurvivor(updat):
    global ocean

    while updat:
        info = updat.pop()
        if ocean[info[3]][info[4]] == False:
            ocean[info[3]][info[4]] = info
        else:
            if ocean[info[3]][info[4]][0] < info[0]:
                # print(ocean[info[3]][info[4]])
                ocean[info[3]][info[4]] = info
                # print(info)
    return

# 1: up, 2: down, 3: right, 4: left
R, C, M = map(int, input().split()) # 4, 6, 8
# R은 y 4, C가 x 6
# 0은 낚시꾼의 위치
ocean = [[False]*C for _ in range(R)]
'''
낚시왕이 잡은 상어의 크기의 합: 22
(r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
d가 
1인 경우는 위, 
2인 경우는 아래, 
3인 경우는 오른쪽, 
4인 경우는 왼쪽을 의미
'''
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    # 1, 4가는 애는 -로 속력을 받는다.
    r = r-1
    c = c-1
    if d == 1 or d == 4:
        ocean[r][c] = [z, -s, d, r, c]
    else:
        ocean[r][c] = [z, s, d, r, c]

catched = []
for step in range(C):

    catchShark(step)

    temp = []
    for r in range(R):
        for c in range(C):
            if ocean[r][c] != False:
                temp.append(ocean[r][c])
                ocean[r][c] = False

    update = []
    while temp:
        info = temp.pop()

        if info[2] == 1 or info[2] == 2:
            newy, newdi = moveShark(info[3], R-1, info[1], info[2])
            info[3] = newy
            info[2] = newdi
            if newdi == 2:
                info[1] = abs(info[1])
            if newdi == 1:
                info[1] = -(abs(info[1]))
            update.append(info)

        elif info[2] == 3 or info[2] == 4:
            newx, newdi = moveShark(info[4], C-1, info[1], info[2])
            info[4] = newx
            info[2] = newdi
            if newdi == 3:
                info[1] = abs(info[1])
            if newdi == 4:
                info[1] = -(abs(info[1]))
            update.append(info)

    findsurvivor(update)

print(sum(catched))





# import sys
# sys.stdin = open('17143.txt', 'r')
# from pprint import pprint
#
#
#
#
# '''
# 낚시왕이 가장 오른쪽에 도착할때까지 다음과 같은 규칙을 반복한다.
# 1. 낚시왕은 오른쪽으로 한칸씩 이동한다.
#
# catchShark();
# 2. 가까운 상어를 잡은 후 잡은 상어는 사라진다.
#
# moveShark();
# 3. 초마다 속력만큼 이동한다. (s, d)
# 상어는 이동하면서 벽에 부딪히면, 반대 방향으로 다시 이동한다.
#
# findsurvivor();
# 4. 같은 공간에 두 상어 이상이 존재하면, 크기가 큰 상어만 살아남는다.
# 둘 이상 존재하는 곳을 찾아 하나만 상어만 존재하게 해야한다.
#
# 상어를 잡고(catchShark),
# 상어가 이동하고(moveShark),
# 상어끼리 잡아먹는 일(findsurvivor)이 발생하는 것이 반복
# '''
#
#
# def catchShark(currentstep):
#     global ocean, catched
#     # 준비되어있는 보드에서 가장 가까운 상어를 사라지게 한다.
#     for y in range(1, R+1):
#         if ocean[y][currentstep] != False:
#             catched.append(ocean[y][currentstep][0])
#             ocean[y][currentstep] = False
#             return
#     return
#
#
# def moveShark(idx_s, w, speed, di):
#     while True:
#         idx_s += speed
#         if 1 <= idx_s <= w:
#             return idx_s, di
#         if idx_s >= w:
#             speed = w - idx_s
#             idx_s = w
#             if di == 2:
#                 di = 1
#             elif di == 3:
#                 di = 4
#         if idx_s <= 1:
#             speed = abs(idx_s)
#             idx_s = 1
#             if di == 1:
#                 di = 2
#             elif di == 4:
#                 di = 3
#
#
# def findsurvivor(updat):
#     global ocean
#
#     while updat:
#         info = updat.pop()
#         if ocean[info[3]][info[4]] == False:
#             ocean[info[3]][info[4]] = info
#         else:
#             if ocean[info[3]][info[4]][0] < info[0]:
#                 ocean[info[3]][info[4]] = info
#
# # 1: up, 2: down, 3: right, 4: left
# R, C, M = map(int, input().split()) # 4, 6, 8
# # R은 y 4, C가 x 6
#
# # 0은 낚시꾼의 위치
# ocean = [[False]*(C+1) for _ in range(R+1)]
# '''
# 낚시왕이 잡은 상어의 크기의 합: 22
# (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
# d가
# 1인 경우는 위,
# 2인 경우는 아래,
# 3인 경우는 오른쪽,
# 4인 경우는 왼쪽을 의미
# '''
# for i in range(1, M+1):
#     r, c, s, d, z = map(int, input().split())
#     # 1, 4가는 애는 -로 속력을 받는다.
#     if d == 1 or d == 4:
#         ocean[r][c] = [z, -s, d, r, c]
#     else:
#         ocean[r][c] = [z, s, d, r, c]
#
# catched = []
# for step in range(1, C+1):
#
#     catchShark(step)
#
#     temp = []
#     for r in range(1, R+1):
#         for c in range(1, C+1):
#             if ocean[r][c] != False:
#                 temp.append(ocean[r][c])
#                 ocean[r][c] = False
#
#     update = []
#
#     while temp:
#         info = temp.pop()
#
#         if info[2] == 1 or info[2] == 2:
#             newy, newdi = moveShark(info[3], R, info[1], info[2])
#             info[3] = newy
#             info[2] = newdi
#             update.append(info)
#         else:
#             newx, newdi = moveShark(info[4], C, info[1], info[2])
#             info[4] = newx
#             info[2] = newdi
#
#             update.append(info)
#
#     findsurvivor(update)
#
# print('잡음', sum(catched), catched)
#
#
