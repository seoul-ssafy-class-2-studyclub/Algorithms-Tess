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

'''
크게 두 가지 분기를 사용
1. 주어진 상황 두 months 같은 경우
같으면 months를 key로 day를 찾는다.
'''

    if dates_list[0] == dates_list[2]:
        print(f'#{T+1} {dates_dict[dates_list[0]]}')

'''
2. 두 months 다른 경우
계산할 값들을 뽑아내는게 관건 이였다고 생각합니다.

total = result1 + result2 + day_count + 1

위 식을 만들기 위해 총 result1, result2, day_count 의 값을 뽑아올 것입니다.
'''
    elif dates_list[0] != dates_list[2]:
        result1 = dates_list[3]
        day_count = 0

        for month, day in dates_dict.items(): # .items() 함수로 딕셔너리 내의 month와 day 정보를 순환하고,
            if dates_list[2]-1 >= month >= dates_list[0]+1: # list에서 주어진 months 가운데 months들의 day 값을 딕셔너리에서
                day_count += dates_dict[month]              # 가져와서 day_count에 더해줍니다.

            if month == dates_list[0]: # 만약 딕셔너리의 month가 list의 month와 같을때의 key에서,
                result2 = day - dates_list[1] # result2의 값을 구합니다.

            else:
                continue # continue를 해주지 않으면 값 추출 불가능함, 자세한 이유가 뭘까요. (여하튼 처리완료!)

        total = result1 + result2 + day_count + 1

        print(f'#{T+1} {total}')
