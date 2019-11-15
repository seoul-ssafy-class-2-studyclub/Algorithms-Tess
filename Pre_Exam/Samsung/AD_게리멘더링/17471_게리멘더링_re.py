import sys
sys.stdin = open('17471.txt', 'r')
N = int(input())
numofpeople = [0]+list(map(int, input().split()))
adj_list = [[] for _ in range(N+1)]
for name in range(1, N+1):
    data = list(map(int, input().split()))
    tdata = data[1:]
    for i in range(1, data[0]+1):
        adj_list[name].append((data[i]))
names = [ i for i in range(1, N+1) ]


def CC2(arr):
    goal_length = len(arr)
    vis2 = [False] + ([False] * (N + 1))
    length = 1
    queue = [arr[0]]
    flag = 0
    while queue:
        now = queue.pop(0)
        vis2[now] = True
        for child in adj_list[now]:
            if child in arr:
                if vis2[child] == False:
                    vis2[child] = True
                    queue.append(child)
                    length += 1
        if length == goal_length:
            flag =1
            break
    return True if flag else False


def combi(k, s):
    global start, names, t, N
    if k == start:
        # 들어온 t에 대해서 유효한 애들인지 확인한다.
        # 그 유효한 애들을 가지고 second를 구하고,
        # 그런데 그룹에 있는 자식만 방문해야한다.
        if CC2(t):
            first.add(tuple(t))
        return
    else:
        for i in range(s, N-start+k):
            t[k] = names[i]
            combi(k+1, i+1)


first = set()
for start in range(1, N+1):
    # 1-5 까지 구한다. 나의 첫번째 집합이 되어줄 것
    t = [0]*start
    combi(0, 0)

mymin = 1e9

for tf in first:
    second = list(set([i for i in range(1, N+1)]) - set(tf))
    first = list(tf)
    sec = CC2(second)
    if sec == True:
        sum1 = sum2 = 0
        for i in second:
            sum1 += numofpeople[i]
        for i in first:
            sum2 += numofpeople[i]
        mymin = min(mymin, abs(sum1-sum2))
if mymin == 1e9:
    print(-1)
else:
    print(mymin)
