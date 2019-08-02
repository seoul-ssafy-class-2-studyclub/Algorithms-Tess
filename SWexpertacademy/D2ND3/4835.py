'''
T = 1
10 ≤ N ≤ 100
2 ≤ M ＜ N
1 ≤ aj ≤ 10000
'''
import sys
sys.stdin = open('4835.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    aj = list(map(int, input().split()))
    temp_sum_list = []
    sum_list = []

    cal_list = []
    #print(N, M, aj)

    for i in range(0, N-M+1):
        for i1 in range(0, M): #0~2
        # aj[i+1]을 기준으로 더한다.
            temp_sum_list.append(aj[i+i1])
            if i1 == M-1: # 2 2
                temp_sum = sum(temp_sum_list)
                sum_list.append(temp_sum)
                temp_sum_list = []
                continue
    #print(sum_list)

    max_temp = sum_list[0]
    for i2 in range(1, len(sum_list)):
        if max_temp < sum_list[i2]:
            max_temp = sum_list[i2]
    cal_list.append(max_temp)
    #print(cal_list)

    min_temp = sum_list[0]
    for i3 in range(1, len(sum_list)):
        if min_temp > sum_list[i3]:
            min_temp = sum_list[i3]
    cal_list.append(min_temp)
    #print(cal_list)

    #print(cal_list[0], cal_list[1])
    result = cal_list[0] - cal_list[1]
    #print(result)

    print('#{} {}'.format(tc, result))



