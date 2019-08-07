import sys
sys.stdin = open('4789.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    clap = list(map(int, input())) # [0, 9]
    statusL = len(clap)
    count = 0
    for i in range(statusL): #0, 1 #2
        if sum(clap[:i+1]) < i+1: # :1 -> 0 < 0+1 1
            # 0 < 1 작으니까. True
            clap[i] += 1
            count += 1
    print(f'#{tc} {count}')