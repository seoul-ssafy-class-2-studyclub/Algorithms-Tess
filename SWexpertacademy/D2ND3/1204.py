import sys
sys.stdin = open('1204.txt', 'r')


def max(dict):
    temp = 0

    temp_list = []
    temp2_list = []
    for key, value in cache.items():
        if temp < value:
            temp = value
            temp2 = key

    return temp2_list[-1]


for tc in range(int(input())):
    T = int(input())
    scores_list = list(map(int, input().split()))

    cache = {}
    for score in scores_list:
        cache[score] = scores_list.count(score)

    res = max(cache)
    print(f'#{T} {res}')







##

'''
for tc in range(int(input())):
    T = int(input())
    numbers = list(map(int, input().split()))
    dict_count = {}
    for i in range(len(numbers)):
        if not numbers[i] in dict_count:
            dict_count[numbers[i]] = 1
        else:
            dict_count[numbers[i]] += 1

    max_value = 0
    max_key = 0

    for key, value in dict_count.items():
        if value > max_value:
            max_value = value
            max_key = key
        elif value == max_value:
            if key > max_key:
                max_key = key

    print(f'#{tc+1} {max_key}')

'''