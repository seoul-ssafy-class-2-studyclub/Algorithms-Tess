import sys
sys.stdin = open('1211.txt', 'r')


def Search(arr, defdy, defdx):

    while defdy <= 99:

        if defdy == 99:
            return total_dict

        elif defdx == 0:
            for (dy, dx) in [[0, 1], [1, 0]]:
                if arr[defdy + dy][defdx + dx] == '1':
                    arr[defdy + dy][defdx + dx] = '3'
                    total_dict[start] += 1
                    defdy = defdy + dy
                    defdx = defdx + dx

        elif defdx == 99:
            for (dy, dx) in [[0, -1], [1, 0]]:
                if arr[defdy + dy][defdx + dx] == '1':
                    arr[defdy + dy][defdx + dx] = '3'
                    total_dict[start] += 1
                    defdy = defdy + dy
                    defdx = defdx + dx

        elif 1 <= defdx < 99:  # 1~98
            for (dy, dx) in all_directions:
                if mat[defdy + dy][defdx + dx] == '1':
                    mat[defdy + dy][defdx + dx] = '3'
                    total_dict[start] += 1
                    defdy = defdy + dy
                    defdx = defdx + dx


for _ in range(10):
    tc = int(input())
    all_directions = [[0, 1], [0, -1], [1, 0]]

    mat = []
    for _ in range(100):
        mat.append(list(input().split()))

    start_x_indexes = []
    for x in range(100):
        if mat[0][x] == '1':
            start_x_indexes.append(x) # index가 시작되는 곳을 모아둔 곳

    total_dict = {} # 데이터를 저장할 곳

    tempdy = 0
    for tempx in start_x_indexes:
        tempdx = tempx
        start = tempx
        total_dict[start] = 0
        res = Search(mat, tempdy, tempdx)
        for idy in range(100):
            for idx in range(100):
                mat[idy][idx] = mat[idy][idx].replace('3', '1')  ## mat 다시 reset 하는 방법.,.

    find_min = []
    for value in res.values():
        find_min.append(value)
    target = min(find_min)

    find_min_x_idx = []
    for key, value in res.items():  #mydict에 아이템을 하나씩 접근해서, key, value를 각각 name, age에 저장
        if value == target: # 그중에 가장 큰 x 인덱스를 가진 출발점
            find_min_x_idx.append(key)
    final = max(find_min_x_idx)
    print(f'#{tc}', final)


