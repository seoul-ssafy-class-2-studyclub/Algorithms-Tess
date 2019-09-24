import sys
# sys.stdin = open('17135.txt', 'r')
import collections
import itertools
input = sys.stdin.readline


'''
combinations는 궁수가 어디에 위치하고 있는지 모르기 때문에 모든 경우의 수를 구하기 위해 불러옴
각 경우의 수마다 시뮬레이션을 돌려야 하기 때문에 맵의 수정이 필요하므로 각 보드 딥카피
deque는 보드 턴마다 pop하고, appendleft하기 위해서 불러옴
Max는 공격할 수 있는 적이 여러 명일 때, 가장 왼쪽에 있는 적을 공격하기 위해만듦
'''

# 수정예정

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
# |r1-r2| + |c1-c2| <= d면 공격 가능
# d = 사정거리
# r1 c1을 궁수 위치
# r2 c2를 적 위치라고 하면
# |r1-r2| + |c1-c2| 요게 거리
'''
1. |r1-r2| + |c1-c2|가 가장 작은 적
2. 1번이 동일하다면 c2가 가장 작은 적(가장 왼쪽)
'''
# 거리에서 가장 가까운 애를 죽이는데, 적이 여럿인 경우 가장 왼쪽에 있는 적을 죽인다.
# - 오른쪽은 해당되는 대상이 아니다.
# - 해당 자리에 없으면 바로 왼쪽 -> 위쪽 -> 왼쪽+1 -> 위쪽 +1의 순서로 왔다갔다 한다.
# 각 턴에 3명의 궁수는 동시에 위 규칙에 따라 공격하고, 한 적을 동시에 공격할 수 있다.
# - 죽이고 바로 0을 하면 안된다. 죽일 적에 대한 좌표를 어딘가에 저장하고, 3명의 턴이 다 끝나면 그때 적을 0으로 만든다.
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


'''
from copy import deepcopy

def print_field_wall(field, wall, check, d, cnt):
    print("Distance: {}".format(d))
    for i in range(len(field)):
        print("{}\t{}".format(field[i], check[i]))
    print(wall)
    print("count: {}".format(cnt))
    print()

def shoot(field, wall, d, check):
    cnt = 0
    for w in range(len(wall)):
        if wall[w] == 2:  # 성벽에 사수가 있다면
            for dist in range(1, d + 1):  # 사격거리 1 ~ d 까지 조사
                cont1 = True  # 계속 조사 할 지 저장하는 변수
                for j in range(len(wall)):  # col 순으로 시작
                    cont2 = True  # 계속 조사 할 지 저장하는 변수
                    for i in range(len(field) - 1, -1, -1):  # row 역순. 성벽 가까이에서 성벽 멀리 조사
                        if abs(i - len(field)) + abs(j - w) == dist:  # 사거리에 들어올 때
                            if field[i][j] == 1 and check[i][j] == False:  # 적군이라면
                                field[i][j] = 0  # 사살하고 필드에서 없앰
                                check[i][j] = True  # 사살했다는 표시
                                cnt += 1
                                cont1 = False  # 3중 포문 탈출. 사수는 한번에 적군 한명만 사살가능
                                cont2 = False
                                break
                            elif field[i][j] == 0 and check[i][j] == True:  # 적이 이미 사살되어서 맵에서 제거됬다면
                                cont1 = False  # 3중포문 탈출
                                cont2 = False
                                break
                    if not cont2:
                        break
                if not cont1:
                    break
    return cnt

def solve(field, check, wall, d):
    global print_table
    fld = deepcopy(field)  # 깊은복사(deep copy)로 mutable 방지
    chk = deepcopy(check)  # 깊은복사(deep copy)로 mutable 방지
    count = 0
    if print_table:
        print("Init")
        print_field_wall(fld, wall, chk, d, count)

    while fld:  # fld가 0 이 되면, 즉 평지에 무엇도 남아있지 않을 경우 탈출
        count += shoot(fld, wall, d, chk)  # 발사
        if print_table:
            print("Shoot")
            print_field_wall(fld, wall, chk, d, count)
        fld.pop()  # 적군의 이동
        chk.pop()  # 적군의 이동
        chk = [[False] * len(fld[0]) for _ in range(len(fld))]  # shoot 전에 다시 초기화해줌
        if print_table:
            print("Move")
            print_field_wall(fld, wall, chk, d, count)

    return count


def main():
    global print_table
    n, m, d = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    check = [[False] * m for _ in range(n)]  # 앞의 사수에 의해 적군이 저격당했는지 확인

    result = 0  # 최종 정답(최댓값)

    # 성벽에 사수 배치. 사수가 3명이라 3중 포문
    wall = [0] * m
    for i in range(m):
        wall[i] = 2
        for j in range(i + 1, m):
            wall[j] = 2
            for k in range(j + 1, m):
                wall[k] = 2

                # 배치가 완료되면 적군 저격하는 시뮬레이션 실행(solve)
                total_count = solve(field, check, wall, d)
                if print_table:
                    print(f"***TOTAL COUNT: {total_count}***")
                    print()

                # 적군의 수를 비교하여 result에 할당
                result = max(total_count, result)

                wall[k] = 0
            wall[j] = 0
        wall[i] = 0

    print(result)  # 결과 출력


if __name__ == "__main__":
    print_table = False  # True 시 중간 결과물 출력, False 시 출력 안함
    main()

'''

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

