import sys
# sys.stdin = open('6603.txt', 'r')

input = sys.stdin.readline
def combi(k, s): # 깊이, 시작숫자
    if k == 6:
        print(' '.join(t))
        return
    else:
        for i in range(s, N):
            t[k] = data[i]
            combi(k+1, i+1)

# 조합생성시에는 visit가 없다.
flag = True
while flag:
    data = list(input().split())
    if data[0] != '0':
        N = len(data[1:])
        data = data[1:]
        t = [0] * 6
        combi(0, 0)
        print('')
    else:
        flag = False
        break


# import sys
# from itertools import combinations
#
# flag = True
# ans = []
# while flag:
#     line = list(input().split())
#     n = line[0]
#     if n == '0':
#         flag = False
#         break
#
#     for case in combinations(line[1:], 6):
#         print(' '.join(case))
#     print('')