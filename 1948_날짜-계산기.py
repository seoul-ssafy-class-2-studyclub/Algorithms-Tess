'''
월 일로 이루어진 날짜를 2개 입력 받아,
두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력

1948. 날짜 계산기

12 >= 월 >= 1

1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31

두번째 날짜가 첫번째 날짜보다 항상 크
월 일 월 일
3 1 3 31

31
'''

## 딕셔너리, 인덱스 중요했던 문제

for T in range(int(input())):

    dates_list = list(map(int, input().split()))
    dates_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    if dates_list[0] == dates_list[2]:
        for month, day in dates_dict.items():
            if month == dates_list[0]:
                print(f'#{T+1} {day}')

    elif dates_list[0] != dates_list[2]:
        result1 = dates_list[3]
        day_count = 0

        for month, day in dates_dict.items():
            if dates_list[2]-1 >= month >= dates_list[0]+1:
                day_count += dates_dict[month]

            if month == dates_list[0]:
                result2 = day - dates_list[1]

            else:
                continue # continue를 해주지 않으면 값 추출 불가능함, 자세한 이유가 뭘까요.

        total = result1 + result2 + day_count + 1

        print(f'#{T+1} {total}')
