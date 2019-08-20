import sys
sys.stdin = open('1219.txt', 'r')

def dfs_stack(table):
    visited = [False]*100
    stack = []
    stack.append(0)
    while stack: # stack이 비지 않았다면,
        node = stack.pop() # 0
        if not visited[node]: # 거짓이라면 실행
            visited[node] = True # true로 바꾸고,
            if 99 in table[node]:
                return 1
            stack.extend(table[node])
    return 0


for tc in range(1, 11):
    t, n = map(int, input().split())
    mat = list(map(int, input().split()))
    standard = [[] for i in range(100)] #인접리스트!
    #print(standard)
    for i in range(len(mat)):
        if i%2 == 0:
            #print(i)
            standard[mat[i]].append(mat[i+1])
    print(f'#{tc} {dfs_stack(standard)}')





