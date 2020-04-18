def solution(office, r, c, move):
    direction = [(1,0), (-1,0), (0,1), (0,-1)]
    # r, c 부터 시작해서 간다.
    ans = 0
    # 북쪽을 바라보는 상태면,
    status = 1 # -1,0 이라는 소리
    current = [r, c]
    goChanges = {0:0, 1:1, 2:2, 3:3}
    leftChanges = {0:2, 1:3, 2:1, 3:0}
    rightChanges = {1:2, 0:3, 2:0, 3:1}
    N = len(office)
    M = len(office[0])
    ans += office[r][c]
    office[r][c] = 0
    while move:
        order = move.pop(0)
        if order == "go":
            status = goChanges[status]
            dy, dx = (current[0] + direction[status][0]), (current[1] + direction[status][1])
            if N > dy >= 0 and M > dx >= 0:
                if office[dy][dx] == -1:
                    continue
                elif office[dy][dx] == 0:
                    current = [dy,dx]
                    continue
                else:
                    current = [dy,dx]
                    ans += office[dy][dx]
                    office[dy][dx] = 0
                    continue
            else:
                if office[current[0]][current[1]] > 0:
                    ans += office[dy][dx]
                    office[dy][dx] = 0
                    continue
        if order == "left":
            status = leftChanges[status]

        if order == "right":
            status = rightChanges[status]
    return ans

solution([[5,-1,4],[6,3,-1],[2,-1,1]], 1, 0, ["go","go","right","go","right","go","left","go"])