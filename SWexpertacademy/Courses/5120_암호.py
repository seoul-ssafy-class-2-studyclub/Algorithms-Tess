import sys
sys.stdin = open('5120.txt', 'r')
'''
#1 5 6 1 9 13 4 2 8 6
#2 1736 2514 778 169 667 498 329 715 386 958
#3 826 1494 668 954 375 1052 677 302 774 2234
'''
temp = '1736 2514 778 169 667 498 329 715 386 958'

## 1736이 추가되면, 시작번호는 추가된 값부터다.
temp1 = list(map(int, temp.split()))
print('정답은',list(reversed(temp1)))

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    standard = M
    stack = []
    stack.append((M, data))
    for k in range(K):
        M, data = stack.pop()
        N = len(data)
        # print(M, N)
        # print(N)
        찾은 data[M:0]사이에 껴넣기
        if N < M:
            # print('xxxx', M, N)
            M = M - N # 9 - 7
            # print(M)
            data1 = data[:M]
            data2 = data[M:]
            #print(data1)
            #print(data2)
            middle = [data1[-1]+data2[0]]
            # print(middle)
            data4 = data1+middle+data2
            data = data4
            M = M + standard
            stack.append((M, data))

        elif N == M: # 0일 경우
            print('c-!!!!!!-------', M, N)
            M = M - N
            print(M)
            data1 = data[M:]
            print(data1)
            print(data1[-1], '이거야? ',data1[-2])
            middle = [data1[-1] + data1[0]]
            print(middle)
            # data2 = data[]
            data4 = data1 + middle
            data = data4
            print('c--------', M, N)
            M = M + standard
            print('c------', data)

            stack.append((M, data))


        else:
            data1 = data[:M]
            data2 = data[M:]
            #print(data1)
            #print(data2)
            middle = [data1[-1]+data2[0]]
            # print(middle)
            data4 = data1+middle+data2
            data = data4
            M = M + standard
            stack.append((M, data))
    #print(data)
    print(f'#{tc}', end=' ')
    N = len(data)
    res = list(reversed(data))
    for idx in range(10):
        if N <= idx:
            break
        else:
            print(res[idx], end=' ')
    print()