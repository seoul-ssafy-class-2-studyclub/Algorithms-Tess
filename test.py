from collections import deque

# deque 생성
thisisdeque = deque()
thisisdeque.append((1, 2))
thisisdeque.append((3, 2))
thisisdeque.append((5, 2))
thisisdeque.append((3, 7))
print(thisisdeque) # deque([(1, 2), (3, 2)])

mypop = thisisdeque.pop()
print(mypop) # (3, 7)

mypopleft = thisisdeque.popleft()
print(mypopleft) # (1, 2)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from itertools import product, combinations, permutations

mylist = [(1, 2), (2, 4), (6, 7)]

myproduct = list(product(mylist, repeat=4)) # 중복있는 조합
print(myproduct)

mycombinations = list(combinations(mylist, 2)) # 여러개중 몇 개의 중복없는 조합
print(mycombinations)

mypermutations = list(permutations(mylist, 3)) # 중복없는 조함
print(mypermutations)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# adj_list 생성

# 무방향 그래프
# 3
# 6 5
# 1 4
# 1 3
# 2 3
# 2 5
# 4 6
# 1 6
# 7 4
# 1 6
# 2 3
# 2 6
# 3 5
# 1 5
# 9 9
# 2 6
# 4 7
# 5 7
# 1 5
# 2 9
# 3 9
# 4 8
# 5 3
# 7 8
# 1 9
adj_list = [[] for i in range(length)]
for e in range(E):
    s, g = map(int, input().split())
    adj_list[s].append(g)
    adj_list[g].append(s)

# 방향 그래프
# 24 2
# 1 17 3 22 1 8 1 7 7 1 2 7 2 15 15 4 6 2 11 6 4 10 4 2
adj_list = [[] for i in range(length)]
for i in range(length):
    if i%2 == 0:
        adj_list[data[i]].append(data[i+1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# visit 생성
visited = [[False]*N for _ in range(N)]

''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 빠른 deepcopy
new = [i[:] for i in old]