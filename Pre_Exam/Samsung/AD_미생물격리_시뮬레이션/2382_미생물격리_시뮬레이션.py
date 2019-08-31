import sys
sys.stdin = open('2382.txt', 'r')

"""

#1 145
#2 5507
#3 9709
#4 2669
#5 3684
#6 774
#7 4797
#8 8786
#9 1374
#10 5040

10
7 2 9
1 1 7 1
2 1 7 1
5 1 5 4
3 2 8 4
4 3 14 1
3 4 3 3
1 5 8 2
3 5 100 1
5 5 1 1
...	// 총 테스트케이스 개수 T=10
// 테스트 케이스 1,     N=7, M=2, K=9
// 세로위치(1), 가로위치(1), 미생물 수(7), 이동방향(상)
// 세로위치(3), 가로위치(2), 미생물 수(8), 이동방향(우)
// 세로위치(3), 가로위치(4), 미생물 수(3), 이동방향(좌)
// 세로위치(1), 가로위치(5), 미생물 수(8), 이동방향(하)

// 나머지는 sample_input.txt 참조
"""

# 읽기 편하기 위해서 0번째 인덱스는 삭제
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

# D_status = 상: 1, 하: 2, 좌: 3, 우: 4

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N=7, M=2, K=9

    # 미생물의 정보를 넣는 기본테이블 구조 생성
    dict_table = {'index_name':
                     {
                         'Y': 0,
                        'X': 0,
                        'numofCell': 0,
                        'D_status': 0,
                         'alive': True,
                         'changed': 0,
                     },
        }
    #print(dict_table['index_name']['alive'])

    # 미생물의 정보를 검색해서 빼올 테이블 완성
    for name in range(1, K+1):
        Y, X, numofCell, D_status = map(int, input().split()) # 세로위치(2), 가로위치(1), 미생물 수(7), 이동방향(상)
        dict_table[name] = {'Y': Y, 'X': X, 'numofCell': numofCell, 'D_status': D_status, 'alive': True, 'changed': numofCell}
    #print(dict_table)

    originalmap = [[-1]*N for _ in range(N)]
    # 보드 약품 처리, -1이 되면
    # 군집내 미생물은 미생물수//2 가 되며, 방향이 바뀐다.

    # originalmap = 모든 데이터가 정상적으로 저장될 곳
    s = [0] * (N - 1)
    for i in range(1, N-1):
        originalmap[i][1:N-1] = s[:]
    #print(originalmap)

    """
    1. 내가 가서 자리를 차지할 수 있는 곳인지 확인, == 이동방향이 바뀌지 않을 위치인지, 해당 위치에 누군가 있는지
    반복문 안에서 돌리고, 그 자리에 누가 있는지 확인하는 맵 그 맵에는 미생물의 수가 저장된다. 필요.
    """

    # 미생물의 수가 비교될 곳
    comparemap = [[-1] * N for _ in range(N)]
    for i in range(1, N-1):
        comparemap[i][1:N-1] = s[:]
    #print(comparemap)
    # M 이라는 시간내에 일어나는 일들
    # h는 해당 시간을 가리킨다.
    """
    2. -1 에 닿으면, 
    군집내 미생물수가 줄어들며 미생물수//2
    방향이 바뀐다. D_status의 반대방향
    0이 되면 죽는다. 
    Alive = True -> False
    originalmap에는 인덱스 이름을 저장하고
    comparemap에는 미생물 수를 저장한다.
    """
    # 둘다 시간이 지남에따라 방향에 맞게 좌표를 바꾼다.
    # 맨처음에 설정해줘야 한다!
    for k in range(1, K + 1):
        for y in range(N):
            for x in range(N):
                originalmap[dict_table[k]['Y']][dict_table[k]['X']] = k
                comparemap[dict_table[k]['Y']][dict_table[k]['X']] = dict_table[k]['numofCell']


    for h in range(M):
        for k in range(1, K + 1):
            num = 0
        # print(dict_table[k]['alive'])
            #print(dict_table[k]['alive'])
            y = dict_table[k]['Y']
            x = dict_table[k]['X']
            tempy = y + dy[dict_table[k]['D_status']]
            tempx = x + dx[dict_table[k]['D_status']]

            if 0 <= tempy < N and 0 <= tempx < N and dict_table[k]['alive'] == True:
                if originalmap[y][x] == k and originalmap[tempy][tempx] == 0:
                    print('check')
                    dict_table[k]['Y'] = tempy
                    dict_table[k]['X'] = tempx
                    originalmap[tempy][tempx] = k
                    comparemap[tempy][tempx] = dict_table[k]['numofCell']

                    originalmap[y][x] = 0
                    comparemap[y][x] = 0

                elif originalmap[y][x] == k and originalmap[tempy][tempx] == -1:
                    print('언제 7', k, y, x, dict_table[k]['numofCell'], tempy, tempx)
                    dict_table[k]['Y'] = tempy
                    dict_table[k]['X'] = tempx
                    num = dict_table[k]['numofCell']//2

                    #print(num)
                    if num == 0:
                        print(num)
                        dict_table[k]['alive'] = False
                        dict_table[k]['numofCell'] = num
                        originalmap[y][x] = 0
                        comparemap[y][x] = 0

                    elif num > 0:
                        print(num)
                        dict_table[k]['numofCell'] = num
                        originalmap[tempy][tempx] = k
                        comparemap[tempy][tempx] = num
                        originalmap[y][x] = 0
                        comparemap[y][x] = 0

                        if dict_table[k]['D_status'] == 1:
                            dict_table[k]['D_status'] = 2

                        elif dict_table[k]['D_status'] == 2:
                            dict_table[k]['D_status'] = 1

                        elif dict_table[k]['D_status'] == 3:
                            dict_table[k]['D_status'] = 4

                        elif dict_table[k]['D_status'] == 4:
                            dict_table[k]['D_status'] = 3

                elif originalmap[dict_table[k]['Y']][dict_table[k]['X']] == k and comparemap[tempy][tempx] > 0:
                    # 미생물수 비교
                    # 만약 갈 위치에있는 군집이 더 많은 미생물을 갖고있다면,
                    new = originalmap[tempy][tempx]
                    print(originalmap[dict_table[k]['Y']][dict_table[k]['X']], comparemap[tempy][tempx])
                    if comparemap[tempy][tempx] > dict_table[k]['numofCell']:
                        # 나는 죽고,
                        dict_table[k]['alive'] = False
                        # 내가 가진 미생물을 갈위치에있는 군집에게 준다.
                        dict_table[originalmap[tempy][tempx]]['changed'] += dict_table[k]['numofCell']

                        originalmap[tempy][tempx] = new
                        comparemap[tempy][tempx] = dict_table[new]['numofCell'] ##
                        dict_table[new]['Y'] = tempy
                        dict_table[new]['X'] = tempx

                        originalmap[y][x] = 0
                        comparemap[y][x] = 0

                    # 만약 갈 위치에 군집이 더 적은 미생물을 갖고있다면,
                    elif comparemap[tempy][tempx] < dict_table[k]['numofCell']:
                        # 나는 살지만 그 적은 미생물을 가진 군집이 죽고,
                        dict_table[new]['alive'] = False
                        # 그 적은 미생물을 가진 군집의 미생물을 내가 갖는다.
                        dict_table[k]['changed'] += dict_table[new]['numofCell']

                        originalmap[tempy][tempx] = k
                        comparemap[tempy][tempx] = dict_table[originalmap[tempy][tempx]]['numofCell'] ##
                        dict_table[k]['Y'] = tempy
                        dict_table[k]['X'] = tempx

                        originalmap[y][x] = 0
                        comparemap[y][x] = 0


    total1 = 0
    total2 = 0
    for k in range(1, K+1):
        if dict_table[k]['alive'] == True:
            total1 += dict_table[k]['numofCell']
            total2 += dict_table[k]['changed']
            print('---------------numofCell')
            print(dict_table[k]['numofCell'])
            print('---------------changed')
            print(dict_table[k]['changed'])

    print('#{} {}'.format(tc, total1))
    print('#{} {}'.format(tc, total2))



