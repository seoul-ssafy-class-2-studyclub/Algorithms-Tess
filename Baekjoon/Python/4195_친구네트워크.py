'''
2
3
4
2
2
4
'''


import sys
sys.stdin = open('4195.txt', 'r')
# 유니온파인드!
# 들어오는 정보가 한번에 들어오는게 아니라서 arr을 처음에 해놓기가
# 어려웠음.

import sys
input = sys.stdin.readline

def find(x):
    if root[x] == x: # 내가 최상위 루트라면 자기자신을 부모로 가지고 있다
        return x # 자기 자신을 부모로서 출력한다.
    else:
        p = find(root[x]) # 그렇지 않은 경우 x의 최상위 루트를 찾아들어간다.
        root[x] = p # 찾은 부모를 root[x]의 부모라는 값으로 추가해준다.
        return root[x] # 그리고 그 부모를 출력한다.

def union(x, y):
    x = find(x) # 2. 각자의 부모를 먼저 찾는다.
    y = find(y)

    if x != y:
        root[y] = x # 부모가 다르다면, 부모로 추가해준다. x가 부모라는 조건 즉, y의 부모는 x다.
        rank[x] += rank[y]

ans = []
tc = int(input())
for _ in range(tc):
    root, rank = dict(), dict()
    # root는 각 자식마다 누가 부모인지 값으로 저장해 줄 것
    # rank는 부모 아래에 있는 자식의 수를 값으로 저장해줄 것
    r = int(input())

    for _ in range(r):
        fo, ft = input().split()
        if root.get(fo) == None:
            root[fo] = fo # 처음에는 자기자신을 루트로 갖는
            rank[fo] = 1 # 처음에는 자기와 연관된 자식이 한 명 인것을 알 수 있기때문에 1로 처리한다.

        if root.get(ft) == None:
            root[ft] = ft
            rank[ft] = 1

        union(fo, ft) # 1. 엮어주기

        # 빠르게 출력하기 위한 것
        ans += [rank[find(fo)]] # 가장 최상위 부모에 있는 값이 답이된다.
print('\n'.join(map(str,ans)))






# 시간초과 10%
# 다른 로직 생각
# import sys
# input = sys.stdin.readline
#
# tc = int(input())
# def solve(ch):
#     global cnt
#     if vis[info_dict[ch]] == False:
#         vis[info_dict[ch]] = True
#         if ch not in connect_dict[ft] and ch != ft:
#             connect_dict[ft].append(ch)  # 자기 자신은 append 되지 않도록 해야한다.
#             if ft not in connect_dict[ch]:
#                 connect_dict[ch].append(ft)
#         if ch not in connect_dict[fo] and ch != fo:
#             connect_dict[fo].append(ch)
#             if fo not in connect_dict[ch]:
#                 connect_dict[ch].append(fo)
#         for chi in connect_dict[ch]:
#             solve(chi)
#
# ans = []
# for _ in range(tc):
#
#     r = int(input())
#     info_dict = dict()
#     # dictionary로 저장해야한다.
#     connect_dict = dict()
#     i = 0
#     for _ in range(r):
#         fo, ft = input().split()
#         if info_dict.get(fo) == None:
#             info_dict[fo] = i
#             connect_dict[fo] = []
#             connect_dict[fo].append(ft)
#             i += 1
#         if info_dict.get(ft) == None:
#             info_dict[ft] = i
#             connect_dict[ft] = []
#             connect_dict[ft].append(fo)
#             i += 1
#         else:
#             connect_dict[fo].append(ft)
#             connect_dict[ft].append(fo)
#
#         # 넘어가면 친구로 넣어줘야지.
#         # CC로 풀어도 될 거 같고
#         for c in connect_dict[fo]:
#             vis = [False]*i
#             solve(c)
#         answer = len(connect_dict[fo]) + 1
#         ans.append(answer)
# print('\n'.join(map(str,ans)))



