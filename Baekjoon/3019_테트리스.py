import sys
sys.stdin = open('3019.txt', 'r')

C, P = map(int, input().split())
heights = list(map(int, input().split()))

print(C, P)
print(heights)