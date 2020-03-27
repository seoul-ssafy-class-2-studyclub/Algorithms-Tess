import sys
sys.stdin = open('input.txt', 'r')

'''
10 8
3
0 3
1 4
0 2
'''
'''
30
'''


x, y = map(int, input().split())
cut_N = int(input())

xi = []
yi = []
for _ in range(cut_N):
    command, cut = map(int, input().split())
    if command == 0:
        xi.append(cut)
    if command == 1:
        yi.append(cut)
print(xi, yi)

tempx = []
tempy = []
