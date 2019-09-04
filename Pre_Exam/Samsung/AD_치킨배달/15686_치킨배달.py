'''
10
'''

import sys
# import random
# import time
from itertools import combinations
from pprint import pprint
sys.stdin = open('15686.txt', 'r')

# st = time.time()
# res = time.time() - st
# print(res)
'''
BFS를 써야하는건가? 라는 생각이 들 수 있지만, 그냥 조합을 구해서 값을 도출하면 되는 심플한 문제다.
집과 집을 통과할 수 있으니까 말이다.
문제를 잘 읽고 푸는게 가장 중요하다.
'''

def find_path(house_start, combis):
    hy, hx = house_start
    temp_list = []
    for c in combis:
        iy, ix = c
        paths_num = abs(hy - iy) + abs(hx- ix) # 1이 접근할 수 있는 모든 2의 좌표 계산하고, 리스트에 추가
        temp_list.append(paths_num)
    return min(temp_list)

N, M = map(int, input().split())
mymap = [list(map(int, input().split())) for _ in range(N)]

# (2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2
# 1. 모든 2의 좌표를 구한다.
temp_candidates = []
for y in range(N):
    for x in range(N):
        if mymap[y][x] == 2:
            temp_candidates.append((y, x))
# 2. 구한 좌표에서 M만큼 해당하는 중복 조합을 고른다.
chicken_combinations = list(combinations(temp_candidates, M))
# 2-1. 변하지 않는 1들의 좌표를 모두 구한다.
houses = []
for y in range(N):
    for x in range(N):
        if mymap[y][x] == 1:
            houses.append((y, x))
# main 시작
final_min = []
for idx in range(len(chicken_combinations)):
    result_min_values = []
    for house in houses:
        res = find_path(house, chicken_combinations[idx])
        result_min_values.append(res)
    final_min.append(sum(result_min_values))
    # 7. 산출한 최종값들을 저장하는 리스트를 추가하고
print(min(final_min))
# 8. 그 리스트의 합들을 더한다.
