import sys
sys.stdin = open('3019.txt', 'r')

C, P = map(int, input().split())
heights = list(map(int, input().split()))
'''
mytemp = heights[0] + 1
if it is 1 == (heights[0] - mytemp)
'''

print(C, P)
print(heights)
'''
1번 모양을 가로로 놓은것을 
0.0을 기준으로 놨을때,
바닥에서
[3,3,3,3,0]이 되어야 놓을 수 있는건데,
[2,1,1,1,0]인 바닥에 두면
[3, 2, 2, 2, 0] -> 0번 인덱스를 기준으로 일정하게 3이되지 않으므로 성립되는 경우가 아니다.
'''