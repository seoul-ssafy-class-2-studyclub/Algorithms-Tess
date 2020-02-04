# -*- coding: utf-8 -*-
import sys
import itertools
sys.stdin = open('17135.txt', 'r')
input = sys.stdin.readline

N, M, D = map(int, input().split())
myMap = [list(map(int, input().split())) for i in range(N)]
myMaxKill = -1

def down(solveMap):
    solveMap = [i[:] for i in solveMap]
    d = solveMap.pop(N-1)
    solveMap = [[0]*M] + solveMap
    alive = 0
    for y in range(N):
        for x in range(M):
            if solveMap[y][x]:
                alive += 1
    return solveMap, alive

def check(solveMap, final):
    solveMap = [i[:] for i in solveMap]
    if len(final) and final != []:
        for x, y in final:
            solveMap[y][x] = 0
    return solveMap

def solve(shooter, solveMap, solveEnemies, kills):
    alive = solveEnemies
    while alive:
        finalKill = set()
        s1, s2, s3 = shooter
        findKill1 = []
        findKill2 = []
        findKill3 = []
        
        for y in range(N-1, -1, -1):
            for x in range(M-1, -1, -1):
                if solveMap[y][x]:
                    d1 = abs(N-y) + abs(s1-x)
                    if D >= d1:
                        findKill1 += [(d1, x, y)]
                    d2 = abs(N-y) + abs(s2-x)
                    if D >= d2:
                        findKill2 += [(d2, x, y)]
                    d3 = abs(N-y) + abs(s3-x)
                    if D >= d3:
                        findKill3 += [(d3, x, y)]
        findKill1.sort()
        findKill2.sort()
        findKill3.sort()
        # 좌표는 같아도 거리가 다를 수 있으므로 거리를 제외한 좌표만 슬라이싱해서 넣는다.
        if len(findKill1) and findKill1[0][1:] not in finalKill:
            finalKill.add(findKill1[0][1:])
        if len(findKill2) and findKill2[0][1:] not in finalKill:
            finalKill.add(findKill2[0][1:])
        if len(findKill3) and findKill3[0][1:] not in finalKill:
            finalKill.add(findKill3[0][1:])

        kills += len(finalKill)
        solveMap = check(solveMap, finalKill)
        solveMap, alive = down(solveMap)
        if alive == 0:
            break
    return kills

enemies = 0
enemiesyx = []
for y in range(N):
    for x in range(M):
        if myMap[y][x]:
            enemies += 1
candiIdx = [i for i in range(0, M)]
shooters = list(itertools.combinations(candiIdx, 3))
for shooter in shooters:
    pin = N
    solveEnemies = enemies
    solveMap = [i[:] for i in myMap]
    mymax = solve(shooter, solveMap, solveEnemies, 0)
    if myMaxKill < mymax:
        myMaxKill = mymax
print(myMaxKill)


# 행의 수 N==Y, 열의 수 M==X, 궁수의 공격 거리 제한 D
# 1이 써진 곳이 적이 존재하는 곳
# n+1번 행, 맨 밑에 성이 존재
# 제거할 수 있는 적의 최대 수를 출력

# 3개의 위치를 고른다.
# 적의 수를 센다
# 죽인다
# max값을 갱신

# 궁수의 위치를 바꿔서 돌린다.
# shooter로 공격
# 거리가 D이하인 적 중에서 가장 가까운 적
# 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격 (적이 몇개인지 먼저 검증 후 가장 왼쪽 공격)
# 같은 적이 여러 궁수에게 공격당할 수 있다
# 공격받은 적은 게임에서 제외 => 바로 0으로 지우지 않는다.
# 남겨두고
# 맨 마지막에 지워준다.
# 턴이 하나 끝나면 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동
# N에 오면 성이 있는 칸으로 이동한 경우에는 게임에서 제외
# 모든 적이 격자판에서 제외되면 게임이 끝난다.
# 격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|
# 거리가 3이면 가장 가까운 애를 쏜다
# 3이랑 2가 있으면 2를 무조건 쏘고, 여럿인 경우 가장 왼쪽을 쏜다.
# 왼쪽이란 x가 가장 작은 경우일 것 sort를 사용한다. (거리, x) 순으로 저장해서 본다.
# D 이내 면서 가장 가까운 적
