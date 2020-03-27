# 5

import sys
sys.stdin = open('2468.txt', 'r')


N = int(input())

board = [ list(map(int, input().split())) for _ in range(N) ]

