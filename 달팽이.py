'''
T = 2

N = 3

N = 4

'''

# 다차원 리스트 선언 방법
board = []
n, k = list(map(int, '3' '4'))
print(n)
print(k)

for o in range(n):
    board.append(list('1 3 3 6 7'.split()))

print(board * k)
print(board[0][0])

방향을
지정한다
1
순차적으로
더하기
2
열이
바뀌면서
더하기
3
순차적으로
빼기
4
올라가면서
처음
열을
빼고
더하기

'''
#1.
Ip_data = list(map(int,input().split()))
    test_case = Ip_data[0]
    size = Ip_data[1]

#2. 
test_case, size = map(int,input().split())
'''