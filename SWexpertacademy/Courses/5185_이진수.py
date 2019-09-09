# 16진수 2진수로 표
import sys
sys.stdin = open('5185.txt', 'r')

# data = '47FE'
# print(int(data,16))
# print(bin(18430))
#
# a = int('41DA16CD',16)
# print(bin(a))



# replace로 바꾸는 것
# 테이블 만들어서 문자열 쭉 쓰기


T = int(input())
for tc in range(1, T+1):
    N, data = map(str, input().split())
    a = bin(int(data, 16))[2:].zfill(8)
    print(f'#{tc}', 0, end='')
    print(a)


    # print(f'#{tc}', end=' ')
    # for i in range(len(a)):
    #     if a[i] == '0' or a[i] == '1':
    #         print(a[i], end='')
    # print()

# 1's 1의 보수

# 2's 2의 보수

# 하드웨어는 더하기 연산으로 되어있다.