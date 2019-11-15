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
names = [i for i in range(1, N+1)]

# BFS CC로 확인해야 한다.
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
            flag = 1
            break
    return True if flag else False


def combi(k, s):
    global start, names, t, N, mymin
    if k == start:
        if CC2(t):
            second = list(set([i for i in range(1, N + 1)]) - set(t))
            if CC2(second):
                sum1 = sum2 = 0
                for i in second:
                    sum1 += numofpeople[i]
                for i in t:
                    sum2 += numofpeople[i]
                mymin = min(mymin, abs(sum1 - sum2))
        return
    else:
        for i in range(s, N-start+k):
            t[k] = names[i]
            combi(k+1, i+1)

mymin = 1e9
for start in range(1, N+1):
    # 1-5 까지 구한다. 나의 첫번째 집합이 되어줄 것
    t = [0]*start
    combi(0, 0)

if mymin == 1e9:
    print(-1)
else:
    print(mymin)
