
T = int(input())
for tc in range(1, T+1):
    R = int(input())
    r_list = []
    for r in range(R):
        temp_list = list(map(int, input().split()))
        r_list.append(temp_list)
    #print(r_list)

    big_board = [[0] * 10 for i in range(10)]
    #print(len(big_board))

    for ri in range(R):
        x1 = r_list[ri][0]
        y1 = r_list[ri][1]
        x2 = r_list[ri][2]
        y2 = r_list[ri][3]
        color = r_list[ri][4]
        #print(x1, y1, x2, y2, color)
        if x1 >= x2:
            minx = x2
            maxx = x1
        else:
            minx = x1
            maxx = x2

        if y1 >= y2:
            miny = y2
            maxy = y1
        else:
            miny = y1
            maxy = y2


        for iy in range(miny, maxy+1):
            for ix in range(minx, maxx+1):
                big_board[iy][ix] += color # 3

    count = 0
    for iy in range(len(big_board)):
        for ix in range(len(big_board)):
            if big_board[iy][ix] >= 3:  # if
                count += 1  # count

    print(f'#{tc} {count}')