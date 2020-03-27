import sys
sys.stdin = open('1941.txt', 'r')


from collections import deque

def combi(depth, idx, d_cnt, my_lis):
    global total_cnt
    if d_cnt > 3: # d_cnt가 3을 초과하면 return 한다.
        return
    if depth == 7:
        total_cnt += check(my_lis)
        return
    for j in range(idx, 25):
        if not combi_visited[j]:  # 아직 방문한적이 없다면,
            combi_visited[j] = 1
            combi(depth+1, j+1,d_cnt+lis[j], my_lis+[j])
            combi_visited[j] = 0

di = [0,0,-1,1]
dj = [-1,1,0,0]
def check(my_combi):

    visisted = [0] * 7
    visisted[0] = 1
    cnt = 1
    q = deque([(my_combi[0]//5, my_combi[0]%5)])
    while q:
        a = q.popleft()
        x,y = a[0], a[1]
        for k in range(4):
            newX,newY = x+di[k], y+dj[k]
            for j in range(7):
                if visisted[j]:
                    continue
                xx,yy  =  my_combi[j] // 5,my_combi[j] % 5
                if xx == newX and yy == newY: # 좌표가 같다면
                    q.append((xx, yy))
                    visisted[j] = 1
                    cnt+=1
    if cnt == 7:
        return 1
    else:
        return 0

lis = []
for i in range(5):
    # Y -> 1, S -> 0
    temp = list(map(lambda x:1 if x == 'Y' else 0, list(input())))
    print(temp)
    lis.extend(temp)
print(lis) # 1) 1차원 배열로 만듦
total_cnt = 0
combi_visited = [0] * 25
combi(0,0,0, [])
print(total_cnt)