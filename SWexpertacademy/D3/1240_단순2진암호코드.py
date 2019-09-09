# 딕셔너리에 추가후 참고하는 형식으로 진행
# 7자리씩 자른다.
# 맞는 번호로 리스트에 담는다
# 식에 맞춰계산한다
# 값이 10의 배수가 맞는지 확인한다.

import sys
sys.stdin = open('1240.txt', 'r')


'''
# (7 + 7 + 5 + 2) * 3 + 5 + 5 + 0 + 7 = 80
# “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수
# 마지막 7자리는 검증코

my_nums = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9',
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    codes = [list(map(int, input())) for _ in range(N)]

    new_N = 0
    start_review = []
    for y in range(N):
        if sum(codes[y]) != 0:
            start_review.append(codes[y])
            new_N += 1
    #print(start_review)

    myx = 0

    for y in range(new_N):
        for x in range(M, -1, -1):
            if 0 <= x < M:
                if start_review[y][x] == 1:
                    myx = x
                    break
    print(myx)

t = 0
for i in range(len(arr)):
    t = t * 2 + int(arr[i])
    if (i+1) % 7 == 0:
        print(t, end=' ')
        t = 0
'''


# 키값을 튜플형식으로 받는다.
P = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3, (1, 1, 3, 2): 4,(1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7,(1, 2, 1, 3): 8,(3, 1, 1, 2): 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    def find():
        for i in range(N):
            for j in range(M - 1, -1, -1):
                if arr[i][j] == '0': # 뒤로가면서, 0이 나오면 패스하고,
                    continue

                # 1이 나오면 시작
                pwd = []
                idx = j
                for k in range(8): # 총 8번을 도는데,
                    c1 = c2 = c3 = c4 = 0
                    while arr[i][idx] == '1': # 뒤부터 검증하므로,
                        c4, idx = c4 + 1, idx - 1

                    while arr[i][idx] == '0':
                        c3, idx = c3 + 1, idx - 1

                    while arr[i][idx] == '1':
                        c2, idx = c2 + 1, idx - 1

                    c1 = 7 - (c2 + c3 + c4)
                    pwd.append(P[(c1, c2, c3, c4)])
                    idx -= c1

                a = pwd[0] + pwd[2] + pwd[4] + pwd[6] 
                b = pwd[1] + pwd[3] + pwd[5] + pwd[7] 
                if ((b * 3 + a) % 10) == 0:
                    return a + b
                else:
                    return 0

    print('#{} {}'.format(tc, find()))

'''

# 모든 코드는 1로 끝나기 때문에 맨 뒷자리를 찾는다.
# 암호코드가 꼭 7의 배수번 째 자리에서 시작한다는 보장이 없기 때문.
def find_end():
    for c in range(M - 1, -1, -1):
        for r in range(N):
            if arr[r][c] == '1':
                return (r, c)
    return 0
​
​
code = {'0001101': 0, '0011001': 1, '0010011':2, '0111101': 3, '0100011': 4, '0110001': 5,
'0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
​
for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    idx = find_end()

    if not idx: # idx가 0 이라면,
        print(f'#{case} 0')
        continue

    r, c = idx # 0이 아니라 (r, c)라면,
    password = []
    temp = ''
    for i in range(c, c-56, -1): # 1이 있다면 8자리가 반드시 존재할 것이다. 즉, 8*8 = 56 이므로, 1을 발견한 곳부터 -56번째 까지가 첫 시작점임을 알 수 있다.
        temp = arr[r][i] + temp
        if len(temp) == 7:
            password.insert(0, code[temp]) # 뒤에서부터 추가되기 때문에 password리스트에 키값으로 검색한 값을 0번째 인덱스에 끼워넣는다.
            temp = ''

    chk = 0
    for i in range(len(password)): # password리스트에 들어가있는 순서대로,
        if not i % 2: # 0이 아니라면, 짝수
            chk += password[i] * 3
        else: # 0이라면, 홀수
            chk += password[i]
​
    if not chk % 10:
        print(f'#{case} {sum(password)}')
    else:
        print(f'#{case} 0')
'''