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

tc = int(input())
for _ in range(tc):
    r = int(input())
    for _ in range(r):
        fo, ft = input().split()
        print(fo, ft)