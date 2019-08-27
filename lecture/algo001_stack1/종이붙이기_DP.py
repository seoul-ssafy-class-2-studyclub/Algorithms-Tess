'''
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

#1 5
#2 21
#3 85

'''

import sys
sys.stdin = open('DP.txt', 'r')

def paper(width):
    if width == N: #목표너비가 되면, 경우 1 반환
        return 1

    if width > N: #목표너비보다 크면,
        return 0
            # 0+10 + (0+20)*2
    return paper(width + 10) + paper(width + 20)*2


T = int(input())
for tc in range(1, T+1):
    N = int(input()) #목표너비
    R = paper(0) #너비를 함수에 추가
    print(f'{tc} {R}')



