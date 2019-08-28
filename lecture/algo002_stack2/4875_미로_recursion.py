import sys
sys.stdin = open('4875.txt', 'r')

dy = [0, 1, -1, 0]
dx = [1, 0, 0, -1]

def is_ok(Y, X):
    return 0 <= Y < n and 0 <= X < n and mymap[Y][X] != 1

# 목적지 도착 여부를 찾는 함수
'''
def find_map(y,x):
    # 종료
    if mymap[y][x] == 3:
        result = 1
        return result
    -------------------
    visited.append((y,x))
    if 우측이 갈 수 있는지 그리고 안 간 좌표이면:
        find_map(우측 좌표)
        "델타 반복"
'''

def find_map(startY, startX):
    global result
    # 1. 종료조건
    if mymap[startY][startX] == 3:
        result = 1
        return

    # 2. 반복검색

    # 같은데가 아닌 것을 체크
    visited.append((startY, startX))

    # 4방향 검색
    # 범위 제어조건
    if is_ok(startY, startX+1) and (startY, startX+1) not in visited:
        find_map(startY, startX+1) # 우측
    if result == 0 and is_ok(startY+1, startX) and (startY+1, startX) not in visited:
        find_map(startY+1, startX)# 아래
    if result == 0 and is_ok(startY, startX-1) and (startY, startX-1) not in visited:
        find_map(startY, startX-1)# 좌측
    if result == 0 and is_ok(startY-1, startX) and (startY-1, startX) not in visited:
        find_map(startY-1, startX)# 위


TC = int(input())
for tc in range(1, TC+1):
    n = int(input()) # 한 변의 길이
    mymap = [list(map(int, input())) for _ in range(n)] # 2차원 배열 구성
    print(mymap)

    # 시작지점 찾기
    starty = -1
    startx = -1
    for y in range(n):
        for x in range(n):
            if mymap[y][x] == 2:
                # 3 시작점이 있는 좌표 확인
                starty = y
                startx = x

    # 미로 필수 요소 -> 방문했던 위치 저장소
    visited = []
    # -> 목적지 도착 여부
    result = 0

    find_map(starty, startx)

    print(result)









