import sys
sys.stdin = open('5252.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    CNM = [input() for n in range(N)] + [input() for m in range(M)]
    total = len(CNM) - len(list(set(CNM)))
    print(f'#{tc} {total}')


'''
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    AN = []
    for n in range(N):
        AN.append(input())

    BM = []
    for m in range(M):
        BM.append(input())

    CNM = AN + BM
    total = len(CNM) - len(list(set(CNM)))
    print(f'#{tc} {total}')
'''