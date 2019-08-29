import sys
sys.stdin = open('1913.txt', 'r')


def snail(n):
    global direction_list
    num = 0
    direction_index = 0
    current_r, current_c = 0, -1
    array = [[-1]*n for _ in range(n)]

    while num < n*n:
        dir = direction_list[direction_index]
        temp_r = current_r + dir[0]
        temp_c = current_c + dir[1]

        # 범위초과시 방향을 바꾼다

        if temp_c < 0 or temp_r < 0 or temp_c >= n or temp_r > n or array[temp_r][temp_c] != -1:
            direction_index += 1
            if direction_index == 4:
                direction_index = 0
            else:
                num += 1
                current_r, current_c = temp_r, temp_c
                array[current_r][current_c] = num
    return array


# 변화하는 방향: 하, 우, 상, 좌
# direction_list = [(0,1), (1,0), (0,-1), (-1,0)]
#     #[(1,0), (0,-1), (-1,0), (0,1)]
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

N = int(input()) # 7**2 만큼의 달팽이 배열
Goal = int(input()) # 달팽이 배열을 만들고, Goal이 있는 좌표 출력

print(N**2)
result = snail(N)
for line in result:
    print(''.join(map(str, line)))