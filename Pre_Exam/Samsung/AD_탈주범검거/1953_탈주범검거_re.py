import sys
sys.stdin = open('1953.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
