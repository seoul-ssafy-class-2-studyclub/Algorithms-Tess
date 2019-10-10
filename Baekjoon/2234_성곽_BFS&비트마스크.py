import sys
sys.stdin = open('2234.txt', 'r')

'''
7 4
11 6 11 6 3 10 6
7 9 6 13 5 15 5
1 10 12 7 13 7 5
13 11 10 8 10 12 13
'''

# 굵은 선은 벽을 나타내고, 점선은 벽이 없어서 지나다닐 수 있는 통로
'''
이 성에 있는 방의 개수
가장 넓은 방의 넓이
하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
'''

# 다음 m개의 줄에는 n개의 정수로 벽에 대한 정보가 주어진다.
n, m = map(int, input().split())





def firststep(Y, X): # 시작점을 돈다.
    global castle, numbered_castle, visited
    width = 0 # 넓이를 계산할것
    neighbours = {} # 다른 번호를 만나면 넣어줄 set









    return width, neighbours
    pass


def thirdstep():
    # 이웃을 돌면서, 이웃의 크기와 자신의 크기를 더해본다.
    pass





# 벽에 대한 정보는 한 정수로 주어지는데,
# 서쪽에 벽이 있을 때는 1을,
# 북쪽에 벽이 있을 때는 2를,
# 동쪽에 벽이 있을 때는 4를,
# 남쪽에 벽이 있을 때는 8을 더한 값이 주어진다.
# 이진수의 각 비트를 생각하면 쉽다. 따라서 이 값은 0부터 15까지의 범위 안에 있다.

# 방숫자 & (1 << i)
castle = [ list(map(int, input().split())) for _ in range(m) ]
print(castle)
# 이진수로 자리 구하기
# 0001 0010 0100 1000
west = 1 << 1
north = 1 << 2
east = 1 << 4
south = 1 << 8
print(west, north, east, south)

# ->0001 0010 0100 1000 을 &해서 true 벽
# 없으면 벽아님, 이동

# 벽이 없는 곳들을 색칠하고, 빠져나오면 새로운 방을 또 색칠한다.
# 1. 빠져나올때마다 1씩 늘려서 방마다 번호를 매긴다. 2. 매길때, 방의 넓이를 따로 cnt해준다.

# 3. 하나의 벽을 제거했을때 얻을 수 있는 가장 큰 방의 크기를 알기위해서,
# 한 방에서 가까운 이웃 번호를 찾고,
# 그 이웃번호가 가진 방의 넓이를 각각의 방마다 조합을 구한 후
# 그 크기중에 가장 큰 방의 크기를 답으로 출력한다.

numbered_castle = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
paints = 0
information = {}
# 전체를 돌면서 BFS로 색칠한다.
for y in range(m):
    for x in range(n):
        if visited[y][x] == False:
            paints += 1
            Width, Neighbours = firststep(y, x)
            information[paints] = [Width, Neighbours]

thirdstep()



'''
& (Binary AND) : bit 단위로 and연산을 합니다.
| (Binary OR) : bit 단위로 or연산을 합니다.
^ (Binary XOR) : bit 단위로 xor연산을 합니다.
~ (Binary NOT) : bit 단위로 not연산을 합니다.(1의 보수)
<< (Binary left Shift) : bit 단위로 왼쪽으로 비트단위 밀기 연산을 합니다.
>> (Binary right Shift) : bit 단위로 오른쪽으로 비트단위 밀기 연산을 합니다.
'''


'''
import sys
from collections import deque
​
input = sys.stdin.readline
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
M, N = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
room_num = 1
max_area = 0
broken = 0
for r in range(N):
    for c in range(M):
        if vis[r][c]:
            continue
        queue = deque()
        queue.append((r, c))
        vis[r][c] = [room_num, 1]
        while queue:
            y, x = queue.popleft()
            room = castle[y][x]
            for i in range(4):
                if not room & (1 << i):
                    yi = y + dy[i]
                    xi = x + dx[i]
                    if not vis[yi][xi]:
                        vis[yi][xi] = vis[r][c]
                        vis[yi][xi][1] += 1
                        queue.append((yi, xi))
        room_num += 1
        if vis[r][c][1] > max_area:
            max_area = vis[r][c][1]
​
for r in range(N):
    for c in range(M):
        for i in range(2, 4):
            ri = r + dy[i]
            ci = c + dx[i]
            if ri < N and ci < M and vis[r][c][0] != vis[ri][ci][0]:
                temp = vis[r][c][1] + vis[ri][ci][1]
                if temp > broken:
                    broken = temp
​
print(room_num - 1)
print(max_area)
print(broken)
'''