import sys
# from pprint import pprint
# sys.stdin = open('15683.txt', 'r')



input = sys.stdin.readline
def counting():
    global nboard, mymin
    cnt = 0
    for y in range(N):
        for x in range(M):
            if nboard[y][x] == '0':
                cnt += 1
                if cnt > mymin:
                    return
    if cnt < mymin:
        mymin = cnt


def coloring(dy, iy, dx, ix):
    global nboard
    if 0 <= iy+dy < N and 0 <= ix+dx < M:
        if nboard[iy+dy][ix+dx] == '0':
            nboard[iy + dy][ix + dx] = '#'
            coloring(dy, iy+dy, dx, ix+dx)
        elif nboard[iy+dy][ix+dx] != '0' and nboard[iy+dy][ix+dx] != '6':
            # 다른 카메라가 있을 경우 그 카메라를 건너뛴 상태로 '#'처리를 해야한다.
            coloring(dy, iy + dy, dx, ix + dx)
        else:
            return
    else:
        return

def solve(status):
    global nboard
    for i in range(len(CCTV_number)):
        mystatus = status[i]
        yx = CCTV_yx[i]
        y = yx[0]
        x = yx[1]

        if CCTV_number[i] == '1':
            iyx = CCTV1[mystatus]
            dy, dx = iyx[0],iyx[1]
            coloring(dy, y, dx,  x)
        elif CCTV_number[i] == '2':
            for iyx in CCTV2[mystatus]:
                dy, dx = iyx[0], iyx[1]
                coloring(dy, y, dx,  x)
        elif CCTV_number[i] == '3':
            for iyx in CCTV3[mystatus]:
                dy, dx = iyx[0], iyx[1]
                coloring(dy, y, dx,  x)
        elif CCTV_number[i] == '4':
            for iyx in CCTV4[mystatus]:
                dy, dx = iyx[0], iyx[1]
                coloring(dy, y, dx,  x)
        elif CCTV_number[i] == '5':
            for iyx in CCTV5[mystatus]:
                dy, dx = iyx[0], iyx[1]
                coloring(dy, y, dx,  x)
    return


N, M = map(int, input().split())
board = [ list(map(str, input().split())) for _ in range(N) ]

# 맵에 어떤 감시카메라가 있는지 확인 필요,
CCTV_yx = []
CCTV_number = []
for y in range(N):
    for x in range(M):
        if board[y][x] != '6' and board[y][x] != '0': # 6:벽도 아니고, 0:빈칸도 아닌 것
            CCTV_yx.append((y, x))
            CCTV_number.append(board[y][x])
numofCCTV = len(CCTV_number)

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# 그리고 해당 감시 카메라의 status가 바뀔때 어떤식으로 바뀌는지 확인필요

CCTV1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
CCTV1_status = [0, 1, 2, 3]

CCTV2 = [((0, 1), (0, -1)),
         ((1, 0), (-1, 0))]
CCTV2_status = [0, 1]

CCTV3 = [((0, 1), (-1, 0)),
         ((0, -1), (1, 0)),
         ((0, -1), (-1, 0)),
         ((0, 1), (1, 0))]
CCTV3_status = [0, 1, 2, 3]

CCTV4 = [((0, 1), (0, -1), (1, 0)),
         ((0, -1), (1, 0), (-1, 0)),
         ((0, 1), (0, -1), (-1, 0)),
        ((1, 0), (-1, 0), (0, 1))
         ]
CCTV4_status = [0, 1, 2, 3]

CCTV5 = [((0, 1), (0, -1), (1, 0), (-1, 0))]
CCTV5_status = [0]

# CCTV 만큼 불러올 중복 순열 필요
# 맵에서 status에 맞게 # 처리 후 0을 세서 최소 사각지대 값을 결과값으로 출력

mydict = {'1': CCTV1_status, '2': CCTV2_status, '3': CCTV3_status, '4': CCTV4_status, '5':CCTV5_status}

# 중복조합
avaliable = []
for i in CCTV_number:
    avaliable.append(mydict.get(i))

def combinations(i, mylist):
    global candidates
    if i == len(avaliable):
        candidates.append(mylist)
        return mylist

    for j in range(len(avaliable[i])): #
        combinations(i+1, mylist+[avaliable[i][j]])

candidates = []
combinations(0, [])

mymin = 99999
for candidate in candidates:
    nboard = [i[:] for i in board]
    solve(candidate)
    counting()
print(mymin)



#
# input = sys.stdin.readline
# def counting():
#     global nboard, mymin
#     cnt = 0
#     for y in range(N):
#         for x in range(M):
#             if nboard[y][x] == '0':
#                 cnt += 1
#                 if cnt > mymin:
#                     return
#     if cnt < mymin:
#         mymin = cnt
#
#
# def coloring(dy, iy, dx, ix):
#     global nboard
#     if 0 <= iy+dy < N and 0 <= ix+dx < M:
#         if nboard[iy+dy][ix+dx] == '0':
#             nboard[iy + dy][ix + dx] = '#'
#             coloring(dy, iy+dy, dx, ix+dx)
#         elif nboard[iy+dy][ix+dx] != '0' and nboard[iy+dy][ix+dx] != '6':
#             # 다른 카메라가 있을 경우 그 카메라를 건너뛴 상태로 '#'처리를 해야한다.
#             coloring(dy, iy + dy, dx, ix + dx)
#         else:
#             return
#     else:
#         return
#
# def solve(status):
#     global nboard
#     for i in range(len(CCTV_number)):
#         mystatus = status[i]
#         yx = CCTV_yx[i]
#         y = yx[0]
#         x = yx[1]
#
#         if CCTV_number[i] == '1':
#             iyx = CCTV1[mystatus]
#             dy, dx = iyx[0],iyx[1]
#             coloring(dy, y, dx,  x)
#         elif CCTV_number[i] == '2':
#             for iyx in CCTV2[mystatus]:
#                 dy, dx = iyx[0], iyx[1]
#                 coloring(dy, y, dx,  x)
#         elif CCTV_number[i] == '3':
#             for iyx in CCTV3[mystatus]:
#                 dy, dx = iyx[0], iyx[1]
#                 coloring(dy, y, dx,  x)
#         elif CCTV_number[i] == '4':
#             for iyx in CCTV4[mystatus]:
#                 dy, dx = iyx[0], iyx[1]
#                 coloring(dy, y, dx,  x)
#         elif CCTV_number[i] == '5':
#             for iyx in CCTV5[mystatus]:
#                 dy, dx = iyx[0], iyx[1]
#                 coloring(dy, y, dx,  x)
#     return
#
#
# N, M = map(int, input().split())
# board = [ list(map(str, input().split())) for _ in range(N) ]
#
# # 맵에 어떤 감시카메라가 있는지 확인 필요,
# CCTV_yx = []
# CCTV_number = []
# for y in range(N):
#     for x in range(M):
#         if board[y][x] != '6' and board[y][x] != '0': # 6:벽도 아니고, 0:빈칸도 아닌 것
#             CCTV_yx.append((y, x))
#             CCTV_number.append(board[y][x])
# numofCCTV = len(CCTV_number)
#
# delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# # 그리고 해당 감시 카메라의 status가 바뀔때 어떤식으로 바뀌는지 확인필요
#
# CCTV1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# CCTV1_status = [0, 1, 2, 3]
#
# CCTV2 = [((0, 1), (0, -1)),
#          ((1, 0), (-1, 0))]
# CCTV2_status = [0, 1]
#
# CCTV3 = [((0, 1), (-1, 0)),
#          ((0, -1), (1, 0)),
#          ((0, -1), (-1, 0)),
#          ((0, 1), (1, 0))]
# CCTV3_status = [0, 1, 2, 3]
#
# CCTV4 = [((0, 1), (0, -1), (1, 0)),
#          ((0, -1), (1, 0), (-1, 0)),
#          ((0, 1), (0, -1), (-1, 0)),
#         ((1, 0), (-1, 0), (0, 1))
#          ]
# CCTV4_status = [0, 1, 2, 3]
#
# CCTV5 = [((0, 1), (0, -1), (1, 0), (-1, 0))]
# CCTV5_status = [0]
#
# # CCTV 만큼 불러올 중복 순열 필요
# # 맵에서 status에 맞게 # 처리 후 0을 세서 최소 사각지대 값을 결과값으로 출력
#
# mydict = {'1': CCTV1_status, '2': CCTV2_status, '3': CCTV3_status, '4': CCTV4_status, '5':CCTV5_status}
#
# # 중복조합
# avaliable = []
# for i in CCTV_number:
#     avaliable.append(mydict.get(i))
#
# def combinations(i, mylist):
#     global candidates
#     if i == len(avaliable):
#         candidates.append(mylist)
#         return mylist
#
#     for j in range(len(avaliable[i])):
#         combinations(i+1, mylist+[avaliable[i][j]])
#
# candidates = []
# combinations(0, [])
#
# mymin = 99999
# for candidate in candidates:
#     nboard = [i[:] for i in board]
#     solve(candidate)
#     counting()
# print(mymin)
