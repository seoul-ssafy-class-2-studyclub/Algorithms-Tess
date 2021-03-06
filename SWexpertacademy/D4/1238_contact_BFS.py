import sys
sys.stdin = open('1238.txt', 'r')

# def check(arr):
#     result = 0
#     for _ in visited:
#         if _ == False:
#             result += 1
#     return result
'''
#1 17 
#2 96


#3 49 
#4 39 
#5 49 
#6 1 
#7 28 
#8 45 
#9 59
#10 64 
'''

def Search(s):
    visit_order = []
    queue = []
    queue.append(s)
    while queue:
        temp = []
        for q in range(len(queue)):
            node = queue.pop(0)
            if visited[node] == 0: # 방문하지 않은 노드만 가기위해서
                visited[node] = 1
                queue.extend(adj_list[node]) # 자손을 추가
                temp.append(node) # 추가한 다른 부모의 같은계층에 속한 모든 자손을 트랙킹하기 위해서
        visit_order.append(temp) # 계층별 추가
    return visit_order

for tc in range(1, 11):
    length, start = map(int, input().split())
    data = list(map(int, input().split()))

    # 방문확인리스트
    visited = [0 for i in range(length)]

    # 인접리스트
    adj_list = [[] for i in range(length)]
    for i in range(length):
        if i%2 == 0:
            adj_list[data[i]].append(data[i+1])
    res = Search(start)
    if res[-1] == []:
        print(f'#{tc} {max(res[-2])}')
    else:
        print(f'#{tc} {max(res[-1])}')






