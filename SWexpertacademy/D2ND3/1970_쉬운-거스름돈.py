'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE

1970. 쉬운 거스름돈


2
32850
160

money = {50000 : 0, 10000 : 0, 5000 : 0, 1000 : 0, 500 : 0, 100 : 0, 50 : 0, 10 : 0}

10 <= N <= 1000000

N[-1] == 0

32850
0 3 0 2 1 3 1 0

나누기 /
몫 //
나머지 %
'''

for T in range(int(input())):
    money_input = int(input())
    money_dict = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0,
    }

    # 50000/돈 나누면, 50000//돈 몫 50000%돈 나머지가 나오고,
    for money, count in money_dict.items():
        change = money_input // money # 몫은 해당 원 단위의 거스름돈 개수이며,
        remainder = money_input % money # 나머지는 다음 원 단위로 다시 나눠야할 돈이된다.
        money_input = remainder # 그 나머지를 순환시키기 위해서 처음 받은 돈을 넣었던 매개변수에 할당한다.
        money_dict[money] = change

    print(f'#{T+1} ')
    for count in money_dict.values():
        print(f'{count}', end=' ')
    print()



