# 2진수와 3진수의 한 자리를 값을 바꿔주는 것
# 바꾼 2진수와 3진수를 10진수의 값으로 변환
# 이 두 개의 값을 비교해서 같은지를 비교


#(1) 2진수와 3자리수의 값들을 for문을 통해서 숫자 한자리씩 변경해주고,
# 그것을 (2) 10진수 값들로 변환한후 각각의 다른 배열에 저장합니다.
# (3)최종적으로 서로 비교해주면 됩니다.


import sys
sys.stdin = open('4366.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    bi_num = input()
    tri_num = input()

    bi_num_lst = []
    tri_num_lst = []
    for i in range(len(bi_num)):
        bi_num2 = list(bi_num)

        if bi_num2[i] == '0':
            bi_num2[i] = '1'
            bi_num_lst.append(int(''.join(bi_num2), 2))

        else:
            bi_num2[i] = '0'
            bi_num_lst.append(int(''.join(bi_num2), 2))


    for i in range(len(tri_num)):
        tri_num2 = list(tri_num)
        if tri_num2[i] == '0':
            tri_num2[i] = '1'
            tri_num_lst.append(int(''.join(tri_num2),3))
            tri_num2[i] = '0'
            tri_num2[i] = '2'
            tri_num_lst.append(int(''.join(tri_num2),3))

        elif tri_num2[i] == '1':
            tri_num2[i] = '2'
            tri_num_lst.append(int(''.join(tri_num2),3))
            tri_num2[i] = '1'
            tri_num2[i] = '0'
            tri_num_lst.append(int(''.join(tri_num2),3))

        else:
            tri_num2[i] = '0'
            tri_num_lst.append(int(''.join(tri_num2),3))
            tri_num2[i] = '2'
            tri_num2[i] = '1'
            tri_num_lst.append(int(''.join(tri_num2),3))

    result = 0
    for i in bi_num_lst:
        if i in tri_num_lst:
            result = i
            break

    print(f'#{tc} {result}')