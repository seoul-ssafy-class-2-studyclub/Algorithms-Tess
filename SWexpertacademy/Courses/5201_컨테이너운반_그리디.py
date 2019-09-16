import sys
sys.stdin = open('5201.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    Nweights = list(map(int, input().split()))
    Nweights = list(sorted(Nweights, reverse=True))
    Mcapas = list(map(int, input().split()))
    Mcapas = list(sorted(Mcapas, reverse=True))
    Ncheck = [False]*N
    Mcheck = [False]*M

    for idx in range(M):
        for jdx in range(N):
            if Mcapas[idx] >= Nweights[jdx] and Mcheck[idx] == False and Ncheck[jdx] == False:
                Ncheck[jdx] = True
                Mcheck[idx] = True
                break

    res = 0
    for jdx in range(N):
        if Ncheck[jdx] == True:

            res += Nweights[jdx]

    print(f'#{tc}', res)

