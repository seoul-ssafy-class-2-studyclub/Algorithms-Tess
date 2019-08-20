import sys
sys.stdin = open('1946.txt', 'r')



import math


##1

'''
for tc in range(int(input())):
    N = int(input())
    Ci_list = []
    Ki_list = []

    for n in range(N):
        D = list(map(str, input().split()))
        Ci_list.append(D[0])
        Ki_list.append(int(D[1]))

    temp = []
    for idx in range(N):
        temp += list(Ki_list[idx]*Ci_list[idx])

    total_num = sum(Ki_list)
    temp_round = math.ceil(total_num/10)
    print(f'#{tc+1}')
    for idx2 in range(temp_round):
        alive = temp[:10]
        print(f"{''.join(alive)}")
        del temp[:10]
    print(end='')
print()
'''

##2

for tc in range(int(input())):
    print(f'#{tc+1}')
    cnt = 0
    for N in range(int(input())):
        char, num = input().split()
        for i in range(int(num)):
            print(char, end='')
            cnt += 1
            if cnt == 10:
                cnt = 0
                print()
    print()