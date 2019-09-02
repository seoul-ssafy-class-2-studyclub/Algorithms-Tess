import sys
sys.stdin = open('6190.txt', 'r')


def shorten(n):
    a = n % 10
    n = int(n / 10)
    print(n)
    while n != 0:
        if n % 10 > a:
            return False
        else:
            a = n % 10
            n = int(n / 10)
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    origin = list(map(int, input().split()))
    resu = -1
    for i in range(N-1):
        for j in range(i+1, N):
            temp = origin[i] * origin[j]
            if resu >= temp:
                continue
            elif shorten(temp):
                resu = temp
    print(f'#{tc}', resu)

''' 코드 런타임에러
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    origin = list(map(int, input().split()))
    resu = -1
    for i in range(N-1):
        for j in range(i+1, N):
            temp = origin[i] * origin[j]
            temp_res = temp
            if temp < 10:
                continue
            else:
                temp_l = []
                for idx in range(len(str(temp))-1):
                    for idx2 in range(idx+1, len(str(temp))):
                        if int(str(temp)[idx]) <= int(str(temp)[idx2]):
                            temp_l += [True]
                        else:
                            temp_l += [False]
                            break
                if False not in temp_l:
                    if temp_res > resu:
                        resu = temp_res
    print(f'#{tc}', resu)
'''