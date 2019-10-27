import sys
sys.stdin = open('16926.txt', 'r')

'''
입력
첫째 줄에 배열의 크기 N, M과 수행해야 하는 회전의 수 R이 주어진다.
둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.

출
입력으로 주어진 배열을 R번 회전시킨 결과를 출력한다.
'''


N, M, R = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(M) ]
print(board)
