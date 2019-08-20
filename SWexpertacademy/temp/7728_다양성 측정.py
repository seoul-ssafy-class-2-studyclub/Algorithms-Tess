'''
7728. 다양성 측정

'''


n = int(input())

for T in range(n):
    a = list(str(input()))
    a = list(set(a))
    number = len(a)
    print(f'#{T+1} {number}')