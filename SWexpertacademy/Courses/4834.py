'''


0-9까지 적힌 타드
가장 많은 카드에 적힌 숫자와
카드가 몇장인지 출력하는 프로그램

카드 장수가 같을때는 적힘 숫자가 큰쪽 출력

'''


'''

T = int(input())
for t in range(1, T + 1):
    N = input()
    num_list = list(map(int, input()))
    answer = -1
    counter = 0

    for i in range(10):
        if num_list.count(i) >= counter:
            counter = num_list.count(i)
            answer = i

    print("#{} {} {}".format(t, answer, counter))

'''
# 카운팅 정렬로 풀기

'''
5
49679
'''

import sys
sys.stdin = open('4834.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    MAX_NUM = 10
    cards = int(input())
    A = list(map(int, input()))
    count = [0]*(MAX_NUM+1)
    for i in range(0, cards):
        count[A[i]] += 1

    num = count[0]
    for id in range(len(count)):
        if num <= count[id-1]: # 0, 1, 2, 3, 4,
            num = count[id-1]  # 2
            if num == count[id-1]:
                x = len(count[0: id-1])


    print('#{} {} {}'.format(t, x, num)) # 2가 나온다




'''

T = int(input())
for test_case in range(1, T + 1):
    trash = input()
    num_list = list(map(int, input()))

    answer = -1
    counter = 0

    for i in range(10):
        if num_list.count(i) >= counter:
            counter = num_list.count(i)
            answer = i

    print("#{} {} {}".format(test_case, answer, counter))

'''







'''
for T in range(int(input())):
    N = int(input())
    aj_list = list(map(int, input())) # split()을 하지않으면 쪼개져서 들어온다.

    # 중복되는 넘버 없이 카운트
    num_list = []
    temp_list = []
    for a in aj_list:
        if a not in temp_list:
            num_list.append(aj_list.count(a))
            temp_list.append(a)

    temp = num_list[0]
    for i in range(1, len(num_list)):
        if temp < num_list[i]:
            temp = num_list[i]
    print(temp) # 2

    max_index = num_list.index(temp)
    print(max_index)

    temp2 = aj_list[max_index]
    # 조건이 장수가 같으면 큰 수를 가져오는 거니까, 어느 수의 장수인지는 사실 상관없음.
    for i2 in range(1,len(aj_list)):
        if temp2 < aj_list[i2]:
            temp2 = aj_list[i2]

    print('#{} {} {}'.format(T+1, temp2, temp)) # 가장많은 카드 숫자와, 장수가 개별 아이템이더라도 결과만 나오면 된다.




'''
