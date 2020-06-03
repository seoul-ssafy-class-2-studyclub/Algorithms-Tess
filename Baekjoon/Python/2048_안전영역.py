import sys
sys.stdin = open('2048.txt', 'r')


# 가장 높은 max 값을 찾는다.
# max에서 1이 까지 -1해보면서
# dfs로 남은 안전영역을 세는 식으로 한다.

# 그리고 남은 안전영역중에 가장 max인 값이 답이 된다.


N = int(input())
earth = [list(map(int, input().split())) for _ in range(N)]
# print(N)
# print(earth)

my_max = -1
for i in range(N):
    for j in range(N):
        if earth[i][j] > my_max:
            my_max = earth[i][j]

# print(my_max)

def waterfall(dummy_earth):
    # print(dummy_earth[0][N-1])
    # print(my_max)
    for i in range(N):
        # print(i)
        for j in range(N):
            # print(dummy_earth[i][j])
            if dummy_earth[i][j] <= my_max:
                dummy_earth[i][j] = -1
    # print(dummy_earth)
    return dummy_earth
            
def find_safe_place(waterfall_dummy_earth):
    
    start_y, start_X = -1, -1 
    # 이제 여기서 시작
    # dfs 로 돌면서 cnt++를 늘리며 찾는다. 안전지대를
    # for 문으로 쭉 돌면서 만나면 시작! -> 만나는 순간부터 dfs 시작해서 쭉 돌기. 
    # 돌면서 dfs로 -1로 색칠한다.
    # 만나지 못하면 그냥 쭉 가게된다.
    cnt = 0
    for i in range(N):
        for j in range(N):
            # print(waterfall_dummy_earth)
            if waterfall_dummy_earth[i][j] != -1:
                # print("=================")
                start_y = i
                start_x = j
                stack = [(i, j)]
                cnt += 1
                # print(stack)
                while stack:
                    # print(stack)
                    iy, ix = stack.pop()
                    waterfall_dummy_earth[i][j] = -1
                    for dy, dx in [(0,1), (1, 0), (-1, 0), (0, -1)]:
                        iiy = dy + iy
                        iix = dx + ix
                        if iiy < N and iix < N and waterfall_dummy_earth[i][j] != -1:
                            stack.append((iiy, iix))
    # print(cnt)
    # print(waterfall_dummy_earth)
    return cnt

answer = -1

for i in range(my_max):
    dummy_earth = [i[:] for i in earth]
    # print(dummy_earth)
    # print("==========")
    # print(dummy_earth)
    waterfall_dummy_earth = waterfall(dummy_earth)
    find_safe = find_safe_place(waterfall_dummy_earth)
    
    # print(find_safe)
    if answer < find_safe:
        answer = find_safe
    my_max -= 1
# print(dummy_earth)
print(answer)