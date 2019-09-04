'''
10
'''

import sys
import time
sys.stdin = open('15686.txt', 'r')

st = time.time()
print(st)

from itertools import combinations
def find_path(house_start, combis):
    hy, hx = house_start
    temp_list = []
    for c in combis:
        iy, ix = c
        paths_num = abs(hy - iy) + abs(hx- ix)
        temp_list.append(paths_num)
    return min(temp_list)
N, M = map(int, input().split())
mymap = [list(map(int, input().split())) for _ in range(N)]
temp_candidates = []
for y in range(N):
    for x in range(N):
        if mymap[y][x] == 2:
            temp_candidates.append((y, x))
chicken_combinations = list(combinations(temp_candidates, M))
houses = []
for y in range(N):
    for x in range(N):
        if mymap[y][x] == 1:
            houses.append((y, x))
final_min = []
for idx in range(len(chicken_combinations)):
    result_min_values = []
    for house in houses:
        res = find_path(house, chicken_combinations[idx])
        result_min_values.append(res)
    final_min.append(sum(result_min_values))
print(min(final_min))
