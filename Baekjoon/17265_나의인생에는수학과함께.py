import sys
# sys.stdin = open('17264.txt', 'r')
# 가는 곳도 정해져 있고, 탈출하는 곳도 확실하기때문에 vis처리를 하지 않아도 된다.
input = sys.stdin.readline
N = int(input())
mymap = [list(map(str, input().split())) for _ in range(N)]
mymin = 1e9
mymax = -1e9
q = []                    # 아직 연산자가 없거나, 사용한적 없으면 -1
q.append((int(mymap[0][0]), -1, 0, 0))
while q:
    for _ in range(len(q)):
        C, op, y, x = q.pop(0)
        if y == N-1 and x == N-1:
            if C < mymin:
                mymin = C
            if C > mymax:
                mymax = C
            continue
        for dy, dx in [(0, 1), (1, 0)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < N:
                if mymap[iy][ix] == '-':
                    q.append((C, 2, iy, ix))
                if mymap[iy][ix] == '+':
                    q.append((C, 1, iy, ix))
                if mymap[iy][ix] == '*':
                    q.append((C, 0, iy, ix))
                if op != -1:
                    if op == 2:
                        q.append((C - int(mymap[iy][ix]), -1, iy, ix))
                    if op == 1:
                        q.append((C + int(mymap[iy][ix]), -1, iy, ix))
                    if op == 0:
                        q.append((C * int(mymap[iy][ix]), -1, iy, ix))
print(mymax, mymin)

