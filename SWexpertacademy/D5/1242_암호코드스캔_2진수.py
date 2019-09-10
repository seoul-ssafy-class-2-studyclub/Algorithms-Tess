# 코드 패턴분석

import sys
sys.stdin = open('1242.txt', 'r')
#
# P = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3, (1, 1, 3, 2): 4,(1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7,(1, 2, 1, 3): 8,(3, 1, 1, 2): 9}
#
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#     N, M = map(int, input().split())
#     # 8개 숫자
#     # (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드 10의 배수
#     # 배열은 16진수로 이루어져있고, 2진수로 변환한 후 암호코드 정보 확인
#     # 정상적인 코드인지 확인
#     # 정상적이면 계산 아니면 0출력
#
#     codes = [list(map(str, input())) for _ in range(N)]
#     #print(codes)
#     lasty = 0
#     lastx = 0
#     for y in range(N):
#         for x in range(M-1, -1, -1):
#             if codes[y][x] != '0': # 0뒤에서 부터 0이 아닌곳이 시작
#                 lasty = y
#                 lastx = x
#                 break
#     print(lasty)
#     print(lastx)
#
#     print(codes[lasty])
#
#     print(int('B', 2))
#
#     my_binary = []
#     for code in codes[lasty]:
#         if code.isdigit():
#             a = list(bin(int(code)))
#             a.pop(1)
#             my_binary.append(a)
#         else:
#             print(code)
#             a = list(bin(code))
#             a.pop(1)
#             my_binary.append(a)
#     print(my_binary)
#
#     # 전부 2진수로 변환 후 확인

P = {(2, 1, 1): 0,
     (2, 2, 1): 1,
     (1, 2, 2): 2,
     (4, 1, 1): 3,
     (1, 3, 2): 4,
     (2, 3, 1): 5,
     (1, 1, 4): 6,
     (3, 1, 2): 7,
     (2, 1, 3): 8,
     (1, 1, 2): 9}

A = ord('A') # 68
nine, zero = ord('9'), ord('0')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]


    def getVal(ch):
        t = ord(ch)
        val = (t - A) + 10 if t > nine else t - zero
        return val


    def find():
        ret = 0
        for i in range(N):
            j = M - 1
            while j >= 0:
                if arr[i][j] != '0' and arr[i - 1][j] == '0':
                    pwd = []
                    L = MIN = 0
                    val, c = getVal(arr[i][j]), 0
                    for k in range(8):
                        c2 = c3 = c4 = 0
                        while (val & 1) == 0:
                            print('--', val >> 1)
                            print('-->', val & 1)
                            val, c = val >> 1, c + 1
                            if c == 4:
                                j, c = j - 1, 0
                                val = getVal(arr[i][j])
                        while val & 1:
                            val, c, c4 = val >> 1, c + 1, c4 + 1
                            if c == 4:
                                j, c = j - 1, 0
                                val = getVal(arr[i][j])
                        while (val & 1) == 0:
                            val, c, c3 = val >> 1, c + 1, c3 + 1
                            if c == 4:
                                j, c = j - 1, 0
                                val = getVal(arr[i][j])
                        while val & 1:
                            val, c, c2 = val >> 1, c + 1, c2 + 1
                            if c == 4:
                                j, c = j - 1, 0
                                val = getVal(arr[i][j])
                        if k == 0:
                            MIN = min(c2, c3, c4)

                        pwd.append(P[(c2 // MIN, c3 // MIN, c4 // MIN)])

                    a = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                    b = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                    if ((b * 3 + a) % 10) == 0:
                        ret += (a + b)
                j -= 1
        return ret

    print('#{} {}'.format(tc, find()))

'''

hex2dec = [[0, 0, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0],
           [0, 0, 1, 1],
           [0, 1, 0, 0],
           [0, 1, 0, 1],
           [0, 1, 1, 0],
           [0, 1, 1, 1],
           [1, 0, 0, 0],
           [1, 0, 0, 1],
           [1, 0, 1, 0],
           [1, 0, 1, 1],
           [1, 1, 0, 0],
           [1, 1, 0, 1],
           [1, 1, 1, 0],
           [1, 1, 1, 1]]
 
code = [[[0 for _ in range(5)]  for _ in range(5)]  for _ in range(5)]
 
code[2][1][1] = 0
code[2][2][1] = 1
code[1][2][2] = 2
code[4][1][1] = 3
code[1][3][2] = 4
code[2][3][1] = 5
code[1][1][4] = 6
code[3][1][2] = 7
code[2][1][3] = 8
code[1][1][2] = 9
 
 
def solve(n):
    global M
    j = 4 * M -1
    sum = 0
    while j >= 0:
        if Lst[n][j] == 1 and Lst[n-1][j] == 0:
            num = [0] * 8
            for k in range(7, -1, -1):
                x = y = z = 0
                while Lst[n][j] == 1:
                    z += 1
                    j -= 1
                while Lst[n][j] == 0:
                    y += 1
                    j -= 1
                while Lst[n][j] == 1:
                    x += 1
                    j -= 1
                while k != 0 and Lst[n][j] == 0:
                    j -= 1
 
                t = min(x, y, z)
                x = x // t
                y = y // t
                z = z // t
 
                num[k] = code[x][y][z]
            check = (num[0] + num[2] + num[4] + num[6]) * 3  + num[1] + num[3] + num[5] + num[7]
            if check % 10 == 0:
                sum += num[0] + num[1] + num[2] + num[3] + num[4] + num[5] + num[6] + num[7]
        j -= 1
 
    return sum
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Lst = [[0 for _ in range(4*M)] for _ in range(N+1)]
 
    for i in range(1, N+1):
        temp = input()
        for j in range(M):
            t = temp[j]
            t = int(t, 16)
            for k in range(4):
                Lst[i][j*4+k] = hex2dec[t][k]
 
    sum = 0
    for i in range(1, N):
        sum += solve(i)
 
    print("#{} {}".format(tc, sum))


'''

'''
def htod(h):
    asc = ord(h)
    if asc >= A:
        asc = asc - A + 10
    else:
        asc = asc - zero
    return asc
 
 
def chk_code():
    global c
    password = []
    mag = 0
    bi_num = htod(arr[r][c])
    chk = 0
    for i in range(8):
        ratio = [0, 0, 0]
        while not(bi_num & 1):
            chk += 1
            bi_num >>= 1
            if chk == 4:
                chk = 0
                c -= 1
                bi_num = htod(arr[r][c])
        while bi_num & 1:
            ratio[2] += 1
            chk += 1
            bi_num >>= 1
            if chk == 4:
                chk = 0
                c -= 1
                bi_num = htod(arr[r][c])
        while not (bi_num & 1):
            ratio[1] += 1
            chk += 1
            bi_num >>= 1
            if chk == 4:
                chk = 0
                c -= 1
                bi_num = htod(arr[r][c])
        while bi_num & 1:
            ratio[0] += 1
            chk += 1
            bi_num >>= 1
            if chk == 4:
                chk = 0
                c -= 1
                bi_num = htod(arr[r][c])
        if not mag:
            mag = min(ratio[0], ratio[1], ratio[2])
        if mag > 1:
            ratio = map(lambda x: x // mag, ratio)
        password.insert(0, decode[tuple(ratio)])
    if chk:
        c -= 1
 
    code = 0
    for i in range(8):
        if not i % 2:
            code += password[i] * 3
        else:
            code += password[i]
    if not code % 10:
        return sum(password)
    else:
        return 0
 
decode = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
(2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}
 
zero = ord('0')  # 48
A = ord('A')  # 65
result_list = []
for case in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    visited = []
    result = 0
    for r in range(N):
        c = M - 1
        while c >= 0:
            if arr[r][c] != '0' and (arr[r-1][c] == '0' or r == 0):
                result += chk_code()
            else:
                c -= 1       
 
    result_list.append(result)
 
for i in range(len(result_list)):
    print(f'#{i+1} {result_list[i]}')

'''