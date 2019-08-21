import sys
sys.stdin = open('1267.txt', 'r')


def dfs_stack(arr, start_node):

    visit = []
    stack = []
    stack.append(start_node)

    while stack:
        #print(stack)
        node = stack.pop()
        #print(stack)
        if adj_list_counting[node] > 0:
            adj_list_counting[node] -= 1
        if adj_list_counting[node] == 0:
            visit.append(node)
            stack.extend(arr[node])
    return visit

def start_list_generation():

    temp_start_list = []
    for i in range(1, len(adj_list_counting)):
        if adj_list_counting[i] == 0:
            temp_start_list.append(i)
    ############### 후보들 제대로! 다시 했음.
    # temp_start_list = []
    # temp = []
    # for i in range(len(mat)):
    #     if i % 2 == 1: # 1 3 5
    #         temp.append(mat[i])
    # for i in range(len(mat)):
    #     if i % 2 == 0:
    #         if mat[i] not in temp:
    #             temp_start_list.append(mat[i])
    start_list = list(set(temp_start_list))
    return start_list

for tc in range(1, 11):
    V, E = map(int, input().split())
    mat = list(map(int, input().split()))

    # 갈수있는곳 진출차수 인접리스트
    adj_list = [[] for _ in range(V+1)] # 1001까지 있다. index error 방지

    # 나한테 올애들의/ 진입차수의 수
    adj_list_counting = [0 for _ in range(V+1)]

    for i in range(len(mat)): #앞으로 갈 노드
        if i%2 == 0:
            adj_list[mat[i]].append(mat[i+1])
            # 나한테 올 노드의 수 리스트
            adj_list_counting[mat[i+1]] += 1

    #print(adj_list)
    # start_node 후보들을 담은 list 완성
    start_list = start_list_generation()

    # dfs stack에 start_node 후보와 adj_list를 넣어준다.
    result = []
    for start in start_list:
        res = dfs_stack(adj_list, start)
        #print(res)
        result.extend(res)
    print(f'#{tc}', ' '.join(map(str, result)))





'''
def dfs_stack(arr, start_node):
    visit = []
    stack = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if adj_list_counting[node] > 0:
            adj_list_counting[node] -= 1
        if adj_list_counting[node] == 0:
            visit.append(node)
            stack.extend(arr[node])
    return visit

def start_list_generation():
    temp_start_list = []
    for i in range(1, len(adj_list_counting)):
        if adj_list_counting[i] == 0:
            temp_start_list.append(i)
    start_list = list(set(temp_start_list))
    return start_list

for tc in range(1, 11):
    V, E = map(int, input().split())
    mat = list(map(int, input().split()))
    adj_list = [[] for _ in range(V+1)] 
    adj_list_counting = [0 for _ in range(V+1)]
    for i in range(len(mat)): 
        if i%2 == 0:
            adj_list[mat[i]].append(mat[i+1])
            adj_list_counting[mat[i+1]] += 1
    start_list = start_list_generation()
    result = []
    for start in start_list:
        res = dfs_stack(adj_list, start)
        result.extend(res)
    print(f'#{tc}', ' '.join(map(str, result)))
'''