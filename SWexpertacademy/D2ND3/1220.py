import sys
sys.stdin = open('1220.txt', 'r')


def columnCounting(arr):
    checked_list = []
    for column in result_bigboard:
        new_string = ''.join(column)
        checked_list.append(new_string.replace('0', '')) # replace 한건 항상 변수에 저장해줘야 한다.
    count_list = []
    for new_string in checked_list:
        count = 0
        while True:

            pattern = '12'
            wall = new_string.find(pattern)
            if wall == -1:
                count_list.append(count)
                break
            else:
                new_string = new_string[wall+len(pattern):]
                count += 1
    return sum(count_list)

for tc in range(10):

    N = int(input())
    bigboard = []
    for tn in range(N):
        bigboard.append(list(map(str, input().split())))

    result_bigboard = list(map(list, zip(*bigboard)))
    count = columnCounting(result_bigboard)
    print(f'#{tc+1} {count}')