'''
1940. 가랏! RC카! D2

0 : 현재 속도 유지.
1 : 가속
2 : 감속

RC 카의 초기 속도는 0 m/s


입력         시간     RC 카의 속도 RC     카의 이동거리
1 2          1 sec          2 m/s                    2 m
2 1          2 sec          1 m/s                    3 m


-> 3


-1
-33

#9 48
#10 111

'''

for T in range(int(input())):

    TT = int(input())


    distance = 0
    speed = 0

    for sec_index in range(TT):
        command_large_list = list(map(int, input().split()))

        if command_large_list[0] == 0:
            distance += speed

        if command_large_list[0] == 1:
            speed += command_large_list[1]
            distance += speed

        if command_large_list[0] == 2:

            if command_large_list[1] < speed:
                speed -= command_large_list[1]
                distance += abs(speed)
            else:
                speed = 0


        else:
            continue

    print(f'#{T+1} {distance}')




