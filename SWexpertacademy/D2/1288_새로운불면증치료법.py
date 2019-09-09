'''

문제이해:
k번째에는 kN번째 양을 센다.

필요조건:
k
N

'''


'''

1. for문과 set, list 활용하여 문제품

'''

for for_num in range(int(input())):
    N = int(input())
    num_list = []
    set_list = []
    k = 0
    while len(set_list) < 10:
        k += 1
        number = k * N
        str_number = str(number)
        for i in range(len(str_number)):
            num_list.append(str_number[i])
            set_list = set(num_list)
    print(f'#{for_num + 1} {k * N}')


'''

2. set 특징 활용하여 문제 풀기

'''


for T in range(int(input())):
    N = int(input()) ## 1
    k = 1
    x = set(str(N)) ## {1} ### {1, 2} #### {1, 2, 3} ... 반복
   # set (1. 중복된 값은 사라진다. 2. 순서가 없다. 라는 특징 활용)
    while len(x) < 10: # 10 미만인 경우에 계속 반복한다. 1, 2, 3, 4, 5, 6, 7, 8, 9
        ### 2
        k += 1 # k에 반복한 수를 추가한다.
        x.update(str(k*N)) ## 2*1 -> 2 ### 3*1 -> 3
        # set.update('value')로 값을 추가한다.
    print(f'#{T+1} {k*N}')
