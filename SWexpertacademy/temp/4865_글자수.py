import sys
sys.stdin = open('4865.txt', 'r')

#############문자열 수세기
# str1에 들어있는 각각의 원소가
# str2에 몇개 들어있는지 찾고,
# 찾은 개수중에 가장많은 수를 출력

T = int(input())

for tc in range(1, T+1):
    str1 = list(set(input()))
    #print(str1)

    str2 = input()

    char_count_dict = {}

    for char1 in str1:
        if char1 in str2:
            char_count_dict[char1] = 0
    #print(char_count_dict)

    for char2 in str2:
        if char2 in str1:
            char_count_dict[char2] += 1
    #print(char_count_dict)

    temp = 0
    for value in char_count_dict.values():
        if value > temp:
            temp = value
    print(f'#{tc} {temp}')