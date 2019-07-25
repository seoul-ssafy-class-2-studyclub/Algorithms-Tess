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
a = []


'''


'''
#1.
Ip_data = list(map(int,input().split()))
    test_case = Ip_data[0]
    size = Ip_data[1]

#2. 
test_case, size = map(int,input().split())
'''


for i in range(int(input())):
    N = int(input())
    s = []
    o = 0
    print(f'#{i+1}')
    for j in range(N):
        x = []
        for k in range(N):
            x.append(0)
        s.append(x)
    a = list(range(1, N*N+1))
    c = N
    p = 0
    while(c>0):
        if o == 0 :
            for k in range(c):
                s[p][k+p] = a[0]
                a.pop(0)
            c -= 1
            o = 1
        elif o == 1 :
            for k in range(c):
                s[k+p+1][N-1-p] = a[0]
                a.pop(0)
            o = 2
        elif o == 2 :
            for k in range(c):
                s[N-1-p][N-2-k-p] = a[0]
                a.pop(0)
            c -= 1
            o = 3
        elif o == 3 :
            for k in range(c):
                s[N-2-p-k][p] = a[0]
                a.pop(0)
            p += 1
            o = 0
    for x in range(N) :
        for y in range(N):
            print(s[x][y], end=' ')
        print('')




